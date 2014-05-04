#clusters a known set of NTRs based on closeness...
from __future__ import division
import sys
n = int(sys.argv[2])
prevStop = 0
tempList = []
prevChr = ''
prevStrand = '~'

for line in open(sys.argv[1],'r'):
    temp = line.strip().split('\t')
    chr = temp[0].strip()
    strand = temp[1].strip()
    start = int(temp[2].strip())
    stop = int(temp[3].strip())

    if chr == prevChr and prevStrand == strand and (start - prevStop) <=  n:
        print '@@@@@@@', start - prevStop, start,prevStop
        tempList.append(line.strip())
    else:
        if len(tempList)>= 2:
            j = 0.00
            for i in tempList:
                print i.strip()
                j = j + float(i.strip().split()[-1])
                
            print j / len(tempList)
            print tempList[0].strip().split('\t')[0],':',tempList[0].strip().split('\t')[2],'-',tempList[-1].strip().split('\t')[3]
            tempList = []
            tempList.append(line.strip())
            print '====================='
        else:
            tempList = []
            tempList.append(line.strip())
            

    prevStop = stop
    prevChr = chr
    prevStrand = strand
    #print chr,strand,start,stop
