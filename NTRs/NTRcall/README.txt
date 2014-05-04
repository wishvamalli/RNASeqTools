A SERIES OF PYTHON SCRIPTS FOR THE IDENTIFICATION OF NOVEL TRANSCRIBED REGIONS (NTRs) FROM AN RNA-SEQ DATASET.	

DOCUMENTATION.

Code and documentation written by Wishva Herath, Robson Lab, Genome Institute of Singapore. <wishvabh99@gis.a-star.edu.sg>

Requirements:
Software:
	python intepreter
	The scripts gaps.py, peakcall_iterate_bsub.py (for using bsub) or peakcall_iterate.py,		peakcall_working.py.
	unix server which supports bsub (optional)

Data:
	A folder containing all the wig files for each chromosome-strand pair.
	There should be no header in the wig files.
	The naming convention should be as follows... chr<#>.<pos/neg>.wig
	eg. chr1.pos.wig
	
	The default counts file containing refSeq counts from the ABI bioscope output.
	(one can modify the code so that the scripts work on other annotation files.)
	
Output:
	The final output will be a folder containing identified NTRs.
	There will be a seperate file for NTRs for all chromosome / strand combinations.
	The NTR files will be tab delimited and will have the following columns describing the identified NTR peak.
	[<chromosome><strand><start><stop><min height><max height><length><ucsc notation><total area>


Process:
	The NTR identification process includes the following steps...
	1)Processing the counts file
	2)Creating a gap file from the counts file.
	3)Identification of NTRs.


1)Processing the counts file.
The biosocpe counts file shows counts for each exon / cds / start codon of refSeq.
First remove CDS and start_codon counts.
Then sort the counts file in the following order 
     i)chromosome ASC
     ii)strand ASC
     iii)start position ASC
Name the counts file as [sampleID].exons.sorted.txt, and use it for the next step.


2)Creating a gap file from the counts file.
while in the pySEQ_for_bioscope folder type...
python scripts/gaps.py [counts file] > [gapfile.txt]

Recommended gapfile name - [sampleID].exon.gap.txt

3)Identification of NTRs.
Once the above script is run type...
python scripts/peakcall_iterate_bsub.py [wiggle file folder] [resuls folder] [gap file] [minthreshhold] [min peak size]

If all goes well the NTRs will be generate in less than 10mins.