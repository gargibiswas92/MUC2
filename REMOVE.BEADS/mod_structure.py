infile1 = input("Enter the name of the structure (.gro) file:")

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
aban_list = []
print('The number of sugards present is :', max_num)
num = int(input('Enter the total number of sugars you want to keep:'))

aban_list = []

def write_gro(line, aban_list):
    flag = 0
    index = int(line[0:5])
    if index in aban_list:
        flag = 1
    return flag

inp1 = open(infile1, 'r')
count = 0
for line in inp1:
    count = count + 1

inp1.close()
print(count)
inp3 = open(infile1, 'r')

out1 = open('MOD.gro', 'w')

count1 = 0
for line3 in inp3:
    count1 = count1 + 1
    if count1 == 1 or count1 == 2 or count1 == count:
        fl = 0
    else:
        fl = write_gro(line3, aban_list)
        
    if fl == 0:
        out1.writelines(line3)
    else:
        continue
        
out1.close()
inp3.close()