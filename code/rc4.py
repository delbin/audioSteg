def keyarray( length, key ):
	S=list(xrange(8))
	K=list(xrange(length))
	for i in range(0, 8):
	    S[i] = i
	
	j = 0
	keylength=len(key)
	for i in range(0, 8):
	    j = (j + S[i] + ord(key[i % keylength])) % 8
	    temp=S[i]
	    S[i]=S[j]
	    S[j]=temp
	
	i = 0
	no = 0
	while (no<length):	
	    i = (i + 1) % 8
	    j = (j + S[i]) % 8
	    temp = S[i]
	    S[i] = S[j]
	    S[j] = temp
	    K[no] = S[(S[i] + S[j]) % 8]
	    #print K[no] , "\n"
	    no=no+1
	   
	return K

