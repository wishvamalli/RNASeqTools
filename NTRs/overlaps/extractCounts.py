
#extractCounts.py

#wishvabh99@gis.a-star.edu.sg

#Function - This script calls on the filter.py script with all the combinations of chromosome-strand.
#make sure a folder called filtered exist.
#the source code for sep.py (hard coded ) should also be available at the given location.
import os
import sys
import shutil


try:
    inputFile = sys.argv[1] # this contains all the query co-ordinates
    
    chromPos = sys.argv[2]
    chromStartPos = sys.argv[3]
    chromEndPos = sys.argv[4]
    namePos = sys.argv[5]
    strandPos = sys.argv[6]
    filteredFolder = sys.argv[7]
except:
    print 'Incorrect parameters'
    print 'python extractCounts.py <inputFile> <positionString>'
    print 'positionString format -> chrom,chromStart,chromStop,name,strand'
    exit()
    
try:
    os.mkdir('filtered') # checking to see if the folder filtered exists, if not it will create it
except:
    shutil.rmtree('filtered') # the folder exists, so need to delete it and re-create it. (Note that the script uses filtered folder as a 'scratch')
    os.mkdir('filtered')
    
print 'Start.....'
print 'inputfile -> ', inputFile
print 'chr,start,stop,name,strand POSITIONS', chromPos, chromStartPos, chromEndPos, namePos, strandPos
#for human
list = range(1,23)
list.append('X')
list.append('Y')

#for zebrafish

#list = range(1,26)
for i in list:
    command = 'python scripts/filter.py '+ 'chr'+str(i)+ ' + ' + chromPos+ ' ' + strandPos   + ' '+ inputFile +  ' > '+ filteredFolder+'/chr'+str(i)+'_positive_filtered.txt'
    print command
    os.system(command)
    
    command = 'python scripts/filter.py '+ 'chr'+str(i)+ ' - ' + chromPos+ ' ' + strandPos  + ' '+ inputFile +   ' >'+ filteredFolder+'/chr'+str(i)+'_negative_filtered.txt'
    print command
    os.system(command)

print 'Filtering DONE'
    

    
