primes = [2,3,5,7,11,13]
num = 13
while len(primes)<10001:
    for i in range(len(primes)):
        if num % primes[i] == 0:
            num +=2
            break
    else:
        primes.append(num)

print(primes[-1])

