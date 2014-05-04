#This script initiates the extraction process
#all the wiggle files with default names should be in a folder called wig and the filtered coordinate range file should be
#in a folder called filtered.
#the gen.py script could be used for the filtered files.


import sys
import os

startPos = sys.argv[1]
stopPos = sys.argv[2]
filteredFolder = sys.argv[3]
wigFolder = sys.argv[4]




for files in os.listdir(filteredFolder):
    chr = files.split('_')[0]
    strand = files.split('_')[1]
    #print strand
    if strand == 'positive':
        s = 'pos'
    elif strand == 'negative':
        s = 'neg'
    
    
    vegapath =  filteredFolder+'/'+files
    wigpath = wigFolder+'/'+chr+'.'+s+'.wig'
    
    
    
    command = 'python scripts/gapman_auto.py '+ vegapath+ ' ' +wigpath+ ' '+ startPos+ ' ' + stopPos
    os.system(command)  #activates the gapman_auto.py script with all the available chr-strand combinations.
    
