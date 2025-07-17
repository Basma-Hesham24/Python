def ordering_numbers():
    nums_input = input("Enter 5 numbers: ")
    numbers = list(map(int, nums_input.split()))

    asc_order = sorted(numbers)
    desc_order = sorted(numbers, reverse=True)
    print (numbers)
    print(asc_order)
    print(desc_order)
    

ordering_numbers()