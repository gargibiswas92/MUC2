
import math
from sympy.solvers import solve
from sympy import symbols
import numpy as np
import sys

inp1 = sys.argv[1]
inp2 = sys.argv[2]

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

def read_coordinates(num, x_cord_prot, y_cord_prot, z_cord_prot):
    x = x_cord_prot[num-1]
    y = y_cord_prot[num-1]
    z = z_cord_prot[num-1]
    return x, y, z

def calc_dist(x1, y1, z1, x2, y2, z2):
    dd = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return dd

def solve_coordinates(x2, y2, z2, x3, y3, z3, x33, y33, z33, inp3, inp4, inp5):
    nan_c = 0

    x_s1 = 5000
    y_s1 = 5000
    z_s1 = 5000

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
        #solv_z = str(sol1)
            
        if type(sol1) == float:
            y = y2 + mult4 - par3*float(sol1)
            x = x2 + mult5 + par4*float(sol1)
            x_s1 = float(x)
            y_s1 = float(y)
            z_s1 = float(sol1)
        
    return x_s1, y_s1, z_s1

def check_real(list, def_val):
    flag = 0
    for item in list:
        if item == def_val:
            flag = 1
            break
        else:
            continue
    return flag 
         
    
def calc_prot_clashes(num, s1, s2, s3, x_cord_prot, y_cord_prot, z_cord_prot, min_dis):
    flag = 0      
    for m in range(len(x_cord_prot)):
        if m != num and m != (num+1) and m != (num-1) and m != (num+2) and m != (num-2) and m != (num+3) and m != (num-3) and m != (num+4) and m != (num-4):
           xp1, yp1, zp1 = read_coordinates(num, x_cord_prot, y_cord_prot, z_cord_prot)
           
           xp2 = s1
           yp2 = s2
           zp2 = s3
           p_to_resd = calc_dist(xp1, yp1, zp1, xp2, yp2, zp2)
           
           if p_to_resd <= min_dis:
              flag = 1
              break
           else:
              continue
    return flag

def append_coord(xm, ym, zm, xlist, ylist, zlist):
    xlist.append(xm)
    ylist.append(ym)
    zlist.append(zm)
    return xlist, ylist, zlist

def calc_sugar_clashes(x_sol, y_sol, z_sol, xs, ys, zs, min_dis):
    flg = 0
    for l in range(len(x_sol)):
        x1 = x_sol[l]
        y1 = y_sol[l]
        z1 = z_sol[l]
        
        dis = calc_dist(x1, y1, z1, xs, ys, zs)
        
        if dis <= min_dis:
              flg = 1
              break
        else:
              continue
    return flg

def write_output(outfile1, outfile2, outfile3, outfile4, outfile5, outfile6, ind, bonded, dih1, dih2, x, y, z):
    ss = 'HETATM {:>5d}  C1 0VA {:>5d} {:>10.2f} {:>7.2f} {:>7.2f}{}'.format(ind, ind, x, y, z, "\n")
    ss2 = '{:>5d}0VA     C1{:>5d} {:>7.3f} {:>7.3f} {:>7.3f}{}'.format(ind, ind, x, y, z, "\n")
    ss3 = ' {:>5d}       NB_2  {:>5d}    0VA     C1  {:>5d}{}'.format(ind, ind, ind, "\n")
    ss4 = '{:>5d}   {:>5d}   1        3.778300432e-01 2.000000000e+04{}'.format(ind, bonded, "\n")
    ss5 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        1.089800000e+03 1.000000000e+00 1{}'.format(ind, bonded, dih1, dih2, "\n")
    ss6 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        3.269400000e+03 5.000000000e-01 3{}'.format(ind, bonded, dih1, dih2, "\n")
           
    outfile1.writelines(ss)
    outfile2.writelines(ss2)
    outfile3.writelines(ss3)
    outfile4.writelines(ss4)
    outfile6.writelines(ss5)
    outfile6.writelines(ss6)
    
    
def write_output2(outfile1, outfile2, outfile3, outfile4, outfile5, outfile6, ind, bonded, dih1, dih2, x, y, z):
    ss = 'HETATM {:>5d}  C1 0VB {:>5d} {:>10.2f} {:>7.2f} {:>7.2f}{}'.format(ind, ind, x, y, z, "\n")
    ss2 = '{:>5d}0VB     C1{:>5d} {:>7.3f} {:>7.3f} {:>7.3f}{}'.format(ind, ind, x, y, z, "\n")
    ss3 = ' {:>5d}       NB_3  {:>5d}    0VB     C1  {:>5d}{}'.format(ind, ind, ind, "\n")
    ss4 = '{:>5d}   {:>5d}   1        3.778300432e-01 2.000000000e+04{}'.format(ind, bonded, "\n")
    ss5 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        1.089800000e+03 1.000000000e+00 1{}'.format(ind, bonded, dih1, dih2, "\n")
    ss6 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        3.269400000e+03 5.000000000e-01 3{}'.format(ind, bonded, dih1, dih2, "\n")
           
    outfile1.writelines(ss)
    outfile2.writelines(ss2)
    outfile3.writelines(ss3)
    outfile4.writelines(ss4)
    outfile6.writelines(ss5)
    outfile6.writelines(ss6)
    
    
def write_for_index(outfile7, num, ind1, ind2, ind3, ind4, sug):
    sp = '{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{}'.format(sug, num, ind1, ind2, ind3, ind4, '\n')
    outfile7.writelines(sp)

out1 = 'COORD.txt'
out2 = 'GRO.txt'
out3 = 'DEF.txt'
out4 = 'BOND.txt'
out5 = 'ABAN.txt'
out6 = 'DIHED.txt'
out7 = 'INDEX.txt'

