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
    if d0 == 0:
        print line.strip()
        
    else:
        pass
        #print geneID,'\t',d2/d0,'\t',d4/d0,'\t',d6/d0,'\t',d8/d0
