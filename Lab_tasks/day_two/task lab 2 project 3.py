def stars():
    list = [" "," "," "," "," "]
    for i in range (len(list)):
     list.append("*")
     list.remove(" ")
     print(list)

print(stars())