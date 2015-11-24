import os

####
#Append all files in the directory to a list
y = os.popen('ls *.fq.rtf')
K = y.read()
FileNumb = len(K) / 2
List_Files = K.split()

print "Here is the beggining list:", List_Files, '\n'

RealList = []

for i in range(len(List_Files) / 2):
	HalfList = List_Files[-i - 1 ]
	print HalfList
	RealList.append(HalfList)

####???????????######

print RealList, '\n'


final_List = ' '.join(RealList)
		
print " Here is the final List of Files that will be downloaded and copid! \n" , final_List
print raw_input()
os.system("scp {} pabster212@ruderalis.colorado.edu:/data/pabster212/raw_data".format(final_List))

	



