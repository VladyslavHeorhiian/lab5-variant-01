# Лабораторна робота №5
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

    result["x"] = (a + b) / 2

    return result

def saveResultsToFile(results):
    with open("results_variant_01.txt", "w", encoding = "utf-8") as file:
        if results == "Неправильні початкові межі":
            file.write(results)
            return results

        file.write(f"Корінь: {results["x"]}\n")
        file.write(f"Кількість ітерацій: {results["iteration_number"]}\n")
        
        base_offset = 25

        file.write(f"{'a':>{base_offset}}{'b':>{base_offset}}{'c':>{base_offset}}\n")
        i = 1
        for (a, b, c) in results["calculation_protocol"]:
            file.write(f"{i}){a:>{base_offset - 2 + (len(str(a)) // 2)}}{b:>{base_offset + (len(str(b)) - len(str(a))) // 2}}{c:>{base_offset + (len(str(c)) - len(str(b))) // 2}}\n")
            i += 1

    with open("results_variant_01.txt", "r", encoding = "utf-8") as file:
         return file.read()

def main():
    func = targetFunction
    a = 0
    b = 1
    e = 0.0001
    result = solveBisection(lambda x: math.acos(x ** 2) - x, a, b, e)
    print(saveResultsToFile(result))

if __name__ == "__main__":
    main()