infileName = 'references.bib'
outfileName = 'references_short.bib'
authorMax = 10

with open(infileName, 'r') as bibfile:
	biblines = bibfile.readlines()

outbib = open(outfileName,'w')

for line in biblines:
	if ("Author =" in line) or ("author =" in line):
		line_lowerand = line.replace("AND","and")
		line_vec = line_lowerand.split("and ")
		if len(line_vec) > authorMax:
			line_vec_update = line_vec[:authorMax]
			line_vec_update.append("others },\n")
		else:
			line_vec_update = line_vec
		line_update = "and ".join(line_vec_update)
	else:
		line_update = line
	outbib.write(line_update)

outbib.close()




