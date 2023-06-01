#!/usr/bin/python
#****************************************
#creats output files and opens input file
#******************************************
import sys
import types
import math
import numpy as np
from math import sqrt
from sympy.solvers import nonlinsolve
from sympy.solvers import solve
from sympy import symbols

#inp1 = input('Insert the name of the initial .gro file:')
#inp2 = input('Insert the name of the glycan index file:')

inp1 = sys.argv[1]
inp2 = sys.argv[2]
inp3 = float(sys.argv[3])
inp4 = float(sys.argv[4])
inp5 = float(sys.argv[5])

infile1 = open(inp1, 'r')
infile2 = open(inp2, 'r')

#in1 = inp2.strip('.PCT.txt')

out1 = 'COORD.txt'
out2 = 'GRO.txt'
out3 = 'DEF.txt'
out4 = 'BOND.txt'
out5 = 'ABAN.txt'
out6 = 'DIHED.txt'

outfile1 = open(out1, 'w')
outfile2 = open(out2, 'w')
outfile3 = open(out3, 'w')
outfile4 = open(out4, 'w')
outfile5 = open(out5, 'w')
outfile6 = open(out6, 'w')


#**************************************************
#Reads the co-ordinates from the .gro file (input)
#**************************************************
res_num = []
x_cord_prot = []
y_cord_prot = []
z_cord_prot = []
x_cord_sug = []
y_cord_sug = []
z_cord_sug = []
count_line = 0
prot_dis = []
sug_dis = []

for lines in infile1:
    a = lines[0:5]
    b = lines[5:8]
    c = lines[20:28]
    d = lines[28:36]
    e = lines[36:44]
    res_num.append(int(a))
    x_cord_prot.append(float(c))
    y_cord_prot.append(float(d))
    z_cord_prot.append(float(e))
    count_line = count_line + 1
    
res_prot_s = []
count_prot_s = 0
sug_count = 0
nan_count = 0
res_nan = []

#*************************************************************
#Reads the glycan indeces from the other file
#*************************************************************

for lines2 in infile2:
    res_prot_s.append(int(lines2))
    count_prot_s = count_prot_s + 1
    
#print(count_line, count_prot_s)
x,y,z = symbols('x, y, z', real=True)

#**************************************************************
#distances calculation subroutine
#**************************************************************

def calc_dist(x1, y1, z1, x2, y2, z2):
    dd = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return dd
#****************************************************************
#solution of three equation where one distance and two angles are
#known, this way x, y, z co-ordinates of any sugar residue was 
#solved
#****************************************************************
    
for i in range(count_prot_s):
    for j in range(count_line):
        if res_prot_s[i] == res_num[j] and res_prot_s[i] <= 40391 and res_prot_s[i] >= 16884:
            bonded_res = res_prot_s[i]
            x2 = x_cord_prot[j]
            y2 = y_cord_prot[j]
            z2 = z_cord_prot[j]
            x3 = x_cord_prot[j+1]
            y3 = y_cord_prot[j+1]
            z3 = z_cord_prot[j+1]
            x33 = x_cord_prot[j-1]
            y33 = y_cord_prot[j-1]
            z33 = z_cord_prot[j-1]
            vec1 = math.sqrt(((x2 - x3)*(x2 - x3)) + ((y2 - y3)*(y2 - y3)) + ((z2 - z3)*(z2 - z3)))
            vec2 = math.sqrt(((x2 - x33)*(x2 - x33)) + ((y2 - y33)*(y2 - y33)) + ((z2 - z33)*(z2 - z33)))
            #mult1 = vec1*math.cos((62.8155*math.pi)/180)*0.37783
            mult1 = vec1*math.cos((inp3*math.pi)/180)*inp5
          
            #mult2 = vec2*math.cos((88.0857*math.pi)/180)*0.37783
            mult2 = vec2*math.cos((inp4*math.pi)/180)*inp5
            
            par1 = ((y2 - y3)*(x2 - x33)) - ((y2 - y33)*(x2 - x3))
            par2 = ((z2 - z3)*(x2 - x33)) - ((z2 - z33)*(x2 - x3))
            mult3 = (mult1*(x2 - x33)) - (mult2*(x2 - x3))  

            if ((par1) != 0) and (x2 - x3)!= 0:
            
                par3 = par2/par1
                mult4 = (mult3/par1) + (z2*par2)/par1
        
                mult5 = (mult1 - (mult4*(y2 - y3)) + (z2*(z2 - z3)))/(x2 - x3)
                par4 = ((par3*(y2 - y3)) - (z2 - z3))/(x2 - x3)
                eq11 = (mult5 + (z*par4))**2 + (mult4 - (z*par3))**2 + (z - z2)**2 - (inp5)**2
                sol1, sol2 = solve(eq11, check=False)
                solved_z = str(sol1)
            
                if ('I' in solved_z) == False:
                    y = y2 + mult4 - par3*float(solved_z)
                    x = x2 + mult5 + par4*float(solved_z)
                    print(y, x, solved_z)
                    s1 = float(x)
                    s2 = float(y)
                    s3 = float(solved_z)
                
                else:
                    continue
                    print("no solutions can be obtained")
                    nan_count = nan_count + 1
                    ss5 = '{:>5s} {:>5s}{}'.format(str(nan_count), str(res_prot_s[i]), "\n")
                    outfile5.writelines(ss5)
             
            else:
                continue
                print("no solutions can be obtained")
                nan_count = nan_count + 1
                res_nan.append(res_num[j])
                ss5 = '{:>5s} {:>5s}{}'.format(str(nan_count), str(res_prot_s[i]), "\n")
                outfile5.writelines(ss5)
        else:
            continue
