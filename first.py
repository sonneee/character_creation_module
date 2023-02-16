from math import sqrt

message = '''Добро пожаловать в самую лучшую программу для вычисления
             квадратного корня из заданного числа'''
print(message)


def calculate_square_root(number):
    '''Вычисляет квадратный корень.'''
    return sqrt(number)


def calc(your_number):
    '''Печатает квадратный корень.'''
    if your_number <= 0:
        return 'Нельзя вычислить корень'
    out = calculate_square_root(your_number)
    return f'''Мы вычислили квадратный корень из введённого вами числа.
              Это будет: {out}'''


print(message)
print(calc(25.5))
