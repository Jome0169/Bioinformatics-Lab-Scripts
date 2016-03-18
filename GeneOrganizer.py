import os
import sys
import re

Location = os.getcwd()

FilesToRun = []


for item in os.listdir(Location):
    if item.endswith('TrimmedIso.txt'):
        FilesToRun.append(item)


def FileReader(FILENAME):
    global Groupname2
    global Trinity
    Groupname = FILENAME.replace("TrimmedIso.txt", '')
    Groupname2 = Groupname.replace("final_", '')
    with open(FILENAME, 'r') as f:
        THeFile = f.read()
        Zerp = HashTableCreator(THeFile)
        Dictioanry = GeneDictCreator(Zerp)
        Names = SpeciesNames(Zerp)
        DictOfGeneIsos= Grouper(Zerp, Dictioanry)
        for key,value in DictOfGeneIsos.iteritems():
            if len(value) > 1:
                Iteratethrought = len(value)
                Z  = RetrieverGenesNamesForSpecies(Names, value)
                DictOfGeneIsos[key] = Z
            elif key == '':
                pass
            else:
                Z = RetrieverGenesNamesForSpecies(Names, value)
                DictOfGeneIsos[key] = Z
        FileWriter(Groupname2, DictOfGeneIsos)


def HashTableCreator(ReadFile):
    # Returns a list of list with everyline read being a new list.
    # Splits on tabs also so seperates each COLUMN into a new thing
    IterableList2 = ReadFile.split('\n')
    NewList = []
    for item in IterableList2:
        z = item.split('\t')
        NewList.append(z)
    return NewList
    

def GeneDictCreator(LIST1):
    # Creates a dictiomnary with the first item (index 0) of the called list
    # being a key and initialiing hte dicitonary with empty list []. The
    # Trimmed gene call here takes out the _iNUM aspect. This helps isolate
    # unique genes.
    HashTown = {} 
    for itme in LIST1[1:]:
        TrimmedGene = re.sub(r'_i\w+', '', itme[0])
        HashTown[TrimmedGene] = []
    return HashTown


def SpeciesNames(ReadFile):
    NameList = []
    for items in ReadFile[0]:
        if items == 'transcript_id':
            pass
        else:
            NameList.append(items)
    return NameList

def Grouper(ReadFile, DICT):
    # Takes in the readfile and a dicitonary with the key of the dictionary
    # being the gene name. Trimms off the isoform number, checks to see if this
    # gene is already in the dictionary and then adds this isoform to the list
    # in the VALUE of the gene in the dictionary. Returns updated dictionary
    Prettylist = []
    for item in ReadFile:
        TrimmedGene = re.sub(r'_i\w+', '', item[0])
        if TrimmedGene in DICT:
            DICT[TrimmedGene].append(item)
        else:
            pass
    return DICT


def RetrieverGenesNamesForSpecies(NameList, IsoForm):
    # Takes in the values from a dictionary as well as the names of every
    # column. Takes the index of this item. THen goes through the values from
    # the dictionary and matches the indexed item(THE NAME) with the
    # appropraite values that corresponds to this individal int his list. 
    # It also takes in a list of the isoform names and return the isoform
    # iteration
    VarietyWithProp = {}
    for item in NameList:
        IndexToTake = NameList.index(item)
        TotalGenesProp = []
        IsoFormNumberuntrimmed = []
        IsoFormNumber = []
        for List in IsoForm:
            IsoFormNumberuntrimmed.append(List[0])
            TotalGenesProp.append(List[IndexToTake + 1])
        for iso in IsoFormNumberuntrimmed:
            Number = iso.split("_")[-1].strip('i')
            IsoFormNumber.append(Number)
        UpdatedGeneProp = GetFPKMValue(Groupname2, item, IsoFormNumberuntrimmed, TotalGenesProp, Trinity)
        NewGeneProps = GetGeneProportions(UpdatedGeneProp)
        FinalizedLocationalData = NAlistMaker(IsoFormNumber, NewGeneProps)
        VarietyWithProp[item] = FinalizedLocationalData
    return VarietyWithProp


