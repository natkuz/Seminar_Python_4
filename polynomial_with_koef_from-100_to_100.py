# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от -100 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def random_polynomial_dict(coef_range_min = -100, coef_range_max = 100):
    import random
    max_power = int(input('Enter max power: '))
    equation_dict = {}
    for i in range(max_power, -1, -1):
        equation_dict[i] = random.randint(coef_range_min, coef_range_max)
    return equation_dict

def polynomial_list(equation: dict):
    eq_str = ''
    for k, v in equation.items():
        if v > 1:
            if k == 1:
                eq_str += f'{v}*x+'
            elif k == 0:
                eq_str += f'{v}+'
            else:
                eq_str += f'{v}*x**{k}+'
        elif v == 1:
            if k == 1:
                eq_str += f'x+'
            elif k == 0:
                eq_str += f'{v}+'
            else:
                eq_str += f'x**{k}+'
        elif v == 0:
            eq_str += ''
        elif v == - 1:
            if k == 1:
                eq_str += f'-x+'
            elif k == 0:
                eq_str += f'{v}+'
            else:
                eq_str += f'-x**{k}+'
        else:
            if k == 1:
                eq_str += f'{v}*x+'
            elif k == 0:
                eq_str += f'{v}+'
            else:
                eq_str += f'{v}*x**{k}+'
    else:
        eq_str = eq_str[:-1]

    return eq_str.replace('+', ' ').replace('-', ' -').split()

def polynomial_str(equation: list):
    equation_new = []
    for item in equation:
        if item == equation[0]:
            equation_new.append(item)
        elif item.startswith('-'):
            equation_new.append(item)
        else:
            equation_new.append('+')
            equation_new.append(item)
    equation_new = ''.join(equation_new)
    return equation_new

polynom_dict = random_polynomial_dict()
print(f'Degrees and coefficients of a polynomial: {polynom_dict}')
polynom_list = polynomial_list(polynom_dict)

print()

with open('polynomial_with_koef_from-100_to_100.txt', 'w') as polynomial:
    polynomial.write(polynomial_str(polynom_list) + '=0')

with open('polynomial_with_koef_from-100_to_100.txt', 'r') as polynomial:
    for line in polynomial:
        print(line)