def fib(m):
    a, b = 0, 1
    for i in range(m):
        print(a)
        a, b = b, a+b

def fi(n):
    L = [0]
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
        L.append(a)
    return L
