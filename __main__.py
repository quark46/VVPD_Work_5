import math

def sinh_taylor(x, terms=50):
    """Вычисляет sh(x) с использованием разложения в ряд Тейлора"""

    sinh_x = 0
    for n in range(terms):
        term = (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sinh_x += term
    return sinh_x


def main():
    pass


'''x = 1.0
print(f"sinh({x}) = {sinh_taylor(x)}")
print(f"Точное значение math.sinh({x}) = {math.sinh(x)}")'''

if __name__ == "__main__.py":
    main()