import sys #to accept command line arguments

#open file for reading
cFile = open(sys.argv[1], "r")


#initialize sequence counter
headcount=0
cSeq="" #create empty string
names=[] #create empty lists
seq=[]
seqlen=[]

#read infile line by line
for line in cFile:
	if(line[0] == ">"):

		#if header line, increase header count, add name to list	
		headcount+=1 
		cName=line[1::].strip()
		names.append(cName) 
		if(headcount != 1): #if this isn't the first header, we should have sequence already

			#add sequence and sequence length to respective lists
			seq.append(cSeq.strip())
			seqlen.append(len(cSeq.strip()))
			cSeq="" #reset sequence
	else:
		cSeq+=line.strip() #concatenate previous line of sequence

#one more time for last line of file
seq.append(cSeq.strip())
seqlen.append(len(cSeq.strip()))

#print number of sequences, all unique sequence lengths, and reformatted data
setSeqLen=list(set(seqlen))
print headcount , " ".join(str(e) for e in setSeqLen)
for n,s in zip(names,seq):
	print n,s
