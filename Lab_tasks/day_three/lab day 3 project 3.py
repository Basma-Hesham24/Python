def verification (x):
    if '@' in x and '.' in x:
        username, domain = x.split('@')
        if username and domain:
            x,y=domain.split('.')
            if x and y:
             return True 
    else:
        print("false")

email= input("Enter your email: ")
print(verification(email))

