def calculator():
    p =int(input ("enter charahcter:"))
    t_table = []
    for x in range(1,p+1):
        table = []
        for i in range(1,x+1):
              table.append(i*x)
        t_table.append(table)
    print(t_table)   

print(calculator())