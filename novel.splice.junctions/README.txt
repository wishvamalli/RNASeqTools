Identification of novel exon exon junctions.


Objective: Using the SAM file to produce a list of novel exon exonjunctions.

Process:

1) filtering.
I start with the bam files (which is smaller than the sam file) and then use samtools to extract it into a SAM file and then do the filtering all in one line.

for example.... samtools view bam file |grep filter 1 | grep filter2 > resultsfile.txt

The filters are...
1) xMyNxM where x should be a min of 10 or more
2) IH flag should be one (mapps to only one place)
3) XJ:Z:P , putative exon exon junctions. I did not know this earlier so spent a week or so to manually identify this!!!

This step produces a sam file with the required filtering.

2) use SAMspliceToBed.py by Mikael to convert the SAM file into a bed file.

3) use bedfileannotate.py to annotate the bed file (put a gene name to the bed file)

The bed file annotate needs an exon annotation file

During the alignment process bioscope identifies reads which map to two known junctions and marks it with a flag.

In summary...
10MxN10M - reads which have atleast 10 full mappings on either of the exons
IH:1 reads which map only to one place of the genome
XJ:Z:P reads which map to novel junction reads
