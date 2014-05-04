import sys

for line in open(sys.argv[1],'r'):
    temp = line.strip().split()

    #print temp
    geneID = temp[0].strip()
    d0 = float(temp[1].strip())
    d2 = float(temp[2].strip())
    d4 = float(temp[3].strip())
    d6 = float(temp[4].strip())
    d8 = float(temp[5].strip())
    if d0 > d2 > d4 > d6 > d8:
        print line.strip()
