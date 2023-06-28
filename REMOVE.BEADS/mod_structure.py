import sys

#infile1 = input("Enter the name of the structure (.gro) file:")
infile1 = sys.argv[1]

inp2 = open('INDEX.txt', 'r')

sug_num = []
sug_ind1 = []
sug_ind2 = []
sug_ind3 = []
sug_ind4 = []

for line2 in inp2:
    arr = line2.split()
    sug_num.append(int(arr[0]))
    sug_ind1.append(int(arr[2]))
    sug_ind2.append(int(arr[3]))
    sug_ind3.append(int(arr[4]))
    sug_ind4.append(int(arr[5]))
    
inp2.close()
max_num = max(sug_num)

#print('The number of sugards present is :', max_num)
#num = int(input('Enter the total number of sugars you want to keep:'))
num = int(sys.argv[2])

aban_list = []
for i in range(len(sug_num)):
    if sug_num[i] > num:
        aban_list.append(sug_ind1[i])
        aban_list.append(sug_ind2[i])
        aban_list.append(sug_ind3[i])
        aban_list.append(sug_ind4[i])
    else:
        continue

def write_gro(line, aban_list):
    index = int(line[15:20])
    if index in aban_list:
        print(index)
        flag = 1
    else:
        flag = 0
    return flag

def write_file(fl, line, out1):
    if fl == 0:
        out1.writelines(line)

inp1 = open(infile1, 'r')
count = 0
for line in inp1:
    count = count + 1

inp1.close()
print(count)
inp3 = open(infile1, 'r')

out1 = open('MOD_str.gro', 'w')

count1 = 0
for line3 in inp3:
    count1 = count1 + 1
    if count1 > 2 and count1 < count:
        fl = write_gro(line3, aban_list)
        write_file(fl, line3, out1)
    else:
        fl = 0
        write_file(fl, line3, out1)
    
       
        
    
out1.close()
inp3.close()
