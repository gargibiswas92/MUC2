from math import sqrt
import sys

infile1 = sys.argv[1]
inp1 = open(infile1, "r")
infile2 = sys.argv[2]
inp2 = open(infile2, "r")

outfile1 = sys.argv[3]
outfile2 = sys.argv[4]
outfile3 = sys.argv[5]
outfile4 = sys.argv[6]
outfile5 = sys.argv[7]
outfile6 = sys.argv[8]

out1 = open(outfile1, "w")
out2 = open(outfile2, "w")
out3 = open(outfile3, "w")
out4 = open(outfile4, "w")
out5 = open(outfile5, "w")
out6 = open(outfile6, "w")

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

##***************************Reading files*****************************************##

for lines in inp2:
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
    
new_sug = []
old_sug = []
prot = []
x_sug = []
y_sug = []
z_sug = []

for line1 in inp1:
    arr = line1.split()
    new_sug.append(int(arr[0]))
    old_sug.append(int(arr[1]))
    prot.append(int(arr[2]))
    x_sug.append(float(arr[3]))
    y_sug.append(float(arr[4]))
    z_sug.append(float(arr[5]))
    
    
count = 0
x_cord_sug = []
y_cord_sug = []
z_cord_sug = []

##***********************Calculaing clashes***************************************##

for i in range(len(new_sug)):
    x1 = x_sug[i]
    y1 = y_sug[i]
    z1 = z_sug[i]
    pp = prot[i]
    ss = old_sug[i]
    flag = 0
    for j in range(len(res_num)):
        tt = res_num[j]
        #if tt >= pp+4 or tt <= pp-4 or tt != ss:
        if tt >= pp+4 or tt <= pp-4:
            x2 = x_cord[j]
            y2 = y_cord[j]
            z2 = z_cord[j]
        dis = sqrt(((x2 - x1)**2)+(y2 - y1)**2+(z2 - z1)**2)
        #if dis <= 1.0:
        #if dis <= 1.0:
        if dis <= 0.35:
            print(new_sug[i], old_sug[i], prot[i], tt, dis)
            flag = 1
            
    if len(x_cord_sug) > 1:
        for n in range(len(x_cord_sug)):
            xs1 = x_cord_sug[n]
            ys1 = x_cord_sug[n]
            zs1 = z_cord_sug[n]
            dis2 = sqrt(((xs1 - x1)**2)+(ys1 - y1)**2+(zs1 - z1)**2)
            #if dis2 <= 1.2:
            if dis2 <= 0.35:
                flag = 2
        
##*****************writing bond, defination, dihedrals and other outputs*******************************************##
    if flag == 0:
        count = count + 1
        ind = count + count_line
        x_cord_sug.append(x1)
        y_cord_sug.append(y1)
        z_cord_sug.append(z1)
        
        ss1 = 'HETATM {:>5s}  C1 0VA {:>5s} {:>10.2f} {:>7.2f} {:>7.2f}{}'.format(str(ind), str(ind), x1, y1, z1, "\n")
        out1.writelines(ss1)
        ss2 = '{:>5d}0VA     C1{:>5d} {:>7.3f} {:>7.3f} {:>7.3f}{}'.format(ind, ind, x1, y1, z1, "\n")
        out2.writelines(ss2)
        ss3 = ' {:>5s}       NB_2  {:>5s}    0VB     C1  {:>5s}{}'.format(str(ind), str(ind), str(ind), "\n")
        out3.writelines(ss3)
        ss4 = '{:>5s}   {:>5s}   1        6.987500432e-01 2.000000000e+04{}'.format(str(ind), str(ss), "\n")
        out4.writelines(ss4)
        ss5 = '{:>7d}{:>7d}{:>7d}{:>12.3f}{:>12.3f}{:>12.3f}{}'.format(ind, ss, pp, x1, y1, z1, "\n")
        out5.writelines(ss5)
        ss6 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        1.089800000e+03 1.000000000e+00 1{}'.format(ind, ss, pp, pp-1, "\n")
        ss7 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        3.269400000e+03 5.000000000e-01 3{}'.format(ind, ss, pp, pp-1, "\n")
        out6.writelines(ss6)
        out6.writelines(ss7)
        #print(ind, ss, pp, x1, y1, z1)
inp1.close()
inp2.close()
out1.close()
out2.close()
out3.close()
out4.close()
out5.close()
out6.close()
