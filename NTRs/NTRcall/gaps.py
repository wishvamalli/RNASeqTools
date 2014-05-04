""" gaps.py - finds gaps withing annotated regions """

__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "Copyright 2012"
__status__ = "Prototype"
__version__ = "0.0.1"
__license__ = "GPL"

#gaps.py
#finds gaps in a list of annotated regions.
#Input - tab delimited file of strand specific annotated regions (e.g refseq)
#Input format - chr,start,stop,strand,Info - Sorted Ascending in the following order - chr,start,strand # corrction 18/8/2010 chr,strand,start
#Output - list of ranges of the 'gaps' between the given annotations.
import sys
try:
    annotfile = sys.argv[1] #The input file
except:
    print 'Incorrect input.'
    print ' python gaps.py <Inputfile>'
#Initialization of variables which describe the range in the line immediately before.
prevstop = 0
prevchr = 'a'
prevstrand = '~'
for line in open(annotfile,'r'): #reads the annotation file line by line
    #stripping data from the current line  
    temp = line.split('\t')
    chr = temp[0].strip()
    strand = temp[3].strip() 
    starts = int(temp[1])
    ends = int(temp[2])
    #info = temp[8].split('\n')[0] #this field in unique for the refseq annotation   
    #This begins the comparing process   
    if prevstop > starts: #usually this cannont be the case, if this is true then either there is an overlap between two annotations or the annotation range is on a different chromosome / strand
        if (prevchr == chr and prevstrand ==strand): #checks to see if its the same chr/strand combination; if this is the case then its an overlap.
            if prevstop < ends: # Checks if the current seqments if fully immersed in the previous one. i.e. a 100! overlap.
                prevstop = ends # if ends is greater then shifts the prevstop position and does not print anything as there is not 'gap'
        else:
            #its a change in either the chromosme or the strand
            prevstop = -1 #resets the prev position and prints the gap from start to the currenet position
            print chr,'\t',prevstop+1,'\t',starts-1,'\t',strand
    else:
            a=1
            #A normal sequential annotation.
            print chr,'\t',prevstop+1,'\t',starts-1,'\t',strand
    prevstop = ends
    prevchr = chr
    prevstrand = strand
    
    
