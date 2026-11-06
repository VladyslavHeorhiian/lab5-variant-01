# Лабораторна робота №1
# Георгіян Владислав
# EIP30
# Варіант 1

import math

def targetFunction(x):
    return math.acos(x ** 2) - x

def solveBisection(func, a, b, e):
    result = {
            "x": 0,
            "iteration_number": 0,
            "calculation_protocol": []
            }

    if func(a) * func(b) > 0 or b <= a:
        return "Неправильні початкові межі"
    elif func(a) * func(b) == 0:
        if func(a) == 0:
            x = a
        elif func(b) == 0:
            x = b

        result["x"] = x
        result["calculation_protocol"].append((a, b, x))
        return result

    while (b - a) / 2 >= e:
        result["iteration_number"] += 1
        c = (a + b) / 2
        result["calculation_protocol"].append((a, b, c))
        
        if func(a) * func(c) < 0:
            b = c
        elif func(a) * func(c) > 0:
            a = c
        elif func(c) == 0:
            result["x"] = c
            return result

    result["calculation_protocol"].append((a, b, (a + b) / 2))
    result["x"] = (a + b) / 2

    return result