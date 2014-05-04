import sys
NTRFile = sys.argv[1]
geneFootPrintFile = sys.argv[2]
n = int(sys.argv[3])
#addint the NTRfile to a dictionary...
dic = {}
for line in open(NTRFile,'r'):
    temp = line.strip().split('\t')
    tID = temp[0]+temp[1]+temp[2]+temp[3]
    #print temp[4],temp[12],temp[13],temp[14],temp[15]
    dic[tID] = line.strip()

for line in open(geneFootPrintFile,'r'):
    temp = line.strip().split('\t')
    print line
    #print temp[0],temp[1],temp[2],temp[3],temp[4]
    geneID  =temp[0].strip()
    chr = temp[1].strip()
    start = int(temp[2])
    stop = int(temp[3])
    strand = temp[4].strip()

    setGene = set(range(start,stop))
    setGeneExtended = set(range(start-n,stop+n))

    for ntr in dic:
        t = dic[ntr].strip().split('\t')
        nchr = t[0].strip()
        nstrand = t[1].strip()
        if nchr == chr and nstrand == strand :
            nstart = int(t[2])
            nstop = int(t[3])
            setNTR = set(range(nstart,nstop))

            L1 = len(setGene & setNTR)
            L2 = len(setGeneExtended & setNTR)

            if L1 == len(setNTR) or L2 == len(setNTR):
                'L3','\t',line.strip(),'\t',dic[ntr].strip()
            else:
                if L1> 0:
                    print 'L1','\t',line,'\t',dic[ntr],'\t',L1
                #print geneID,chr,start,stop,strand,nchr,nstrand,nstart,nstop,'L1',L1
                if L2 > 0:
                    print 'L2','\t',line.strip(),'\t',dic[ntr].strip(),'\t',L2
                
                #print geneID,chr,start,stop,strand,nchr,nstrand,nstart,nstop,'L2',L2

    
