def fibonacci_number(indexFib):
    if indexFib <= 0:
        return "Index <= 0"
    elif indexFib == 1:
        return 1
    elif indexFib == 2:
        return 1
    else:
        indexFib += 1
        a, b = 0, 1
        for _ in range(2, indexFib):
            a, b = b, a + b
        return b
try:
    indexFib = int(input("What index Fibanachi do you wont? \nWrite namber: "))
except ValueError:
    print("That's not an int!")
else: 
    try:
        result = fibonacci_number(indexFib)
        print("The Fibonacci number for this index is: ", result)
    except:
        print("Error")