from __future__ import print_function
import wave
import math
import rc4
import bit

f=wave.open("output.wav","r")
numframes=f.getnframes()
data=f.readframes(numframes)

frames2=[ord(c) for c in data]
framecount=44;
length=0

key= raw_input("Enter the key:")

base=math.ceil(math.log((((numframes*4)-44)/8) , 2))

for j in range(0,int(base)):
		length=length + (2**j) *(frames2[framecount] & 1 )
		framecount = framecount + 1
		
count=0
K=rc4.keyarray(length*8, key)
for i in range(0,length):
	number=0
	for j in range(0,8):
		number=number + (2**j) *(bit.getbit(frames2[framecount],K[count]) )
		framecount = framecount + 1
		count=count+1
		
	print (chr(number) , end="")
	
print ("\n")
