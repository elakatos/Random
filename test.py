expressions = ['\\frac', "\\cdot", '\\rightarrow', '\\ref', '\\text{', '\\mathbf', "\\left", '\\right', '\\sim', '\\mu', '\\dot', '\\begin{bmatrix}', '\\sigma', '\\mathbb', '\\alpha', '\\beta', '\\int', '=']

texDirectory = '/Users/el613/Documents/Writeup/Thesis'
texFiles = ['chapter_background.tex', 'chapter_mcmea.tex', 'chapter_p53abc.tex', 'chapter_landscape.tex', 'chapter_reachability.tex', 'appendixA.tex', 'appendixB.tex', 'appendixC.tex']

exprDict = {expr : 0 for expr in expressions }

for i in range(len(texFiles)):
	with open(texDirectory+'/'+texFiles[i], 'r') as infile:
		lines = infile.readlines()

	for line in lines:
		for expr in expressions:
			exprDict[expr] +=line.count(expr)

print('Number of occurrences for each expression:')
for k in expressions:
	print(k+': '+str(exprDict[k]))



