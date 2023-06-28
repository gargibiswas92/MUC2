import sys
import numpy as np  

infile1 = sys.argv[1]
#infile1 = input("Enter the name ofthe topoloy file:")
ind = np.loadtxt('INDEX.mod.txt')
sug_ind = ind[:,0]
prot_ind = ind[:,1]
sug1 = ind[:,2]
sug2 = ind[:,3]
sug3 = ind[:,4]
sug4 = ind[:,5]

max_val = int(max(sug4))
ch_sug = int(max(sug_ind))
max_sys = max_val + ch_sug

out1 = open('sod_def.txt', 'w')
inp1 = open(infile1, 'r')

for ind in range(max_val+1, max_sys+1):
    ss3 = ' {:>5d}        SOD  {:>5d}    SOD    SOD  {:>5d}{}'.format(ind, ind, ind, "\n")
    out1.writelines(ss3)
    
out1.close()
count = 1

for line in inp1:
    count = count + 1
    if ('bonds' in line):
        last = count
inp1.close()

out2 = open('MOD.red.top', 'w')
inp2 = open(infile1, 'r')

count2 = 1
for line2 in inp2:
    count2 = count2 + 1
    if count2 <= last-2:
        out2.writelines(line2)
inp2.close()

inp3 = open('sod_def.txt', 'r')

for line3 in inp3:
    out2.writelines(line3)
    
inp4 = open(infile1, 'r')
count3 = 1
for line4 in inp4:
    count3 = count3 + 1
    if count3 >= last:
        out2.writelines(line4) 
inp4.close()

out2.close()
