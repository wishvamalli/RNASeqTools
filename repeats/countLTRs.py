# counts LTRs given a list of LTRs and a combined wig file

import sys

LTRFile = sys.argv[1]
wigFile = sys.argv[2]

# load the wigFile into a dictionary...

wig = {}
print 'dictionary loading'
for line in open(wigFile,'r'):
    temp = line.strip().split('\t')
    wig[temp[0].strip()+temp[1].strip()+temp[2].strip()]=int(temp[3].strip())

print 'dictionary loaded'
#print wig

for line in open(LTRFile,'r'):
    temp = line.strip().split()
    #print temp
    start = int(temp[1])
    stop = int(temp[2])
    chr = temp[0].strip()
    strand = temp[3].strip()
    tot = 0
    for i in range(start,stop+1):
        #print chr.strip()+strand.strip()+str(i).strip()
        if chr.strip()+strand.strip()+str(i).strip() in wig:
            tot = tot+ wig[chr.strip()+strand.strip()+str(i).strip()]

    if tot > 1:
        print line.strip(),'\t',tot
        
