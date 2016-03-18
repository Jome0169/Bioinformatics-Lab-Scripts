import os 
import sys


Location = os.getcwd()



def Tablereader(Table):
    with open(Table,'r') as f:
        for line in f:
            if line.startswith('transcript_id'):
                with open("TrimmedIsoforms.txt", 'a') as c:
                    c.write(line)
            else:
                x = line.strip('\n').split('\t')
                newlen = len(x)
                pretty = map(float,x[1:newlen])
                Sums = sum(pretty)
                if Sums >= 1 : 
                    with open("TrimmedIsoforms.txt", 'a') as c:
                        c.write(line)



for itme in os.listdir(Location):
    if itme == "TotalIsoforms2.txt":
        Tablereader(itme)

















