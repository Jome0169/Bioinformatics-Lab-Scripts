import os 



GeneLocationClean = []

NewFileToBeWritten = open("MitoGenesFinal", "a+")

def LocationInput(NameofLocation):
	UnprocList = []
	GenelocationFile = open(NameofLocation, "r")
	CutOntab = GenelocationFile.read().split("\r")
	for item in CutOntab:
		UnprocList.append(item.split("\t"))
	for itme in UnprocList:
		GeneLocationClean.append(itme[2:5])
	del GeneLocationClean [0]


RealFile = ""
		
def MitochondriaInput(MitoFile):
	global RealFile
	cleaner = []
	MitoFileRead = open(MitoFile, "r")
	Readtoram = MitoFileRead.read()
	RemoveNewline = Readtoram.replace('\n', '').replace(">C7_mtDNA", '')
	RealFile += RemoveNewline.replace('\r', '')

def RvrseComplement(seq):
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
	ComplimentList = []
	for item in seq:
		if item in complement:
			ComplimentList.append(item.replace(item,complement[item]))
	Finalized = ''.join(ComplimentList)
	return Finalized
	
def SeqDaSequence(ListofLocation, MitochodriaSequence):
	for triplet in ListofLocation:
		if triplet[2] > triplet[1]:
			print len(MitochodriaSequence)
			print triplet[0]
			print triplet[2], triplet[1]
			print int(triplet[2]) - int(triplet[1])
			print "MITO SEQ LENGTH", len(MitochodriaSequence[int(triplet[1]) - 1:int(triplet[2])])
			print MitochodriaSequence[int(triplet[1]) - 1:int(triplet[2])]
			print "\n"
			
		elif triplet[1] > triplet[2]: 
			print "WE GOT A NEGATIVE GENE!!!"
			print triplet[0]
			print triplet[1], triplet[2]
			print int(triplet[1]) - int(triplet[2])
			print  "MITO SEQ LENGTH", len(MitochodriaSequence[int(triplet[1])-1:int(triplet[2]):-1])
			print MitochodriaSequence[int(triplet[1])-1:int(triplet[2]):-1]
			print "RVS COMPL"
			X = RvrseComplement(MitochodriaSequence[int(triplet[1])-1:int(triplet[2]):-1])
			print RvrseComplement(MitochodriaSequence[int(triplet[1])-1:int(triplet[2]):-1])
		
			print "\n"
		

		# if triplet[2] > triplet[1]:
		# 	 NewFileToBeWritten.write(triplet[0]) 
		# 	 NewFileToBeWritten.write("\n") 
		# 	 NewFileToBeWritten.write(MitochodriaSequence[int(triplet[1]) - 1:int(triplet[2]) - 1])
		# 	 NewFileToBeWritten.write("\n")
		# elif triplet[1] > triplet[2]: 
		# 	NewFileToBeWritten.write(triplet[0]) 
		# 	NewFileToBeWritten.write(" Negative Gene!") 
		# 	NewFileToBeWritten.write("\n")
		# 	X = RvrseComplement(MitochodriaSequence[int(triplet[1])-1:int(triplet[2]) - 1:-1]) 
		# 	print triplet[0], '\n', X
		# 	NewFileToBeWritten.write(X)
		# 	NewFileToBeWritten.write("\n")


LocationInput("genelist.txt")
MitochondriaInput("mitochondria.fasta")
SeqDaSequence(GeneLocationClean, RealFile)

