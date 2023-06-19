#!/usr/bin/python
import sys

inp1 = sys.argv[1]
inp2 = sys.argv[2]
inp3 = sys.argv[3]
inp4 = sys.argv[4]
out1 = sys.argv[5]


infile1 = open(inp1, "r")

infile2 = open(inp2, "r")

infile3 = open(inp3, "r")

infile4 = open(inp4, 'r')

#out1 = 'BEAD1.top'

outfile1 = open(out1, "w")

count_line = 0
for lines in infile1:
    count_line = count_line + 1
    if "bonds" in lines:
       bond_line = count_line
    if "dihedrals" in lines:
       dihedral_line = count_line
    if "system" in lines:
       sys_line = count_line
print(sys_line)

infile1.close()
infile1 = open(inp1, "r")
count_line_w = 0
for lines_w in infile1:
    count_line_w = count_line_w + 1
    if count_line_w <= bond_line-2:
       outfile1.writelines(lines_w)
infile1.close()

for lines2 in infile2:
    outfile1.writelines(lines2)
infile2.close()

infile1 = open(inp1, "r")
count_line_w = 0
for lines_w in infile1:
    count_line_w = count_line_w + 1
    if count_line_w >= bond_line-1 and count_line_w <= dihedral_line-2:
       outfile1.writelines(lines_w)
infile1.close()

for lines3 in infile3:
    outfile1.writelines(lines3)
infile3.close()

infile1 = open(inp1, "r")
count_line_w = 0
for lines_w in infile1:
    count_line_w = count_line_w + 1
    if count_line_w >= dihedral_line-2 and count_line_w <= sys_line-2:
       outfile1.writelines(lines_w)
infile1.close()

for lines4 in infile4:
    outfile1.writelines(lines4)
infile4.close()

infile1 = open(inp1, "r")
count_line_w = 0
for lines_w in infile1:
    count_line_w = count_line_w + 1
    if count_line_w >= sys_line-2:
       outfile1.writelines(lines_w)
infile1.close()
outfile1.close()
