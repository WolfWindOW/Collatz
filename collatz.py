def collatz(n):
    while n > 1: # loops while not equal to 1
        print(n)
        if n < 1:
            print("Only positive numbers, please.") 
            break
        elif n % 2 == 0: # n is even
            n = n//2
        elif n % 2 == 1: # n is odd
            n = 3*n + 1
    print(1)

def rounding():
    return int(round(float(input('Enter n: '))))

n = rounding()

collatz(n)