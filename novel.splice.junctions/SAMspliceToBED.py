""" SAMspliceToBED.py : Identifies splice junctions from a sam file """
__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "Copyright 2012"
__status__ = "Prototype"
__version__ = "0.0.1"
__license__ = "GPL"
import sys, re

iF = open(sys.argv[1])

p = re.compile('[0-9]+M[0-9]+N[0-9]+M')

hits = {}
for line in iF:
	c=line.split()
	chr = c[2]
	start = int(c[3])	
	try:
		m = p.search(line)
		cig = m.group().split()[0]
	except:
		continue

	z = cig.split("M")
	first_match = int(z[0])
	gap_and_sec = z[1]
	gap = int(z[1].split("N")[0])
	second_match = int(z[1].split("N")[1].split("M")[0])	
	jcn_left = start + first_match
	jcn_right = start + first_match + gap

	bed_str = chr + "\t" + str(jcn_left) + "\t" + str(jcn_right)

	if hits.has_key(bed_str):
		hits[bed_str]+=1
	else:	
		hits[bed_str]=1

for k in hits.keys():
	print k, hits[k]
