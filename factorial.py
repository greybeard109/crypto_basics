
def factorial(n):
    """Recursive implementation of the factorial function"""
    if n <=1:
        return n
    else:
        return factorial(n-1)*n

for i in range(1, 21):
    print(f'{i:2} {factorial(i):.2e}')
