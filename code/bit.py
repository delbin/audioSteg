def getbit( integer, pos ):
   "This returns the bit at given position"
   value=(integer & (1 << pos) != 0)
   if value==False:
   	return 0
   else:
   	return 1

def changeLSB(integer, bit):
	"This replaces the LSB of integer with given bit"
	return ((integer & ~1) | bit)
	
def changeBIT(integer, pos, bit):
	"This replaces the <pos> th bit from right of integer with given bit"
	if bit == 1:
		return (integer | 1 << pos)
	if bit == 0:
		return (integer & ~(1 << pos))



