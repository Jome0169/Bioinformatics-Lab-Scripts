import os
import sys

Place = os.getcwd()
FastqTogetQual = []


for file in os.listdir(Place):
        if file.endswith(".fq"):
            FastqTogetQual.append(file)


def FileAnalyzer(FileItem):
    with open(FileItem, 'r') as f:
        head = [next(f) for x in xrange(20)]
        Fourthitemlist = head[3::4]
        if any("^" in s for s in Fourthitemlist):
            Phred64list(FileItem)
        else:
            Phred33list(FileItem)

def Phred64list(Name):
    with open("Phred64.txt", 'a') as f:
        f.write(Name)

def Phred33list(Name):
    with open("Phred33.txt", 'a') as f:
        f.write(Name)

for item in FastqTogetQual:
    FileAnalyzer(item)




