def calculator():
    p =int(input ("enter charahcter:"))
    for x in range(1,p+1):
     for b in range (1,x+1):
        print(f"{x}*{b}= {x*b}")

print(calculator())