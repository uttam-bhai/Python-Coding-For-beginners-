# Uttam,500
# Dinesh,50
# Ankit,200
# Anurag,100
with open('salary.txt','r') as rf:
    with open('output.txt','a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary} ')