#gets a region from a file (vega) and then extracts the info corresponding to that region from a wig file
#chr and strand should be on the fourth and the fifth columns respectively.





import sys

vega = sys.argv[1] #the path for the genomic regions
wig = sys.argv[2] #the path for the wiggle file
startPos = int(sys.argv[3]) # position of  start
stopPos = int(sys.argv[4]) # position of stop



try:
    wigfile = open(wig,'r')
except:
    exit()

wigline = wigfile.readline() #reads the first line of the wig file

while not wigline.split('\t')[0].isdigit(): #moves through the wiggle file line by line to bypass the header (with text)
    wigline=wigfile.readline() # at this point the wig file pointer is at the first line of the data part of the wig file.
    
    


    
totalcounts =  0 #the varialbe which contains the count of 'hits' for that region (actually the area!)




def readwig(start,stop):
    global wigline
    global wigfile
    global totalcounts
    global line
    
    
    
    if wigline=='' or wigline.split('\t')[0]=='' :
        print 'Incorrect file?',vega
        sys.exit() 
    while (int(wigline.split('\t')[0]) < start):
        wigline = wigfile.readline()
        if wigline=='':
            #print 'two',vega
            sys.exit()
            
    #print 'first loop end, vega = ',start,'wigfilestart = ', wigline.split('\t')[0]
        
        
    
    if wigline.split('\t')[0] >= start:
        totalcounts = 0
        
        while (int(wigline.split('\t')[0]) <= stop):
            totalcounts= totalcounts+int(wigline.split('\t')[1])
            wigline = wigfile.readline()
            if wigline=='':
                #print 'three',vega
                sys.exit()
        #print 'second loop end, vegstop = ', stop,'wigfilestop=', wigline.split('\t')[0], 'total =',totalcounts
    a = line.strip()
    print a, '\t', start,'\t',stop,'\t','totalcounts=',totalcounts
    
    
    
        
    
        


for line in open(vega,"r"):
    vegafile = line.split('\t')
    
    vegastart = int(vegafile[startPos])
    vegastop = int(vegafile[stopPos])
    
    
    readwig(vegastart,vegastop) #from the vega file strips out the start and stop and sends to the readwig function
    
    
    
