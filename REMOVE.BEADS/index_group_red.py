import numpy as np 

out1 = open('index_file_group_red.ndx', 'w')
    
ind = np.loadtxt('INDEX.mod.txt')
sug_ind = ind[:,0]
prot_ind = ind[:,1]
sug1 = ind[:,2]
sug2 = ind[:,3]
sug3 = ind[:,4]
sug4 = ind[:,5]

sug_ind = sug_ind.astype(int)
prot_ind = prot_ind.astype(int)
sug1 = sug1.astype(int)
sug2 = sug2.astype(int)
sug3 = sug3.astype(int)
sug4 = sug4.astype(int)

max_val = int(max(sug4))
ch_sug = int(max(sug_ind))
max_sys = max_val + ch_sug

sugar = np.concatenate((sug1, sug2, sug3, sug4))

def create_list(low_lim, up_lim):
    name = []
    count = 0
    for num in range(low_lim, up_lim):
        name.append(num)
        
    name1 = np.array(name)
    name1 = name1.astype(int)
    return name1

def write_index_file(list, name, outfile):
    count1 = 0 
    namestring = '[ '+name+' ]'
    sp_0 = ["\n", namestring,"\n"]
    outfile.writelines(sp_0)
    for item in list:
        count1 = count1 + 1
        if count1 <= 15:
           sp_1 = [str(item), " "]
           outfile.writelines(sp_1)
        else:
           sp_2 = ["\n", str(item), " "]
           outfile.writelines(sp_2)
           count1 = 1
           continue 
       
body = create_list(1, 16885)
tail = create_list(16885, max_val+1)
system = create_list(1, max_sys+1)
protein = create_list(1, max_val+1)
ions = create_list(max_val+1, max_sys+1)

write_index_file(body, 'body', out1)
write_index_file(tail, 'tail', out1)
write_index_file(system, 'system', out1)
write_index_file(sugar, 'sugars', out1)
write_index_file(sug4, 'charged sugars', out1)
write_index_file(ions, 'ions', out1)
write_index_file(protein, 'protein', out1)
