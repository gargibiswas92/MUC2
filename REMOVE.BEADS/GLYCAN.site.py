#!/usr/bin/python

import sys
import math
from math import sqrt
from sympy.solvers import nonlinsolve
from sympy.solvers import solve
from sympy import symbols
import random

#inp1 = input("Insert the name of the initial .gro file:")

inp1 = sys.argv[1]

infile1 = open(inp1, 'r')

#inp2 = input("Insert the degree of glycosylation in percentage:")

inp2 = sys.argv[2]

out1 = 'GLYCAN.PCT.txt'
out2 = 'GLYCAN.IND.txt'

outfile1 = open(out1, 'w')
outfile2 = open(out2, 'w')

res_num = []
count_line = 0
res_name = []

deg = float(int(inp2)/100)

for lines in infile1:
    a1 = int(lines[0:5])
    a2 = str(lines[5:8])
    res_num.append(a1)
    res_name.append(a2)
    count_line = count_line + 1
    
count_gly_site = 0
gly_site = []

for i in range(count_line):
    if res_num[i] >= 16884:
       if res_name[i] == 'SER' or res_name[i] == 'THR':
          #print(res_num[i])
          gly_site.append(res_num[i])
          count_gly_site = count_gly_site + 1
#print(count_gly_site)

perc = count_gly_site*deg
perc_int = int(perc)
#print(perc)

li2 = random.sample(gly_site,perc_int)
#print(li2)
 
for i in range(len(li2)):
    ss1 = [str(li2[i]), "\n"]
    ss2 = [str(i), " ",str(li2[i]), "\n"]
    outfile1.writelines(ss1)      
    outfile2.writelines(ss2)      
