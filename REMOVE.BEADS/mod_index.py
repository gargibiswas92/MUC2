import sys

inp2 = open('INDEX.txt', 'r')

sug_num = []

for line2 in inp2:
    arr = line2.split()
    sug_num.append(int(arr[0]))
    
inp2.close()
max_num = max(sug_num)

#print('The number of sugars present is :', max_num)
#num = int(input('Enter the total number of sugars you want to keep:'))

num = int(sys.argv[1])

out1 = open('INDEX.mod.txt', 'w')
inp3 = open('INDEX.txt', 'r')
for line3 in inp3:
    arr2 = line3.split()
    sug_num2 = int(arr2[0])
    if sug_num2 <= num:
        out1.writelines(line3)
    else:
        continue

out1.close()
inp3.close()
    


