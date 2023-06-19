import sys

end_sug = int(sys.argv[1]) + 1
end_sod = int(sys.argv[2]) + 1

def write_index_file(init, end, name, outfile):
    count1 = 0 
    namestring = '[ '+name+' ]'
    sp_0 = ["\n", namestring,"\n"]
    outfile.writelines(sp_0)
    for j in range(init,end):
        count1 = count1 + 1
        if count1 <= 15:
           sp_1 = [str(j), " "]
           outfile.writelines(sp_1)
        else:
           sp_2 = ["\n", str(j), " "]
           outfile.writelines(sp_2)
           count1 = 1
           continue
       
out1 = open('index_file.ndx', 'w')

write_index_file(1, 16885, 'body', out1)
write_index_file(16885, end_sug, 'tail', out1)
write_index_file(1, end_sod, 'system', out1)
out1.close()