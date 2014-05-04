"""spliceFinder.py: Identifies splice junctions of a given gene"""
__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "Copyright 2012"
__status__ = "Prototype"
__version__ = "0.0.1"
__license__ = "GPL"

import pickle
try:
    
    import psyco
    psyco.profile()
except:
    print 'psyco not installed'

import sys
fName = sys.argv[1] #exon file
bedFile = sys.argv[2]
geneNameFile = sys.argv[3]
geneID = geneNameFile
dicBase = {}
dicJoin = {}
usedPair = []
count = 1
stops = []
starts = []
pairList = []
print 'Exons for the given gene - ', geneID
for line in open(fName,'r'):
    temp = line.strip().split('\t')
    if temp[5] == geneID:
        dicBase[count] = temp[2]+'-'+temp[3]
        chr = temp[1]
        print count, temp
        count = count+1
        
        #getting the range
        starts.append(int(temp[2]))
        stops.append(int(temp[3]))

lowestStop = min(stops)-1
highestStart = max(starts)
for i in range(1,len(dicBase)):
    startStop = dicBase[i]
    
        

    for j in range(1,len(dicBase)):
        
        if dicBase[j] == startStop:
            
            pair =  startStop+'<-->'+dicBase[j+1]
            if pair in usedPair:
                pass
            else:
                #print pair
                pairList.append(pair)
                usedPair.append(pair)
                
pL = []

for item in pairList:
    pL.append(item.split('<-->')[0].split('-')[1]+'--'+item.split('<-->')[1].split('-')[0])
#print 'Known exon exon junctions'
#print pL
    
    


#going to read the all_exons file

junctions = []

#print 'exon exon junctions based on spliced reads'
for line in open(bedFile,'r'):
    temp = line.strip().split()
    if temp[0] == chr and lowestStop<= int(temp[1]) and highestStart >= int(temp[2]):
        #print temp[0],int(temp[1])-1,int(temp[2]), int(temp[3])
        a = int(temp[1])-1
        junctions.append(str(a)+'--'+temp[2]+'@'+temp[3])

#print junctions

# comparing the two lists junctions (from bed file) and pL (paired list from the exon exon junctions)
for splice in junctions:
    if splice.strip().split('@')[0] in pL:
        #print splice,"known"
        pass
    else:
    
       # if splice.strip().split('@')[1] <> "":
            #print geneID
            #check if the splice connects two exons of the same transcript
        jStart = int(splice.strip().split('--')[0])
        jStop = int(splice.strip().split('--')[1].split('@')[0])
        if (jStart in stops) and (jStop in starts):
            print geneID,'\t', splice,'\t',"unknown,connecting2known"
            continue
            #if (jStart in stops) or (jStop in starts):
                #print geneID,'\t', splice,'\t',"unknown,connecting1unKnown"

        
            


        
