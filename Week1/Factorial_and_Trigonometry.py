def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_2n(n):
    return factorial(2 * n)

def factorial_2n_add1(n):
    return factorial(2 * n + 1)

def trigonometric(x, n):
    sin_x = 0
    cos_x = 0
    sinh_x = 0
    cosh_x = 0
    for i in range(n + 1):
        sin_x += ((-1) ** i) * (x ** (2 * i + 1)) / factorial_2n_add1(i)
        cos_x += ((-1) ** i) * (x ** (2 * i)) / factorial_2n(i)
        sinh_x += (x ** (2 * i + 1)) / factorial_2n_add1(i)
        cosh_x += (x ** (2 * i)) / factorial_2n(i)
    
    print(f"approx_sin(x = {x}, n = {n}) = {sin_x}")
    print(f"approx_cos(x = {x}, n = {n}) = {cos_x}")
    print(f"approx_sinh(x = {x}, n = {n}) = {sinh_x}")
    print(f"approx_cosh(x = {x}, n = {n}) = {cosh_x}")

x = float(input("Enter x (in radians): "))
n = int(input("Enter n (number of terms): "))
trigonometric(x, n)