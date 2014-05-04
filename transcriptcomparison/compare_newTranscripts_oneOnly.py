#compares new transcripts

import sys
check = 0
for line in open(sys.argv[1],'r'):
    temp = line.strip().split()
    #print temp
    oneChr = temp[1].strip()
    oneStart = int(temp[3].strip())
    oneStop = int(temp[5].strip())
    one = set(range(oneStart,oneStop))
    check = 0
    for line2 in open(sys.argv[2],'r'):
        temp2 = line2.strip().split()
        twoChr = temp2[1].strip()
        twoStart = int(temp2[3].strip())
        twoStop = int(temp2[5].strip())
        if oneChr == twoChr:
            two = set(range(twoStart,twoStop))

            if len(one & two) > 0:
                check = 1
    if check == 0:
        print line.strip()
