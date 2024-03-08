def isNumberInFibo(n):
    f = [0, 1]
    i = 0
    while n not in f and f[-1] < n:
        f.append(f[i-1] + f[i-2])
        
    if n in f:
        return True
    return False

number = int(input())

if isNumberInFibo(number):
    print(f"O número {number} faz parte da sequência de Fibonacci")
else:
    print(f"O número {number} não faz parte da sequência de Fibonacci")