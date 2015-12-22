# coding: utf-8
# -------------------------------------------------------------------
""" Make a bibtex file of my publications for CV """

__author__ = "Charlotte Mason <cmason@astro.ucla.edu>"

import time
import ads
# -------------------------------------------------------------------
# Keywords for finding me
name      = "Mason, C"
keywords  = "astro*"
startyear = 2013
outputbib = "my_pubs.bib"

# Look for papers 
papers = list(ads.SearchQuery(author=name, q=keywords, sort="pubdate"))

# Only select ones I could have published...
my_pubs = []
cittot  = 0
for p in papers:                                             
    if int(p.year) >= startyear:
    	my_pubs.append(p)
    	cittot = cittot + p.citation_count

print "Retrieved %i publications since %i, with a total of %i citations" % (len(my_pubs), startyear, cittot)

with open(outputbib, "w") as bib_file:
	now = time.strftime("%Y-%m-%d %H:%M")
	bib_file.write("My publications last retrieved from ADS at %s" % now)
	for p in my_pubs:
		try:
			bib_file.write("%s" % p.bibtex)
		except:
			print 'No bibtex entry found for',p
			pass

print "Bibtex file written to "+outputbib