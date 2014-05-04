#this script takes in a counts file and produces RPKM values for individual genes.
from __future__ import division
import sys

fName = sys.argv[1]
seqDepth = int(sys.argv[2])
countsDic = {}
lengthDic = {}

print seqDepth
for line in open(fName,'r'):
    temp = line.strip().split('\t')
    
    if temp[2] == 'exon':
        chr = temp[1]
        start = int(temp[3])
        stop = int(temp[4])
        length = stop - start
        hits = int(temp[5])
        geneID = temp[8].split('"')[1].split('"')[0]
        if geneID[-1:]=='P':
            geneID = geneID[:-1]
        #print line.split()
        #print chr,start,stop,hits,geneID

        if geneID in countsDic:
            #geneId has already been added
            countsDic[geneID] = countsDic[geneID]+hits
            lengthDic[geneID] = lengthDic[geneID]+length
        else:
            countsDic[geneID] = hits
            lengthDic[geneID] = length


k = countsDic.keys()
k.sort()

for gene in k:
    totalCounts = countsDic[gene]
    totalLength = lengthDic[gene]/2
    if totalCounts == 0:
        print gene, totalCounts,totalLength,0
    else:
        print gene, totalCounts,totalLength, (totalCounts/(totalLength/1000))/seqDepth * 1000000
