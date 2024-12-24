import math
import sys

menu_txt = ['"1" - Выполнить первую функцию',
            '"2" - Выполнить вторую функцию',
            '"3" - Выполнить третью функцию',
            '"4" - Завершить выполнение программы']
menu_error = 'Ошибка. Введите число в следующем диапазоне: [1, 4]'

def get_int(text, err_text, bounds=None):
    '''integer input'''
    while True:
        if isinstance(text, list):
            print('')
            print(*text, sep='\n')
        else:
            print('')
            print(text)
        inp = input()
        print('')
        try:
            inp = int(inp)
        except ValueError:
            print(err_text)
        if isinstance(inp, int):
            if isinstance(bounds, list):
                if bounds[0] <= inp <= bounds[1]:
                    return int(inp)
                print(err_text)
            else:
                return int(inp)


def menu(text, err_txt, bounds):
    '''menu'''
    user_inp = get_int(text, err_txt, bounds)
    return user_inp


def sinh_taylor(x, terms=50):
    """Вычисляет sh(x) с использованием разложения в ряд Тейлора"""

    sinh_x = 0
    for n in range(terms):
        term = (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sinh_x += term

    return sinh_x


def arctan_taylor(x, terms=50):
    """Вычисляет arctan(x) с использованием разложения в ряд Тейлора"""

    if abs(x) > 1:
        raise ValueError("Ряд Тейлора для arctan(x) сходится только при |x| <= 1")
    
    arctan_x = 0
    for n in range(terms):
        term = ((-1)**n * x**(2*n + 1)) / (2*n + 1)
        arctan_x += term

    return arctan_x


def main():
    while True:
        user_choise = menu(menu_txt, menu_error, [1, 4])
        match user_choise:
            case 1:
                x = get_int('Введите Х', 'Ошибка ввода')
                print(f"sinh({x}) = {sinh_taylor(x)}")
            case 2:
                x = get_int('Введите Х', 'Ошибка ввода. Введите число в диапазаоне от -1 до 1', [-1, 1])
                approx_value = arctan_taylor(x)
                print(f"arctan({x}) (аппроксимация) = {approx_value}")
            case 3:
                x = get_int('Введите Х', 'Ошибка ввода')
            case 4:
                sys.exit()


if __name__ == "__main__":
    main()