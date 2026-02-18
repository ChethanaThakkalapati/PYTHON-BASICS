'''Design a module math_utils.py with functions:
factorial(n)
is_prime(n)
gcd(a,b)
Include exception handling for invalid or negative inputs. Import and test these functions from another script.
Concepts: Loops, recursion, functions, input validation.'''

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Prime check requires an integer.")
    if n < 0:
        raise ValueError("Prime check is not valid for negative numbers.")
    if n <= 1:
        return False

    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("GCD requires integer inputs.")
    if a < 0 or b < 0:
        raise ValueError("GCD is not defined for negative numbers.")

    
    while b != 0:
        a, b = b, a % b
    return a

n = int(input("Enter a number to find factorial: "))
print("Factorial:", factorial(n))

p = int(input("Enter a number to check prime: "))
print("Is Prime?:", is_prime(p))

a = int(input("Enter first number for GCD: "))
b = int(input("Enter second number for GCD: "))
print("GCD:", gcd(a, b))


