def fib():
    a, b = 0, 1

    for i in range(5):
        print(a, b)
        a += b 
        b = a + b 
fib()