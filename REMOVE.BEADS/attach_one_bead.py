import math
from sympy.solvers import solve
from sympy import symbols
import numpy as np
import sys

def read_grofile(infile1):
    res = []
    xprot = []
    yprot = []
    zprot = []
    count_line = 0

    for lines in infile1:
        a = lines[0:5]
        b = lines[5:8]
        c = lines[20:28]
        d = lines[28:36]
        e = lines[36:44]
        res.append(int(a))
        xprot.append(float(c))
        yprot.append(float(d))
        zprot.append(float(e))
        
        res_num = np.array(res)
        x_cord_prot = np.array(xprot)
        y_cord_prot = np.array(yprot)
        z_cord_prot = np.array(zprot)
        count_line = count_line + 1
    return res_num, x_cord_prot, y_cord_prot, z_cord_prot

def read_sites(infile2):
    res_s = []
    count_prot_s = 0
    for lines2 in infile2:
        res_s.append(int(lines2))
        res_prot_s = np.array(res_s)
        count_prot_s = count_prot_s + 1
    return count_prot_s, res_prot_s

def read_coordinates(num, res_num, x_cord_prot, y_cord_prot, z_cord_prot):
    for i in range(len(res_num)):
        if res_num[i] == num:
            x = x_cord_prot[i]
            y = y_cord_prot[i]
            z = z_cord_prot[i]
    return x, y, z

def calc_dist(x1, y1, z1, x2, y2, z2):
    dd = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return dd

def solve_coordinates(x2, y2, z2, x3, y3, z3, x33, y33, z33, inp3, inp4, inp5):
    nan_c = 0
    x,y,z = symbols('x, y, z', real=True)
    vec1 = math.sqrt(((x2 - x3)*(x2 - x3)) + ((y2 - y3)*(y2 - y3)) + ((z2 - z3)*(z2 - z3)))
    vec2 = math.sqrt(((x2 - x33)*(x2 - x33)) + ((y2 - y33)*(y2 - y33)) + ((z2 - z33)*(z2 - z33)))
            
    mult1 = vec1*math.cos((inp3*math.pi)/180)*inp5
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
        solv_z = str(sol1)
            
        if ('I' in solv_z) == False:
            y = y2 + mult4 - par3*float(sol1)
            x = x2 + mult5 + par4*float(sol1)
            x_s1 = float(x)
            y_s1 = float(y)
            z_s1 = float(sol1)
            #print(y, x, solved_z)
            #s1 = float(x)
            #s2 = float(y)
            #s3 = float(solved_z)
        else:
            x_s1 = 5000
            y_s1 = 5000
            z_s1 = 5000
        
    return x_s1, y_s1, z_s1
         
    
def calc_prot_clashes(num, s1, s2, s3, x_cord_prot, y_cord_prot, z_cord_prot):
    flag = 0      
    for m in range(len(x_cord_prot)):
        if m != num and m != (num+1) and m != (num-1) and m != (num+2) and m != (num-2) and m != (num+3) and m != (num-3) and m != (num+4) and m != (num-4):
           xp1, yp1, zp1 = read_coordinates(num, res_num, x_cord_prot, y_cord_prot, z_cord_prot)
           
           xp2 = s1
           yp2 = s2
           zp2 = s3
           p_to_resd = calc_dist(xp1, yp1, zp1, xp2, yp2, zp2)
           
           if p_to_resd <= 0.6:
              flag = 1
              break
           else:
              continue
    return flag

#x2, y2, z2 = read_coordinates(39733, res_num, x_cord_prot, y_cord_prot, z_cord_prot)
#print(x2, y2, z2)          
#inp1 = sys.argv[1]
#inp2 = sys.argv[2]
#inp3 = float(sys.argv[3])
#inp4 = float(sys.argv[4])
#inp5 = float(sys.argv[5])

#infile1 = open(inp1, 'r')
#infile2 = open(inp2, 'r')

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

infile1 = open('INIT.CONF.gro', 'r')
infile2 = open('GLYCAN.PCT.txt', 'r')
inp3 = 62.0
inp4 = 88.0
inp5 = 0.37
    
res_num, x_cord_prot, y_cord_prot, z_cord_prot = read_grofile(infile1)
count_prot_s, res_prot_s = read_sites(infile2)

x_sol = []
y_sol = []
z_sol = []

x_sol1 = []
y_sol1 = []
z_sol1 = []

prot_res = []

for k in range(count_prot_s):

    num = res_prot_s[k]
    x2, y2, z2 = read_coordinates(num, res_num, x_cord_prot, y_cord_prot, z_cord_prot)
    x3, y3, z3 = read_coordinates(num+1, res_num, x_cord_prot, y_cord_prot, z_cord_prot)
    x33, y33, z33 = read_coordinates(num-1, res_num, x_cord_prot, y_cord_prot, z_cord_prot)
    xs, ys, zs = solve_coordinates(x2, y2, z2, x3, y3, z3, x33, y33, z33, inp3, inp4, inp5)
    
    if xs != 5000 and ys !=5000 and zs !=5000:
        val = calc_prot_clashes(num, xs, ys, zs, x_cord_prot, y_cord_prot, z_cord_prot)
        if val == 0:
           x_sol.append(xs)
           y_sol.append(ys)
           z_sol.append(zs)
        flag1 = 0
        if len(x_sol) > 1:
            for m in range(len(x_sol)):
                x1 = x_sol[m]
                y1 = y_sol[m]
                z1 = z_sol[m]
        
                x2 = xs
                y2 = ys
                z2 = zs
            
                dis = calc_dist(x1, y1, z1, x2, y2, z2)
                if dis < 0.6:
                   flag1 = 1
                   break
                else:
                   continue
        if flag1 == 0:
            x_sol1.append(xs)
            y_sol1.append(ys)
            z_sol1.append(zs) 
            prot_res.append(num)

max_val = len(res_num)       
for i in range(len(prot_res)):
       ind = max_val + i
       x = x_sol1[i]
       y = y_sol1[i]
       z = z_sol1[i]
       prot_r = prot_res[i]
       ss = 'HETATM {:>5d}  C1 0VA {:>5d} {:>10.2f} {:>7.2f} {:>7.2f}{}'.format(ind, ind, x, y, z, "\n")
       ss2 = '{:>5d}0VA     C1{:>5d} {:>7.3f} {:>7.3f} {:>7.3f}{}'.format(ind, ind, x, y, z, "\n")
       ss3 = ' {:>5d}       NB_2  {:>5d}    0VA     C1  {:>5d}{}'.format(ind, ind, ind, "\n")
       ss4 = '{:>5d}   {:>5d}   1        3.778300432e-01 2.000000000e+04{}'.format(ind, prot_r, "\n")
       ss5 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        1.089800000e+03 1.000000000e+00 1{}'.format(ind, prot_r, (prot_r-1), (prot_r-2), "\n")
       ss6 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        3.269400000e+03 5.000000000e-01 3{}'.format(ind, prot_r, (prot_r-1), (prot_r-2), "\n")
           
       outfile1.writelines(ss)
       outfile2.writelines(ss2)
       outfile3.writelines(ss3)
       outfile4.writelines(ss4)
       outfile6.writelines(ss5)
       outfile6.writelines(ss6)
       
       
outfile1.close()
infile1.close()
infile2.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()