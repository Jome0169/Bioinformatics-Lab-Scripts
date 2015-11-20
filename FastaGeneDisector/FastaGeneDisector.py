#The goal of this program is going to be go throught a fasta formatted file and look for genes that have similar name. Output a new file for every gene with the proper and and the species name.

import glob, os, re, itertools

DirectFileList = "/Users/Pablo/Desktop/Code/Python_Scripts/FastaNucDisection"

ActualFiles = []

def GetFastaList(DirectoryList):
	"""
        This segment of code goes through and searches for all files that we will be using. All files end with a .txt and we append them to the file we will be using. 
        
        Arguments:
        DirectoryList is the name of the directory which we are currently in.
        In this example the directory path is known by DirectFileList
        """

	Poss = os.listdir(DirectoryList)
	for item in Poss:
		if str(item).endswith('.fasta'):
			ActualFiles.append(item)

def GeneNameList(FirstFile):
	"""
        This function foes through and creates every possible gene name file.
        It makes them all writable and gets them ready for appending of the
        rest of the genes from different organisms.

        FirstFile takes in the first file in a list of all files. THe
        assumption here is that all files will have the same or similar genes.
        This should be improved upon later.
        """
	Genes4Files = []
	ReadFile = open(FirstFile,"r")
	Debate = ReadFile.readlines()
	Names = []
	for line in Debate:
		if ">" in line:
			Names.append(line)
	for name in Names:
		Regex = re.search(r"\[(gene=[A-Za-z0-9_]+)\]", name)
		Genes4Files.append(Regex.group())
	for genename in Genes4Files:
		FILES = open(genename, "w+")



GnSeqDict = {}
IterationCount = 0


def GeneFileParser(AllFiles):
    """
    This command goes through and parses each file. It opens files iterably. It
    then looks for the > sign which acts as a signifier that a gene is present

    Argument: Takes in a list of all the fasta files in the directory.
    Currently the files that end with .txt

    Outputs: A dictionary with the GENE NAME followed by the reads.
    """
	GeneNames = []
	GeneSeq = []
	global IterationCount
	global GnSeqDict
	countoffiles = 0
	numberoffiles = len(AllFiles)
	for filename in AllFiles:
		if numberoffiles >= countoffiles:
			with open(AllFiles[countoffiles],'r') as f:
				print f		
				ListOfSequence = list(f)
				RawUncutString = ''
				for item in ListOfSequence:
					RawUncutString += item
				StringofGenes = RawUncutString.split(">")
				SplitOnNames = []
				for item in StringofGenes:
					SplitOnNames.append(item.split("]\n"))
				SplitOnNames.pop(0)
				FinishedList = []
				for pair in SplitOnNames:
					Regex2 = re.search(r"\[(gene=[A-Za-z0-9_]+)\]", pair[0])
					FinishedList.append(Regex2.group())
				I = 0
				for pair in SplitOnNames:
					pair[0] = FinishedList[I]
					I += 1
				ListFileWriter(SplitOnNames)


			countoffiles += 1
			IterationCount += 1
	

def ListFileWriter(ListofGenes):
    """
    Goes through and writes the list of genes found to the files it should be
    appended to 

    Arguments: ListOfgenes is a list of all the genes. Assumes proper order.

    Output: Writes these genes to files in current directory.

    """
	CreatedGeneFiles = []
	FileToWriteto = os.listdir(DirectFileList)
	for item in FileToWriteto:
		if "gene" in item:
			CreatedGeneFiles.append(item)
	for file1 in CreatedGeneFiles:
		for pair in ListofGenes:
			if pair[0] == file1:
				with open(file1, "a") as appendingfile:
					appendingfile.write(">" + ActualFiles[IterationCount] + "\n")
					appendingfile.write(pair[1] + "\n")
			else: 
				pass 

	
GetFastaList(DirectFileList)
GeneNameList(ActualFiles[0])
GeneFileParser(ActualFiles)
print len(ActualFiles)

