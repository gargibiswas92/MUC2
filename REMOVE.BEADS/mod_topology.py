infile1 = input("Enter the name of the topology file:")

inp1 = open(infile1, 'r')
count = 0
for line in inp1:
    count = count + 1
    if '[ atoms ]' in line:
        at_line = count
    if '[ bonds ]' in line:
        bo_line = count
    if '[ dihedrals ]' in line:
        di_line = count
    if '[ system ]' in line:
        sy_line = count
    else:
        continue
inp1.close()
print(at_line, bo_line, di_line, sy_line)

sug_num = []
sug_ind1 = []
sug_ind2 = []
sug_ind3 = []
sug_ind4 = []

inp2 = open('INDEX.txt', 'r')
for line2 in inp2:
    arr = line2.split()
    sug_num.append(int(arr[0]))
    sug_ind1.append(int(arr[2]))
    sug_ind2.append(int(arr[3]))
    sug_ind3.append(int(arr[4]))
    sug_ind4.append(int(arr[5]))
    
inp2.close()
max_num = max(sug_num)
aban_list = []
print('The number of sugards present is :', max_num)
num = int(input('Enter the total number of sugars you want to keep:'))

for i in range(len(sug_num)):
    if sug_num[i] > num:
        aban_list.append(sug_ind1[i])
        aban_list.append(sug_ind2[i])
        aban_list.append(sug_ind3[i])
        aban_list.append(sug_ind4[i])
    else:
        continue
    
inp3 = open(infile1, 'r')
out1 = open('MOD.top', 'w')

def write_def(line, aban_list):
    flag = 0
    arr1 = line.split()
    inde = int(arr1[0])
    if inde in aban_list:
        flag = 1
    return flag

def write_bond(line, aban_list):
    flag = 0
    arr1 = line.split()
    inde = int(arr1[0])
    inde1 = int(arr1[1])
    if inde in aban_list:
        flag = 1
    if inde1 in aban_list:
        flag = 1
    return flag
        
def write_dihedral(line, aban_list):
    flag = 0
    arr1 = line.split()
    inde = int(arr1[0])
    inde1 = int(arr1[1])
    inde2 = int(arr1[2])
    inde3 = int(arr1[3])
    if inde in aban_list or inde1 in aban_list or inde2 in aban_list or inde3 in aban_list:
        flag = 1
    return flag

count1 = 0
for line3 in inp3:
    count1 = count1 + 1
    if (count1 >= at_line + 2) and (count1 <= bo_line -2):
        fl1 = write_def(line3, aban_list)
    if (count1 >= bo_line + 2) and (count1 <= di_line -3):
        if line3.startswith(';'):
            continue
        if line3.strip():
           fl1 = write_bond(line3, aban_list)
        else:
            continue
    if (count1 >= di_line + 2) and (count1 <= sy_line -3):
        if line3.strip():
           fl1 = write_dihedral(line3, aban_list) 
    else:
        fl1 = 0
    if fl1 == 0:
        out1.writelines(line3)
out1.close()    