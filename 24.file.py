lines_data=['Ritik\n','karan\n','manoj\n']

with open("write_file.txt",'w') as f:
    f.write('Anuj\n')
    f.writelines(lines_data)