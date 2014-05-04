import os
import sys

#chrList = ['chr1','chr2','chr3', 'chr4', 'chr5', 'chr6', 'chr6', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY']

chrList = ['chr7']
for i in chrList:
    t = 'bsub "python findrepeatsingaps.py slim.hg18.repeatmaster.txt gaps.rhe001.txt ' + i + '  + > /home/wishvabh99/bioscope_data/SUBMP/LTR/repeatmasker_excludingrefSeq/'+ 'output'+ i+'+'+'.txt"'
    print t
    os.system(t)
    t ='bsub "python findrepeatsingaps.py slim.hg18.repeatmaster.txt gaps.rhe001.txt ' + i + '  - > /home/wishvabh99/bioscope_data/SUBMP/LTR/repeatmasker_excludingrefSeq/'+ 'output'+ i+'-'+'.txt"'
    print t
    os.system(t)
