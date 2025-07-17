emails = ["basmahwaked@gmail.com","ahmedali@yahoo.com","omarmahmoud66@outlook.com"]
Domain = list(map(lambda x: x.split("@")[1],emails))
print (Domain)
