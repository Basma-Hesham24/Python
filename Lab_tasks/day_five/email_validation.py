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

