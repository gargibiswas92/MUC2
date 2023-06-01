#!/usr/bin/python
import sys

inp1 = sys.argv[1]
out1 = sys.argv[3]

infile1 = open(inp1, 'r')

inp2 = sys.argv[2]

infile2 = open(inp2, "r")

#out1 = 'BEAD1.gro'

outfile1 = open(out1, "w")
count_line = 0
line_num = []

infile1 = open(inp1, "r")

for lines in infile1:
    outfile1.writelines(lines)
infile1.close()

for lines2 in infile2:
    outfile1.writelines(lines2)

infile1.close()
infile2.close()
outfile1.close()
