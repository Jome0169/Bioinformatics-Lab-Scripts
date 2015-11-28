import os


# formatter = "%r %r %r %r"
# print formatter % (1, 2, 3, 4)

# _S1_reverse_paired.fq
# _forward_paired.fq
# _S1_reverse_paired.fq
# _reverse_paired.fq

# fastq_to_fasta -i C4_S4_reverse_paired.fq -o C4REV.fasta
# fastq_to_fasta -i C4_S4_reverse_paired.fq -o C4REV.fasta
# fastq_to_fasta -i C4_S4_reverse_paired.fq -o C4REV.fasta
# fastq_to_fasta -i C4_S4_reverse_paired.fq -o C4REV.fasta
# sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C4FWD.fasta > C4FWDNew.fasta
# sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C4FWD.fasta > C4FWDNew.fasta
# sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C4FWD.fasta > C4FWDNew.fasta
# sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C4FWD.fasta > C4FWDNew.fasta
# python Wheaver.py C1FWD.fasta C1REV.fasta 
# python Wheaver.py C1FWD.fasta C1REV.fasta
# head -n 8000000 C1R_final.fasta > Start1File.fasta
# head -n 8000000 C4R_final.fasta > Start2File.fasta
# python NumberEr.py Start1File.fasta Start2File.fasta 
# cat Start1File.fasta Start2File.fasta1 > TestBatch.fasta 
# python /data/pabster212/repeatexplorer/seqclust_cmd.py -s TestBatch.fasta -f 4 -d Viridiplantae -c 9 -v OutputTest


global FileNames
FileNames = []
FileList = []
pairedComparison = []

for file in os.listdir("/Users/Pablo/Desktop/Code/Python_Scripts/CannabiPipeline"):
	if file.endswith(".fq"):
		FileList.append(file)



def FileDivider(ListOFiles):
	NumFile = len(ListOFiles)
	SamplePairs = NumFile/4
	midway = NumFile/2
	for x in xrange(0,NumFile,
	 2):
		FileNames.append(ListOFiles[x:x+2])

paired_list = []

def FilePairer(PairedfileList):
	test_list = []
	HalfMark = len(PairedfileList)/2
	Filerange = xrange(0, HalfMark)
	for item in Filerange:
		paired_list.append(PairedfileList[item] + PairedfileList[item+HalfMark])
		
def CommandWriter(PairedList):
	counter = 0
	headername  = []
	list_of_head_files = []
	forward = 'FWD.fasta'
	reverse = 'REV.fasta'
	forward1 = 'FWD1.fasta'
	reverse1 = 'REV1.fasta'
	finalized_filenames = []
	finalized_filenames1 = []
	#print PairedList
        for set1 in PairedList:
		X = set1[0].rsplit('_')
		Y = set1[2].rsplit('_')
		main_header = X[0] + '_' + Y[0] 
		headername.append(main_header)
		script_file_name = X[0] + '_' + Y[0] + "_script.sh"	 
                WriteFile(script_file_name)
		for item in set1:
                    if 'forward' in item:
                        splititem = item.rsplit('_')
                        itemlen = len(splititem[0])
                        global itemlen
			slc = str(item[0:itemlen + 1])
			finalized = slc + forward
			finalized_filenames.append(finalized)
			finalized1 = slc + forward1
			finalized_filenames1.append(finalized1)
			fastqFwd  =  "fastq_to_fasta -i %s -o %s" % (item, finalized)
			write2file(fastqFwd)
			sedfwd =  'sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g %s > %s' % (finalized, finalized1)
			write2file(sedfwd)
		    elif "reverse" in item:
       		        splititem = item.rsplit('_')
                        itemlen = len(splititem[0]) 
			slc = str(item[0:itemlen + 1])
			finalized = slc + reverse
			finalized_filenames.append(finalized)
			finalized1 = slc + reverse1
			finalized_filenames1.append(finalized1)
			fastqRev =  "fastq_to_fasta -i %s -o %s" % (item, finalized)
			write2file(fastqRev)
			sedRev = 'sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g %s > %s' % (finalized, finalized1)
			write2file(sedRev)
	iterationcount = xrange(0,len(finalized_filenames1), 2)
	for number in iterationcount:
		MiniSet = finalized_filenames1[number:number + 2]
		PrefixOffile = MiniSet[0].rsplit('_')
		FullNewFile = PrefixOffile[0] + "_full.fasta"
		HeadNewFile = PrefixOffile[0] + "_head.fasta"
		list_of_head_files.append(HeadNewFile)
		pythonwhev = 'python Wheaver.py %s %s %s' % (MiniSet[0], MiniSet[1], FullNewFile )
		write2file(pythonwhev)
		Header = 'head -n 8000000 %s > %s' % (FullNewFile, HeadNewFile)
		write2file(Header)
	pairIteration = xrange(0,len(finalized_filenames)/2, 2)
	for number in pairIteration:		
		sets = list_of_head_files[number:number + 2]
		NumberDat = 'python NumberEr.py %s %s' % (sets[0], sets[1])  
		write2file(NumberDat)
		Kittycat =  "cat %s %s > %s " % (sets[0], str(sets[1]) + '1', str(headername[counter]) + '.fasta')
		write2file(Kittycat)
		finalcommand = "python /bigdata/pabster212/RepeatExplorer/seqclust_cmd.py -s %s -f 4 -d Viridiplantae -c 9 -v %s" % (str(headername[counter]) + '.fasta', str(headername[counter]) + '_output')
		write2file(finalcommand)
		counter += 1 


def WriteFile(StringArgument):
	open(StringArgument, 'a')

def write2file(string_arugument_to_append):
	List_of_sh_files = []
	String_argument_headers = string_arugument_to_append.rsplit(' ')
        print String_argument_headers
	possibleheaders = [item[0:itemlen + 1] for item in String_argument_headers if 'C' in item]
	for file in os.listdir("/Users/Pablo/Desktop/Code/Python_Scripts/CannabiPipeline"):
		if file.endswith(".sh"):
			List_of_sh_files.append(file)
	for item in List_of_sh_files:
		if str(possibleheaders[0]) in item:
			with open(item, 'a') as myfile:
				myfile.write(string_arugument_to_append)
				myfile.write('\n')

	

		
		

		



FileDivider(FileList)
FilePairer(FileNames)
CommandWriter(paired_list)