#***********************************************************************
#checks whether the newly calculated co-ordinates makes any clashes with
#any protein residues
#***********************************************************************
 
    flag = 0      
    k = int(i) + 40393
    for m in range(40392):
        if m != bonded_res and m != (bonded_res+1) and m != (bonded_res-1) and m != (bonded_res+2) and m != (bonded_res-2) and m != (bonded_res+3) and m != (bonded_res-3) and m != (bonded_res+4) and m != (bonded_res-4):
           xp1 = x_cord_prot[m]
           yp1 = y_cord_prot[m]
           zp1 = z_cord_prot[m]
           xp2 = s1
           yp2 = s2
           zp2 = s3
           p_to_resd = calc_dist(xp1, yp1, zp1, xp2, yp2, zp2)
           if p_to_resd <= 1.0:
              flag = 1
              break
           else:
              continue
#*****************************************************************************
#checks whether the newly calculated co-ordinates make any clashes with any of
#the other sugar residues
#*****************************************************************************
    
    if len(x_cord_sug) > 1:
       for n in range(len(x_cord_sug)):
           xs1 = x_cord_sug[n]
           ys1 = x_cord_sug[n]
           zs1 = z_cord_sug[n]
           xs2 = s1
           ys2 = s2
           zs2 = s3
           s_to_resd = calc_dist(xs1, ys1, zs1, xs2, ys2, zs2)
           if s_to_resd <= 1.2:
              flag = 1
              break
           else:
              continue        
#*******************************************************************************
#writes the co-ordinates, other topology informations in the output files
#*******************************************************************************

    if flag == 0:    
       x_cord_sug.append(s1)
       y_cord_sug.append(s2)
       z_cord_sug.append(s3)
       #sug_count = sug_count + 1
       kk = 40392 + len(x_cord_sug)
       ss = 'HETATM {:>5s}  C1 0VA {:>5s} {:>10.2f} {:>7.2f} {:>7.2f}{}'.format(str(kk), str(kk), s1, s2, s3, "\n")
       ss2 = '{:>5d}0VA     C1{:>5d} {:>7.3f} {:>7.3f} {:>7.3f}{}'.format(kk, kk, s1, s2, s3, "\n")
       ss3 = ' {:>5s}       NB_2  {:>5s}    0VA     C1  {:>5s}{}'.format(str(kk), str(kk), str(kk), "\n")
       ss4 = '{:>5s}   {:>5s}   1        3.778300432e-01 2.000000000e+04{}'.format(str(kk), str(res_prot_s[i]), "\n")
       ss5 = '{:>5s}   {:>5s}   {:>5s}   {:>5s}   1        1.089800000e+03 1.000000000e+00 1{}'.format(str(kk), str(res_prot_s[i]), str(res_prot_s[i]-1), str(res_prot_s[i]-2), "\n")
       ss6 = '{:>5s}   {:>5s}   {:>5s}   {:>5s}   1        3.269400000e+03 5.000000000e-01 3{}'.format(str(kk), str(res_prot_s[i]), str(res_prot_s[i]-1), str(res_prot_s[i]-2), "\n")

       outfile1.writelines(ss)
       outfile2.writelines(ss2)
       outfile3.writelines(ss3)
       outfile4.writelines(ss4)
       outfile6.writelines(ss5)
       outfile6.writelines(ss6)
    else:
       continue
                
outfile1.close()
infile1.close()
infile2.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()
