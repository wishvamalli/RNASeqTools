

import sys

list = []

for line in open(sys.argv[1],'r'):
    list.append(line.strip())

b = 0

for line in open(sys.argv[2],'r'):
    temp = line.strip().split('\t')
    chr = temp[0].strip()
    start = int(temp[2].strip())
    stop = int(temp[3].strip())
    strand = temp[1].strip()
    #print chr,start,stop,strand
    for i in list:
        temp2 = i.strip().split('\t')
        chr1 = temp2[6].strip()
        start1 = int(temp2[8].strip())
        stop1 = int(temp2[9].strip())
    
        strand1 = temp2[7].strip()
        #print chr1,start1,stop1,strand1
        if chr == chr1 and start == start1 and stop == stop1 and strand == strand1 :
            #print line.strip()
            b = 1

    if b == 0:
        print line.strip()
    if b == 1:
        b = 0
