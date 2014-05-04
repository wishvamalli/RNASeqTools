""" peakcall.py - identifies peaks from a given wig file"""
#Input - tab delimited file; Format  - chr,start,stop,strand
__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "Copyright 2012"
__status__ = "Prototype"
__version__ = "0.0.1"
__license__ = "GPL"
try:
    import psyco
    psyco.full()
except:
    pass

import sys


#define user inputs, this is as a backup for testing so that i don't need to type all the params every time. Will take out in final.
#chromosome = 'chr1'
#inputstrand = '-'
#wigfile = 'chr1_negative.wig'
#minthreshhold = 5
#minpeaksize = 40

#takes in userinput.
chromosome = sys.argv[1]
inputstrand = sys.argv[2]
wigfile = sys.argv[3]
minthreshhold = int(sys.argv[4])
minpeaksize = int(sys.argv[5])
gapfile = sys.argv[6]
# a typical input 241-237:sandbox wishvaherath$ python peakcall.py chr1 - chr1_negative.wig 5 40
dic = {} #this is the dictionary which will contain all the data from the wig file
#first the script adds the entire wig file to a dictionary. WARNING - you need a considerable amount of ram. This mac has 4Gig and it seems sufficent.
for line in open(wigfile,'r'): #loops through the file reading each line and adds it to the dictionary - dic
    temp = line.split('\t') 
    pos = temp[0]
    
    if pos.isdigit(): #prevents the header giving an error.
        pos = int(pos)
        count = int(temp[1].split()[0])
        
        dic[pos] = count #dic is the dictionary

line = '' #reusing line and temp variables
temp = ''
prevplace = 0


peak={} # this will act as a temporary dictionary to contain the data of a peak

for line in open(gapfile,'r'): #reads the file containing the gap positions line by line    
    temp = line.split('\t')
    chr = temp[0].split()[0] 
    strand = temp[3].split()[0]
    
    if chr==chromosome and strand == inputstrand: #This limits the search for only the given chromosome and strand.
        starts = int(temp[1])
        stops = int(temp[2]) #start and stop coordinates of the gap
        
        prevplace = starts-1 #this holds the previous stop+1 
        
        for i in range(starts,stops+1): #why use stops+1?
        
            try:
                d =  dic[i] # checks if the position contains a value in the dictionary. if not there will be an error.
                #ithere IS a count value for the given position
                if d > minthreshhold: #provides a threshhold value for the peaks
                    #itpiht there is a count for the position and it is more than the threshhold
                    if (i-prevplace) == 1: #checks if the current position is adjecent to the  previous. i.e checks for continuity.
                        peak[i] = int(d)
                        d=0
                    else:
                        #itpiht there is gap i.e the peak has stopped! So showld display the peak.
                        q=2
                prevplace = i      
            except :
                q=2 #The peak has ended
                if len(peak) > minpeaksize:
                    
                    peakpoints = peak.values()
                    peakkeys = peak.keys()
                    #print 'max', max(peakpoints)
                    #print 'min',min(peakpoints)
                    #print 'length',len(peakpoints)
                    c = len(peakpoints)-1
                    tot = 0
                    for i in peakpoints:
                        tot = tot+int(i)
                    print chr,'\t',strand,'\t',min(peakkeys),'\t',max(peakkeys),'\t',max(peakpoints),'\t',min(peakpoints),'\t',len(peakpoints),'\t',chr,':',min(peakkeys),'-',max(peakkeys),'\t',tot

                    peak.clear() #resetting the peak dictionary
                else:
                    peak.clear()
                    
    #to run after the loop ends (this is for peaks which end with the range). i.e the peaks which continues throught the annotations, i.e. the extensions?
                    
    if len(peak) > minpeaksize:
                    peakpoints = peak.values()
                    peakkeys = peak.keys()
                    #print 'max', max(peakpoints)
                    #print 'min',min(peakpoints)
                    #print 'length',len(peakpoints)
                    c = len(peakpoints)-1
                    tot = 0
                    for i in peakpoints:
                        tot = tot+ int(i)
                    print chr,'\t',strand,'\t',min(peakkeys),'\t',max(peakkeys),'\t',max(peakpoints),'\t',min(peakpoints),'\t',len(peakpoints),'\t',chr,':',min(peakkeys),'-',max(peakkeys),'\t',tot
                    
                    
                    #print peak
                    #print 'gap by last line...'
                    peak.clear() #resetting the peak dictionary
    else :
        peak.clear()
        
            
    #print '-----------------------------'
    peak.clear()
                
    
    
    
    
        
                
    
