def email_vald():
   while True:
        name = input("Enter your name: ")
        if name and not name.isdigit():
          break
        else:
          print("Please enter a valid name (non-empty and not an integer).")

   while True:
        email = input("Enter your email: ")
        if '@' in email and '.' in email:
          username, domain = email.split('@')
        if username and domain:
            x,y=domain.split('.')
            if x and y:
                break
        else:
          print("Please enter a valid email address.")
   print(f"\nName: {name}")
   print(f"Email: {email}")

print(email_vald())