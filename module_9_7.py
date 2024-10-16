def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        for i in range(2, int(n)):
            if i == 1:
                continue
            if int(n) % i == 0:
                is_primes = False
                break
            else:
                is_primes = True
        if is_primes:
            print('Простое')
        else:
            print('Составное')
        return n
    return wrapper


@is_prime
def sum_three(*args):
    res = sum(args)
    return res

result = sum_three(2, 3, 6)
print(result)