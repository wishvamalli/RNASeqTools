#takes in chromosome and strand and produces a list filtered for the given criteria
#input format python sep.py chromosome strand
#the main_source is hard-coded into the script (join.ucsc_vega_sorted.txt)
#the main_source file should be tab seperated and should have the chromosome name (chr1 ...) and the strand (+/-) on the second
#and the third respectively.
#the entire line which fills the criteria (i.e. having the same chromosme and the strand) will be printed out.
#the gen.py script which activates this script will redirect it to a file aptly names on the filtered folder (which should pre exist)

import sys
chr = sys.argv[1]
strand = sys.argv[2]
chromPos = int(sys.argv[3])
strandPos = int(sys.argv[4])
inputFile = sys.argv[5]


for line in open(inputFile,'r'):
    if (line.split('\t')[chromPos].strip()==chr and line.split('\t')[strandPos].strip()==strand):
        print line.split('\n')[0]
