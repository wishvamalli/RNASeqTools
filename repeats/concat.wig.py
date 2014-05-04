#given a folder containing wiggle files this concatenates it...

import sys
import os
folderName = sys.argv[1]

fileList = os.listdir(folderName)

for file in fileList:
    #print file.split('.')[0],file.split('.')[1]
    chrName = file.split('.')[0].strip()
    strandText = file.split('.')[1].strip()
    if strandText == 'pos':
        strand = '+'
    if strandText == 'neg':
        strand = '-'

    #print chrName, strand
    for line in open(folderName+'/'+file,'r'):
        print chrName,'\t', strand, '\t', line.strip()
