""" altsplice.py: Identifies the genes which show a change in their splicing profile with respect to another sample. """
__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "Copyright 2012"
__status__ = "Prototype"
__version__ = "0.0.1"
__license__ = "GPL"

#What it does
#Given a list of combined exon counts sorted according the exon and start position, this script identifies transcripts which show potential alt splicing.
#It assumes that the ratio of expression level of individual exons whithin a single transcript at a single time point is the same.

#input format:
#e.g sortedQuery, tab delimited, no header, optional [ID, chromosome,start, stop, strand, exon, strand] level for each sample,

from __future__ import division # this line makes python division behave like normal i.e with decimals
#from statlib import stats #statlib package used to do statistical calculations
import sys


#assigning command line arguments to variables
try:
    fname = sys.argv[1] # data file
    
    d0place = int(sys.argv[2]) #position of the first sample
    d8place = int(sys.argv[3]) #position of the second sample
    minAdj = float(sys.argv[4]) #min size of adjoining peaks
    minPeak = float(sys.argv[5]) #min size of peak under study
    mul = float(sys.argv[6]) # multiplication factor
    

except:
    print 'input -> python altsplice.py <datafile>  <column number of first sample> <column number of second sample> <minimum_adjoining peak size> <min peak size> <ratio of ratios>'
    exit(1)
    # Typical input python altsplice.py sortedQuery.txt 10 5 9


#variable initiation
lines = [] #array of lines belonging to the same gene and having a non zero exon count
pgenename = '' #holds the name of the previous gene
ratio = [] #the ration between the two exon counts
d0 = []
d8 = []
exonStart = []
exonStop = []
exonStartStop = []
r = 0.01
dic= {} #dictionary of lines and the start position, user for sorting
count = 0 #counts the number of lines
dir = ''
prevExonLength = 0
nextExonLength = 0
nowExonLength = 0


print 'pgenename','\t','exon','\t','pratio','\t','nratio','\t','d0prev','\t','d0now','\t','d0next','\t','d8prev','\t','d8now','\t','d8next'
for line in open(fname,'r'): #sortedQuery.txt contains the combination of all the exon counts sorted according to the gene
    temp = line.strip().split('\t')
    genename = temp[9].strip()
    #print genename
    if pgenename == genename: #The objective here is to make a list (lines) of all the exons belonging to the same gene.
        lines.append(line)
    else:
        #once the lines list is filled it gets processed here
        #sorting the lines in the exon order
        for l in lines:
            dic[int(l.strip().split('\t')[2])] = l #dictionary format startposition : line 
        #sorting dic
        dk = dic.keys()
        dk.sort() #get the list of keys i.e. startpositions and then sort that.
        for l in dk:
            t = dic[l].strip().split('\t')
            d0i = int(t[d0place])
            d8i = int(t[d8place])
            d0.append(d0i)
            d8.append(d8i)
            exonStartStop.append( str(t[0]).strip()+':'+str(t[1]).strip()+'-'+str(t[2]).strip())
            exonStart.append(int(t[1].strip()))
            exonStop.append(int(t[2].strip()))

        
        prevExonLength = 0
        nextExonLength = 0
        nowExonLength = 0

        for i in range(1,len(d0)-2):
            d0now = d0[i]
            d8now = d8[i]
            #correction for overlapped exons
            #enter current start and stop into a set
            nowSet = set(range(exonStart[i],exonStop[i]))
            prevSet = set(range(exonStart[i-1],exonStop[i-1]))
            nextSet = set(range(exonStart[i+1],exonStop[i+1]))
            #check for previous
            
            
            if len(nowSet & prevSet) == 0:
                d0prev = d0[i-1]
                d8prev = d8[i-1]
            else:
                #print 'wishva',pgenename
                d0prev = d0[i-2]
                d8prev = d8[i-2]

            if len(nowSet & nextSet) == 0:
                
                d0next = d0[i+1]
                d8next = d8[i+1]
            else:
                #print 'wishva',pgenename
                d0next = d0[i+2]
                d8next = d8[i+2]
            
            #start code for finding exons which goes completely AWOL

            if d0now < minPeak and d0now > 0 and d8now >= minPeak and d8prev > 0 and d8next > 0 and d8now / d0now >= mul:
                if (d0prev / d8prev  >=  mul/2 or d0next / d8next >= mul/2):
                #potential appearance of a peak
                    if d0prev >= minAdj and d0next>= minAdj and d8prev >= minAdj and d8next >= minAdj:
                        print pgenename,'\t', exonStartStop[i],'\t',pratio,'\t',  nratio,'\t',d0prev,'\t',d0now,'\t',d0next,'\t',d8prev,'\t',d8now,'\t',d8next,'\t', pratio >= mul\
     and nratio>= mul, int(exonStartStop[i].split('-')[1]) - int(exonStartStop[i].split(':')[1].split('-')[0]),"Extream UP"


            if d8now < minPeak and d8now > 0 and d0now >= minPeak and d0prev > 0 and d0next > 0 and d0now / d8now >= mul :
                if (d8prev / d0prev  >=  mul/2 or d8next / d0next >= mul/2) :
                #potential dissappearance of a peak                                                                    
                                                                
                    if d0prev >= minAdj and d0next>= minAdj and d8prev >= minAdj and d8next>= minAdj:
                        print pgenename,'\t', exonStartStop[i],'\t',pratio,'\t',  nratio,'\t',d0prev,'\t',d0now,'\t',d0next,'\t',d8prev,'\t',d8now,'\t',d8next,'\t', pratio >= mul\
     and nratio>= mul, int(exonStartStop[i].split('-')[1]) - int(exonStartStop[i].split(':')[1].split('-')[0]),"Extream DOWN"

            #end code for vertical comparison--------------------------------------------------------------------------------------------------------------
            if d0prev >= minAdj and d0next >= minAdj  and d8prev >= minAdj and d8next >= minAdj:
                
                if d0now >= minPeak and d8now >= minPeak:
                    
                    d0prevratio = d0now/d0prev
                    d0nextratio = d0now/d0next
                    
                    d8prevratio = d8now/d8prev
                    d8nextratio = d8now/d8next
                    
                    #previous ratios
                    if d0prevratio >= d8prevratio:
                        pratio = d0prevratio/d8prevratio
                        
                    else:
                        pratio = d8prevratio / d0prevratio
                        
                        
                    #next ratios
                    if d0nextratio >= d8nextratio:
                        nratio = d0nextratio/d8nextratio
                    else:
                        nratio = d8nextratio / d0nextratio
                    
                    
                    
                    if pratio >= mul or nratio>= mul  : # or?
                        print pgenename,'\t', exonStartStop[i],'\t',pratio,'\t',  nratio,'\t',d0prev,'\t',d0now,'\t',d0next,'\t',d8prev,'\t',d8now,'\t',d8next,'\t', pratio >= mul and nratio>= mul, int(exonStartStop[i].split('-')[1]) - int(exonStartStop[i].split(':')[1].split('-')[0]),'\t',"Normal"
                        dir = ''
                        count = count+1
            
                    
                  
        d0 = []
        d8 = []
        exonStartStop = []
        ratio = []
        dic = {}
        
        
            
        lines = []
        lines.append(line)
    pgenename = genename
                  
print count
                
        
