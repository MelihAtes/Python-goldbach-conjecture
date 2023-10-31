def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def goldbach_conjecture(n):
    if n % 2 != 0 or n <= 2:
        print("Enter an even number bigger than 2: ")
        return
    
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print(f"{n} = {i} + {n - i}")

while True:
    try:
        n = int(input("Enter an even number bigger than 2: "))
        goldbach_conjecture(n)
    except ValueError:
        print("Enter an even number bigger than 2: ")
