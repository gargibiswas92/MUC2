import numpy as np 

out1 = open('index_file_pull2.ndx', 'w')
    
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

def create_list(low_lim, up_lim):
    name = []
    count = 0
    for num in range(low_lim, up_lim):
        name.append(num)
        
    name1 = np.array(name)
    name1 = name1.astype(int)
    return name1
        
def find_sugar(list, prot_ind, sug1, sug2, sug3, sug4):
    new_list = []
    for item1 in list:
        for item2, item3, item4, item5, item6 in zip(prot_ind, sug1, sug2, sug3, sug4):
            if item1 == item2:
               new_list.append(item3)
               new_list.append(item4)
               new_list.append(item5)
               new_list.append(item6)
            else:
               continue
    list2 = np.append(list, new_list)
    return list2

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
       
def write_group_index(list1, list2, prot_ind, sug1, sug2, sug3, sug4, out1):
    
    for item, item2 in zip(list1, list2):
        new_list = find_sugar(item, prot_ind, sug1, sug2, sug3, sug4)
        new_list = new_list.astype(int)
        write_index_file(new_list, item2, out1)
    
              
body_c = create_list(4825, 7237)
body = create_list(1, 16886)
tail = create_list(16885, max_val+1)
system = create_list(1, max_val+1)


tail_a = create_list(20261, 22762)
tail_b = create_list(26138, 28639)
tail_d = create_list(37892, 40393)
tail_dd = create_list(34953, 37454)
tail_bb = create_list(23199, 25700)
tail_cc = create_list(29076, 31577)

tail_c1 = create_list(32015, 32516)
tail_c2 = create_list(32516, 33016)
tail_c3 = create_list(33016, 33516)
tail_c4 = create_list(33516, 34016)
tail_c5 = create_list(34016, 34516)

fix_tails = np.concatenate((tail_a, tail_b, tail_d, tail_dd, tail_bb, tail_cc))

tail_aa1 = create_list(17322, 17823)
tail_aa2 = create_list(17823, 18323)
tail_aa3 = create_list(18323, 18823)
tail_aa4 = create_list(18823, 19323)
tail_aa5 = create_list(19323, 19823)

write_index_file(body_c, 'body_c', out1)
write_index_file(body, 'body', out1)
write_index_file(tail, 'tail', out1)
write_index_file(system, 'system', out1)
write_index_file(fix_tails, 'fix_tails', out1)


group_b = [tail_c1, tail_c2, tail_c3, tail_c4, tail_c5]
name_b = ['tail_c1', 'tail_c2', 'tail_c3', 'tail_c4', 'tail_c5'] 
write_group_index(group_b, name_b, prot_ind, sug1, sug2, sug3, sug4, out1)


group_dd = [tail_aa1, tail_aa2, tail_aa3, tail_aa4, tail_aa5]
name_dd = ['tail_aa1', 'tail_aa2', 'tail_aa3', 'tail_aa4', 'tail_aa5'] 
write_group_index(group_dd, name_dd, prot_ind, sug1, sug2, sug3, sug4, out1)


out1.close()