def GetFPKMValue(Cultivargroup, StrainName, isofromlist, proportionlist, Trin):
    #So the purpose of this section of the code is to calculate the true FPKM
    #values of all isoforms, including those with zeros. The below code takes
    #ina  myriad of differnt files. Talk to chris if they don't make sense
    FinalizedPorportionList = []
    Nmappedreads = 0
    fpkmTotal = 0 
    C = 1
    ConservedisoLen = 0
    filetoopen = str(Cultivargroup) + '_FPKMMappedReads.txt'
    filetoopen2 = str(Cultivargroup) + '_TotalFPKM.txt'
    with open(filetoopen, 'r') as f:
        for line in f:
            if StrainName in line:
                X = line.split(" ")
                Nmappedreads += int(X[1].strip('\n'))
    with open(filetoopen2, 'r') as f:
        for line in f:
            if StrainName in line:
                X = line.split(" ")
                fpkmTotal += float(X[1].strip('\n'))
    for item in isofromlist:
        LengthofIso = Trin[item]
        ConservedisoLen += LengthofIso
    OneReadfpkm = (float(10**9) * C)/float(Nmappedreads * LengthofIso)
    OneReadTPM = float(OneReadfpkm/fpkmTotal) * 1000000
    Check = [float(i) for i in proportionlist]
    Check2 = sum(Check)
    if Check2 > 0:
        for item in proportionlist:
            NewTPM = float(item) + OneReadTPM 
            FinalizedPorportionList.append(NewTPM)
    else:
        for item in proportionlist:
            FinalizedPorportionList.append('NA')
    return FinalizedPorportionList
    

def ReadIsoLengths(TrinityAssembly):
    #Reads in the Entire Trinity Assembly in order to calculate the TPM from
    #FPKM. Since we aligned to Silas and Chrisis assembly we only need the one
    #trinity assembly from both of them. Will return a dictionary with the KEY
    # being the gene iso name and the value  being the isolength
    GeneLengthDict = {}
    with open(TrinityAssembly, 'r') as f:
        for line in f:
            if line.startswith('>'):
                X = line.split(' ')
                GeneLengthDict[X[0].strip('>')] = int(X[1].strip("len="))
    return GeneLengthDict


def GetGeneProportions(List):
    #Takes in a list of proportions and then returns the a new list of
    # proportions. If the total is zero for a lists it skips that list. 
    if 'NA' in List:
        return List
    else:
        Division = len(List)
        Total = 0
        for item in List:
            Total += float(item)
            #Call New function to calculate 
        for i in xrange(Division):
            if Total == 0:
                pass
            #To every one of these props add 1 reads tpm
            else:
                NewThing = float(List[i])/Total
                List[i] = NewThing
        return List
    

def NAlistMaker(WhereToReplace, WhattoReplace):
    # Creates a list of NAs (31 because the largest number of isoforms is 31).
    # Then takes in the isoform data numbers and then the proportions to relace
    # the NAs. Then iterates through both list in parralell. 
    ListOfNas = ['NA'] * 31
    for Loc, Prop in zip(WhereToReplace, WhattoReplace):
        ListOfNas[int(Loc)-1] = Prop
    return ListOfNas

def FileWriter(File2Write2, FinalizedDict):
    NewFileName = str(File2Write2) + 'FinalizedTableV2.txt'
    with open(NewFileName, 'a') as f:
        String2Write = ''
        for key,value in FinalizedDict.iteritems():
            if key == '':
                pass
            else:
                for Var, Prop in value.iteritems():
                    
                    String2Write += str(key) 
                    String2Write += '\t'
                    String2Write += str(Var) 
                    String2Write += '\t'
                    String2Write += str(File2Write2)
                    String2Write += '\t'
                    String2Write += '\t'.join(str(v) for v in Prop)
                    f.write(String2Write)
                    f.write("\n")
                    String2Write = ''

global Trinity
Trinity = ReadIsoLengths("Trinity.fasta")



for item in FilesToRun:
    FileReader(item)



