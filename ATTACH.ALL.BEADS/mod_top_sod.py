import sys

infile1 = sys.argv[1]
low_lim = sys.argv[2]
up_lim = sys.argv[3]

out1 = open('sod_def.txt', 'w')
inp1 = open(infile1, 'r')

for ind in range(low_lim, up_lim):
    ss3 = ' {:>5d}        SOD  {:>5d}    SOD    SOD  {:>5d}{}'.format(ind, ind, ind, "\n")
    out1.writelines(ss3)
    
out1.close()
count = 1

for line in inp1:
    count = count + 1
    if ('bonds' in line):
        last = count
inp1.close()

out2 = open('MOD.top', 'w')
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