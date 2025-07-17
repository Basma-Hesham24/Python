users =[{"name":"ahmed","password":"1234"},{"name":"mohamed","password":"5678"}]
x = input("Enter your name: ")
for user in users:
    if user["name"] == x:
     password = input("Enter your password: ")
     if user ["password"] == password:
        print("Welcome")
        break
     else :
       print("Unvalid")
    else: 
       continue
else:
    print("unauthorized")
    exit
