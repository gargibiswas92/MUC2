import numpy as np 

out1 = open('index_file2.ndx', 'w')
    
ind = np.loadtxt('INDEX.txt')
sug_ind = ind[:,0]
prot_ind = ind[:,1]
sug1 = ind[:,2]
sug2 = ind[:,3]
sug3 = ind[:,4]
sug4 = ind[:,5]

max_val = int(max(sug4))

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
    
              
body_a = create_list(2413, 4825)
body_b = create_list(9649, 12061)
body_c = create_list(4825, 7237)
body_d = create_list(7237, 9649)
body_bb = create_list(12061, 14473)
body = create_list(1, 16886)
tail = create_list(16885, max_val)
system = create_list(1, max_val)

write_index_file(body_a, 'body_a', out1)
write_index_file(body_b, 'body_b', out1)
write_index_file(body_c, 'body_c', out1)
write_index_file(body_d, 'body_d', out1)
write_index_file(body_bb, 'body_bb', out1)
write_index_file(body, 'body', out1)
write_index_file(tail, 'tail', out1)
write_index_file(system, 'system', out1)


tail_a1 = create_list(20261, 20762)
tail_a2 = create_list(20762, 21262)
tail_a3 = create_list(21262, 21762)
tail_a4 = create_list(21762, 22262)
tail_a5 = create_list(22262, 22762)

tail_b1 = create_list(26138, 26639)
tail_b2 = create_list(26639, 27139)
tail_b3 = create_list(27139, 27639)
tail_b4 = create_list(27639, 28139)
tail_b5 = create_list(28139, 28639)

tail_c1 = create_list(32015, 32516)
tail_c2 = create_list(32516, 33016)
tail_c3 = create_list(33016, 33516)
tail_c4 = create_list(33516, 34016)
tail_c5 = create_list(34016, 34516)

tail_d1 = create_list(37892, 38393)
tail_d2 = create_list(38393, 38893)
tail_d3 = create_list(38893, 39393)
tail_d4 = create_list(39393, 39893)
tail_d5 = create_list(39893, 40393)

tail_aa1 = create_list(17322, 17823)
tail_aa2 = create_list(17823, 18323)
tail_aa3 = create_list(18323, 18823)
tail_aa4 = create_list(18823, 19323)
tail_aa5 = create_list(19323, 19823)

tail_bb1 = create_list(23199, 23700)
tail_bb2 = create_list(23700, 24200)
tail_bb3 = create_list(24200, 24700)
tail_bb4 = create_list(24700, 25200)
tail_bb5 = create_list(25200, 25700)

tail_cc1 = create_list(29076, 29577)
tail_cc2 = create_list(29577, 30077)
tail_cc3 = create_list(30077, 30577)
tail_cc4 = create_list(30577, 31077)
tail_cc5 = create_list(31077, 31577)

tail_dd1 = create_list(34953, 35454)
tail_dd2 = create_list(35454, 35954)
tail_dd3 = create_list(35954, 36454)
tail_dd4 = create_list(36454, 36954)
tail_dd5 = create_list(36954, 37454)

group_a = [tail_a1, tail_a2, tail_a3, tail_a4, tail_a5]
name_a = ['tail_a1', 'tail_a2', 'tail_a3', 'tail_a4', 'tail_a5'] 
write_group_index(group_a, name_a, prot_ind, sug1, sug2, sug3, sug4, out1)

group_b = [tail_b1, tail_b2, tail_b3, tail_b4, tail_b5]
name_b = ['tail_b1', 'tail_b2', 'tail_b3', 'tail_b4', 'tail_b5'] 
write_group_index(group_b, name_b, prot_ind, sug1, sug2, sug3, sug4, out1)

group_c = [tail_c1, tail_c2, tail_c3, tail_c4, tail_c5]
name_c = ['tail_c1', 'tail_c2', 'tail_c3', 'tail_c4', 'tail_c5'] 
write_group_index(group_b, name_b, prot_ind, sug1, sug2, sug3, sug4, out1)

group_d = [tail_d1, tail_d2, tail_d3, tail_d4, tail_d5]
name_d = ['tail_d1', 'tail_d2', 'tail_d3', 'tail_d4', 'tail_d5'] 
write_group_index(group_d, name_d, prot_ind, sug1, sug2, sug3, sug4, out1)

group_aa = [tail_aa1, tail_aa2, tail_aa3, tail_aa4, tail_aa5]
name_aa = ['tail_aa1', 'tail_aa2', 'tail_aa3', 'tail_aa4', 'tail_aa5'] 
write_group_index(group_aa, name_aa, prot_ind, sug1, sug2, sug3, sug4, out1)

group_bb = [tail_bb1, tail_bb2, tail_bb3, tail_bb4, tail_bb5]
name_bb = ['tail_bb1', 'tail_bb2', 'tail_bb3', 'tail_bb4', 'tail_bb5'] 
write_group_index(group_bb, name_bb, prot_ind, sug1, sug2, sug3, sug4, out1)

group_cc = [tail_cc1, tail_cc2, tail_cc3, tail_cc4, tail_cc5]
name_cc = ['tail_cc1', 'tail_cc2', 'tail_cc3', 'tail_cc4', 'tail_cc5'] 
write_group_index(group_cc, name_cc, prot_ind, sug1, sug2, sug3, sug4, out1)

group_dd = [tail_dd1, tail_dd2, tail_dd3, tail_dd4, tail_dd5]
name_dd = ['tail_dd1', 'tail_dd2', 'tail_dd3', 'tail_dd4', 'tail_dd5'] 
write_group_index(group_dd, name_dd, prot_ind, sug1, sug2, sug3, sug4, out1)


out1.close()