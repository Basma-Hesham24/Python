def domain(email):
    try:
        return email.split("@")[1]
    except:
        return None