def validation(emails):
    try: 
        if "@" in emails:
            domain = emails.split("@")[1]
            if "." in domain:
                 return True
        return False
    except ValueError:
        print("invalid email")
        return False
for i in range (5):
    emails= (input("Enter your email:"))
    if validation(emails):
        print("Valid")
        break
    else:
        print("Invalid")
else:
    raise validation("Invalid")

import os
print(os.getcwd())

