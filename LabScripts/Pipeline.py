import os

y = os.popen('ls *.fq.rtf')
K = y.read()
FileNumb = len(K) / 2
List_Files = K.split()
ListList = []

# 

def ConCat(FILES):
	FileNumb = len(FILES)
	count = 0
	count1 = 2
	for item in FILES:
		if count1 <= FileNumb:
			print FILES[count:count1]
			ListList.append(FILES[count:count1])
			count += 2
			count1 += 2
		else:
			break


empty = []

def smasher(doubles):
	smasher_length = len(doubles)
	for item in doubles:
		for pair in item:
			length_Name = len(pair)
			empty.append(pair[0:length_Name - 9])

set1 = []
set2 = []

def seperator(Tings):
	for group in Tings:
		set1.append(group[0])
		set2.append(group[1])
	return empty
		


ConCat(List_Files)
smasher(ListList)
unique_list = set(empty)
seperator(ListList)


for item in set1:
	for thing in set2:
		for thing2 in unique_list:
			os.system("cat {} {} > {}.fq".format(item, thing, thing2))


