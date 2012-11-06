#!/usr/bin/python

import sys
import math
import wave
import bit
import rc4

f=wave.open("Msg.wav","r")

numframes=f.getnframes()
channels=f.getnchannels()
sampwidth=f.getsampwidth()
framerate=f.getframerate()
comptype=f.getcomptype()
data=f.readframes(numframes)
f.close()

frames=[ord(c) for c in data]

msg= raw_input("Enter the message:")
key= raw_input("Enter the key:")
integerrep=[ord(c) for c in msg]
framecount=44;

length=len(msg)
print "Length of the message ", length*8

#if (length*8 > (numframes*4-44)):
#	print ("The text is too long for the selected .wav file")
#	sys.exit(0)
	
base=math.ceil(math.log((((numframes*4)-44)/8) , 2))
	
#print base
print int(base)

for j in range(0,int(base)):
		frames[framecount]=bit.changeLSB(frames[framecount],bit.getbit(length,j))
		framecount=framecount+1

K=rc4.keyarray(length*8, key)		
count=0
for i in range(0,length):
	for j in range(0,8):
		frames[framecount]=bit.changeBIT(frames[framecount],K[count],bit.getbit(integerrep[i],j))
		framecount=framecount+1
		count=count+1		

		
output=[chr(c) for c in frames]
print len(frames)
out=wave.open("output.wav","w")
out.setnchannels(channels)
out.setsampwidth(sampwidth)
out.setframerate(framerate)
out.setnframes(numframes)
out.setcomptype(comptype, 'NONE')

for i in range(0, len(output)):
	out.writeframes(output[i])


