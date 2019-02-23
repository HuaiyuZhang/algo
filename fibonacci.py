# Recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Test
for c in range(20):
    print(fib(c), " ")    

# Non-recursion
def fib2(n):
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        x1 = 0
        x2 = 1
        x3 = x1 + x2
        counter = 3
        while counter <= n:
            x1 = x2
            x2 = x3
            x3 = x1 + x2
            counter += 1
        return x3
# Test
for c in range(20):
    print(fib2(c), " ")    