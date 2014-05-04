#find repeatmasker regions in gaps
import sys

chr = sys.argv[3]
strand = sys.argv[4]

repeatFile = sys.argv[1]
gapFile = sys.argv[2]

repeatList = []
gapList = []

for line in open(repeatFile,'r'):
    temp = line.strip().split('\t')
    if temp[0].strip() == chr and temp[3].strip() == strand:
        repeatList.append(line.strip())


for line in open(gapFile,'r'):
    temp = line.strip().split('\t')
    if temp[0].strip() == chr and temp[3].strip() == strand:
        gapList.append(line.strip())

for repeat in repeatList:
    repeatStart = int(repeat.strip().split('\t')[1])
    repeatStop = int(repeat.strip().split('\t')[2])

    for gap in gapList:
        gapStart = int(gap.strip().split('\t')[1])
        gapStop = int(gap.strip().split('\t')[2])
        if repeatStart >= gapStart and repeatStop <= gapStop:
            print repeat.strip(),gap.strip()
            break
