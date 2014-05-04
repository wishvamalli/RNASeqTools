# a typical input 241-237:sandbox wishvaherath$ python peakcall.py chr1 - chr1_negative.wig 5 40

import os
import sys
sampleFolder = sys.argv[1]
resultsFolder = sys.argv[2]
gapFile = sys.argv[3]
minThreshHold = sys.argv[4]
minPeakSize = sys.argv[5]


print sampleFolder, resultsFolder, gapFile, minThreshHold, minPeakSize

#for human
c = range(1,23)
c.append('X')
c.append('Y')

#for zebrafish
#c = range(1,26)

for i in c:
    command =  'python scripts/peakcall_working.py chr'+str(i)+' + '+ sampleFolder +'/chr'+str(i)+'.pos.wig '+minThreshHold+ ' ' + minPeakSize +' '+  gapFile+ ' > '+resultsFolder+ '/CNTR_chr'+str(i)+'+'+minThreshHold + '_'+minPeakSize+'.txt'
    command = 'bsub ' + ' \" ' + command + ' \" '
    #print command
    os.system(command)
    command =  'python scripts/peakcall_working.py chr'+str(i)+' - '+ sampleFolder+ '/chr'+str(i)+'.neg.wig '+minThreshHold+ ' ' + minPeakSize +' '+   gapFile +' > ' +resultsFolder+'/CNTR_chr'+str(i)+'-'+minThreshHold + '_'+minPeakSize+'.txt'

    #print command
    command = 'bsub ' + ' \" ' + command + ' \" '
    os.system(command)
    
