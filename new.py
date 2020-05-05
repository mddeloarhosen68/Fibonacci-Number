#Ex:1
def fib(n):

    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)


    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fib(100)


#Ex:2
def fib(n):

    a = 0
    b = 1


    print(a)
    print(b)


    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fib(int(input("Enter your input: ")))