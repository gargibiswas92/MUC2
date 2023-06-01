import sys
import types
import math
import statistics
import numpy as np
from math import sqrt
from sympy.solvers import nonlinsolve
from sympy.solvers import solve
from sympy import symbols

inp1 = sys.argv[1]
inp2 = sys.argv[2]

dis1 = float(sys.argv[3])
ang1 = float(sys.argv[4])
ang2 = float(sys.argv[5])

#dis1 is the distance between new sugar and sugar 1 (sugar(i) and sugar(i-1))
#ang1 is the angle between sugar(i)-sugar(i-1)-prot(ii)
#ang2 is the angle between sugar(i)-prot(ii)-prot(ii-1)

infile1 = open(inp1, "r")
infile2 = open(inp2, "r")

out1 = sys.argv[6]
outfile1 = open(out1, "w")

prot_ind = []
sugar_ind = []
counta = 0

##Reading the bond information##
#******************************************************************
for lines2 in infile2:
    aa = lines2[0:5]
    bb = lines2[8:13]
    prot_ind.append(int(bb))
    sugar_ind.append(int(aa))
    counta = counta + 1
    
res_num = []
x_cord = []
y_cord = []
z_cord = []
x_cord_sug = []
y_cord_sug = []
z_cord_sug = []
count_line = 0
prot_dis = []
sug_dis = []
sug_count = 0

##Reading the structure##
#******************************************************************

for lines in infile1:
    a = lines[0:5]
    b = lines[5:8]
    c = lines[20:28]
    d = lines[28:36]
    e = lines[36:44]
    res_num.append(int(a))
    x_cord.append(float(c))
    y_cord.append(float(d))
    z_cord.append(float(e))
    count_line = count_line + 1
    
##Function defination##
#******************************************************************

def read_cordinates(m):
    for i in range(count_line):
        if res_num[i] == m:
            xx = x_cord[i]
            yy = y_cord[i]
            zz = z_cord[i]
    return xx, yy, zz

def calc_dist(x1, y1, z1, x2, y2, z2):
    dd = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return dd

##New co-ordinate generation##
#******************************************************************

countp = 0
for j in range(counta):
    qq = prot_ind[j]
    rr = sugar_ind[j]
    pp = qq - 1

    x1, y1, z1 = read_cordinates(rr)
    x2, y2, z2 = read_cordinates(qq)
    x3, y3, z3 = read_cordinates(pp)

    #ang1 = 69.205 
    #ang2 = 86.189
    #dis1 = 0.59
    
    #ang1 = 60.205 
    #ang2 = 80.189
    #dis1 = 0.698
    
    x,y,z = symbols('x, y, z', real=True)
    ang11 = math.cos((ang1*math.pi)/180)
    ang22 = math.cos((ang2*math.pi)/180)
    
    vec1 = math.sqrt(((x1 - x2)*(x1 - x2)) + ((y1 - y2)*(y1 - y2)) + ((z1 - z2)*(z1 - z2)))
    vec2 = math.sqrt(((x3 - x2)*(x3 - x2)) + ((y3 - y2)*(y3 - y2)) + ((z3 - z2)*(z3 - z2)))
    
    mult1 = vec1*ang11*(dis1)
    mult2 = vec2*ang22*(dis1)
    
    par2 = ((x3 - x2)*(y1 - y2)) - ((x1 - x2)*(y3 - y2))
    par1 = ((x3 - x2)*(z1 - z2)) - ((x1 - x2)*(z3 - z2))
    mult3 = (mult1*(x3 - x2)) - (mult2*(x1 - x2))  
    
    if ((par2) != 0) and (x3 - x2)!= 0:
        par3 = par1/par2
        mult4 = (mult3/par2) + (z2*par1)/par2 
            
        mult5 = (mult2 - (mult4*(y3 - y2)) + (z2*(z3 - z2)))/(x3 - x2)
        par4 = ((par3*(y3 - y2)) - (z3 - z2))/(x3 - x2)
            
        eq11 = (mult5 + (z*par4))**2 + (mult4 - (z*par3))**2 + (z - z2)**2 - (dis1)**2
        sol1, sol2 = solve(eq11, check=False)
            
        solved_z = str(sol1)
            
        if '*' in solved_z:
            z_sol = 60000
        else:
            z_sol = float(solved_z)
            countp = countp +1
            ll = count_line + countp
                
        if z_sol != 60000:
            x_sol = x2 + mult5 + par4*z_sol
            y_sol = y2 + mult4 - par3*z_sol
            print(ll, rr, qq, x_sol, y_sol, z_sol)
            ssd = '{:>7d}{:>7d}{:>7d}{:>12.3f}{:>12.3f}{:>12.3f}{}'.format(ll, rr, qq, x_sol, y_sol, z_sol, "\n")
            outfile1.writelines(ssd)
infile1.close()
infile2.close()
outfile1.close()
