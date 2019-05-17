#!/usr/bin/env python

'''
A fun skim-through of my thesis to answer @yosoykit's question: https://twitter.com/yosoykit/status/996870912963117056

@Author: Eszter Lakatos
'''
import glob

#Define the list of tex expressions to be counted, use \\ to escape regular expressions
expressions = ['\\frac', "\\cdot", '\\rightarrow', '\\ref', '\\text{', '\\mathbf', "\\left", '\\right', '\\sim', '\\mu', '\\dot', '\\begin{bmatrix}', '\\sigma', '\\mathbb', '\\alpha', '\\beta', '\\int', '=']

# Define directory of tex files (give absolute path) and query all texfiles from it
texDirectory = '/Users/el613/Documents/Writeup/Thesis'
texFiles = glob.glob(texDirectory+'/*.tex')

exprDict = {expr : 0 for expr in expressions }

# For each texfile, count the number of expressions and update dictionary
for i in range(len(texFiles)):
	with open(texFiles[i], 'r') as infile:
		lines = infile.readlines()

	for line in lines:
		for expr in expressions:
			exprDict[expr] +=line.count(expr)

print('Number of occurrences for each expression:')
for k in expressions:
	print(k+': '+str(exprDict[k]))



