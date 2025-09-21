import math, time, random

def is_prime(num: int) -> bool:
    if num > 1:
        return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    return False


#Тест Миллера-Рабина
def is_prime_fast(num: int, k = 5) -> bool:
    if num <= 1: return False
    if num <= 3: return True
    if num % 2 == 0: return False
    d = num - 1
    r = 0
    
    while d % 2 == 0:
        d //= 2
        r += 1
    
    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)
        
        if x == 1 or x == num - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    
    return True


def find_largest_prime(limit: int, use_fast: bool = True) -> int:
    if limit < 2: return -1
    # return max([num for num in range(2, limit + 1) if is_prime_fast(num)])
    for num in range(limit, 1, -1):
        if is_prime(num): return num
