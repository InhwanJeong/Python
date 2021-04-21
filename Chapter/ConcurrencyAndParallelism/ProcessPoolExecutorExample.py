#from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    1099726123585419,
    1234726123585419,
    1543726123585419,
    123726123585419,
    16549726123585419,
    12139726123585419,
    112399726123585419,
]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_order(n):
    temp = n
    n = PRIMES[n]
    if n < 2:
        return False, temp
    if n == 2:
        return True, temp
    if n % 2 == 0:
        return False, temp

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False, temp
    return True, temp

#1. 순서가 필요할 때: 리스트의 번호를 넘겨줌
def main_order():
    PRIMES_COUNT_LIST = []
    i = 0
    for PRIME in PRIMES:
        PRIMES_COUNT_LIST.append(i)
        i = i + 1
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime_order, PRIMES_COUNT_LIST)):
            print('%d is prime: %s, %s번째 아이템' % (number, prime[0], prime[1]))

#2. 순서가 필요하지 않을 때: 리스트를 통째로 넘겨줌
def main_disorder():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    #main_disorder()
    while 1:
        main_order()