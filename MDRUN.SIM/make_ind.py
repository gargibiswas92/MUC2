import numpy as np   

outfile = open("index_new.ndx", "w")


ind = np.loadtxt('INDEX.txt')
sug_ind = ind[:,0]
prot_ind = ind[:,1]
sug1 = ind[:,2]
sug2 = ind[:,3]
sug3 = ind[:,4]
sug4 = ind[:,5]

max_val = int(max(sug4))
ch_sug = int(max(sug_ind))
max_sys = max_val + ch_sug

sp_0 = ["\n", "[ body ]","\n"]
outfile.writelines(sp_0)
count1 = 0 
for j in range(1,16885):
    count1 = count1 + 1
    if count1 <= 15:
        sp_1 = [str(j), " "]
        outfile.writelines(sp_1)
    else:
        sp_2 = ["\n", str(j), " "]
        outfile.writelines(sp_2)
        count1 = 1
        continue

sp_02 = ["\n","[ tails ]","\n"]
outfile.writelines(sp_02)
countp = 0
for j in range(16885,ch_sug+1):
    countp = countp + 1
    if countp <= 15:
        sp_p = [str(j), " "]
        outfile.writelines(sp_p)
    else:
        sp_pp = ["\n", str(j), " "]
        outfile.writelines(sp_pp)
        countp = 1
        continue


sp_01 = ["\n","[ system ]","\n"]
outfile.writelines(sp_01)
count11 = 0 
for j in range(1,max_sys+1):
    count11 = count11 + 1
    if count11 <= 15:
        sp_11 = [str(j), " "]
        outfile.writelines(sp_11)
    else:
        sp_21 = ["\n", str(j), " "]
        outfile.writelines(sp_21)
        count11 = 1
        continue