outfile1 = open(out1, 'w')
outfile2 = open(out2, 'w')
outfile3 = open(out3, 'w')
outfile4 = open(out4, 'w')
outfile5 = open(out5, 'w')
outfile6 = open(out6, 'w')
outfile7 = open(out7, 'w')

#infile1 = open('INIT.CONF.gro.original', 'r')
#infile2 = open('GLYCAN.PCT.txt.original', 'r')

infile1 = open(inp1, 'r')
infile2 = open(inp2, 'r')

#inp3 = 62.0
#inp4 = 88.0
#inp5 = 0.37
    
res_num, x_cord_prot, y_cord_prot, z_cord_prot = read_grofile(infile1)
count_prot_s, res_prot_s = read_sites(infile2)

x_sol = []
y_sol = []
z_sol = []

x_sol1 = []
y_sol1 = []
z_sol1 = []

prot_res = []

sug_count = 0
sug = 0

for k in range(count_prot_s):
    

    num = res_prot_s[k]
    x2, y2, z2 = read_coordinates(num, x_cord_prot, y_cord_prot, z_cord_prot)
    x3, y3, z3 = read_coordinates(num+1, x_cord_prot, y_cord_prot, z_cord_prot)
    x33, y33, z33 = read_coordinates(num-1, x_cord_prot, y_cord_prot, z_cord_prot)
    xs, ys, zs = solve_coordinates(x2, y2, z2, x3, y3, z3, x33, y33, z33, 117.0, 92.0, 0.38)
    xs1, ys1, zs1 = solve_coordinates(x2, y2, z2, x3, y3, z3, x33, y33, z33, 116.0, 90.0, 0.71)
    xs2, ys2, zs2 = solve_coordinates(x2, y2, z2, x3, y3, z3, x33, y33, z33, 116.4, 92.7, 1.12)
    xs3, ys3, zs3 = solve_coordinates(x2, y2, z2, x3, y3, z3, x33, y33, z33, 115.5, 90.9, 1.59)
    
    max_val = len(res_num) 
    
    solution = [xs, ys, zs, xs1, ys1, zs1, xs2, ys2, zs2, xs3, ys3, zs3]
    fl = check_real(solution, 5000)
    if fl == 0:
        print(solution)
        val1 = calc_prot_clashes(num, xs, ys, zs, x_cord_prot, y_cord_prot, z_cord_prot, 0.35)
        val2 = calc_prot_clashes(num, xs1, ys1, zs1, x_cord_prot, y_cord_prot, z_cord_prot, 0.35)
        val3 = calc_prot_clashes(num, xs2, ys2, zs2, x_cord_prot, y_cord_prot, z_cord_prot, 0.35)
        val4 = calc_prot_clashes(num, xs3, ys3, zs3, x_cord_prot, y_cord_prot, z_cord_prot, 0.35)
        print(val1, val2, val3, val4)
        if val1 == 0 and val2 == 0 and val3 == 0 and val4 == 0:
           x_sol, y_sol, z_sol = append_coord(xs, ys, zs, x_sol, y_sol, z_sol)
           x_sol, y_sol, z_sol = append_coord(xs1, ys1, zs1, x_sol, y_sol, z_sol)
           x_sol, y_sol, z_sol = append_coord(xs2, ys2, zs2, x_sol, y_sol, z_sol)
           x_sol, y_sol, z_sol = append_coord(xs3, ys3, zs3, x_sol, y_sol, z_sol)
           
           if len(x_sol) > 4:
               d1 = calc_sugar_clashes(x_sol, y_sol, z_sol, xs, ys, zs, 0.35)
               d2 = calc_sugar_clashes(x_sol, y_sol, z_sol, xs1, ys1, zs1, 0.35)
               d3 = calc_sugar_clashes(x_sol, y_sol, z_sol, xs2, ys2, zs2, 0.35)
               d4 = calc_sugar_clashes(x_sol, y_sol, z_sol, xs3, ys3, zs3, 0.35)
               
               d = [d1, d2, d3, d4]
               
               ds = check_real(d, 0)
               
               if ds == 0:
                    
                   x_sol1, y_sol1, z_sol1 = append_coord(xs, ys, zs, x_sol1, y_sol1, z_sol1)
                   x_sol1, y_sol1, z_sol1 = append_coord(xs1, ys1, zs1, x_sol1, y_sol1, z_sol1)
                   x_sol1, y_sol1, z_sol1 = append_coord(xs2, ys2, zs2, x_sol1, y_sol1, z_sol1)
                   x_sol1, y_sol1, z_sol1 = append_coord(xs3, ys3, zs3, x_sol1, y_sol1, z_sol1)
                   
                   ind = max_val + sug_count + 1
                   
                   write_output(outfile1, outfile2, outfile3, outfile4, outfile5, outfile6, ind, num, (num-1), (num-2), xs, ys, zs)
                   write_output(outfile1, outfile2, outfile3, outfile4, outfile5, outfile6, ind+1, ind, num, (num-1), xs1, ys1, zs1)
                   write_output(outfile1, outfile2, outfile3, outfile4, outfile5, outfile6, ind+2, ind+1, ind, num, xs2, ys2, zs2)
                   write_output2(outfile1, outfile2, outfile3, outfile4, outfile5, outfile6, ind+3, ind+2, ind+1, ind, xs3, ys3, zs3)
                   
                   sug_count = sug_count + 4
                   sug = sug + 1
                   
                   write_for_index(outfile7, num, ind, ind+1, ind+2, ind+3, sug)

print(sug)       
outfile1.close()
infile1.close()
infile2.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()
outfile7.close()
