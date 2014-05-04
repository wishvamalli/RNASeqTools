import sys
list = []

for line in open(sys.argv[1],'r'):
    list.append(line.strip().split('\t')[13].strip())



for line in open(sys.argv[2],'r'):
    a = line.strip().split('\t')[7].strip()

    if  a in list:
        pass
    else:
        print line.strip()
