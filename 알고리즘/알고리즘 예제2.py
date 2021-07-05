# Prime Num
def isPrime(n):
    for i in range(2, n//2 + 1):
        if n%i==0:
            return False
    return True

n = int(input('정수 입력 :'))
prime = set()

for i in range(1, n):
    if isPrime(i):
        prime.add(i)

print(prime)
