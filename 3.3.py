import math


def find_roots(a, b, c):
    D = b**2 - 4*a*c 
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        return None


def main():
    
    a_min = int(input("Введіть мінімальне значення для a: "))
    a_max = int(input("Введіть максимальне значення для a: "))
    b_min = int(input("Введіть мінімальне значення для b: "))
    b_max = int(input("Введіть максимальне значення для b: "))
    c_min = int(input("Введіть мінімальне значення для c: "))
    c_max = int(input("Введіть максимальне значення для c: "))
    
   
    for a in range(a_min, a_max + 1):
        if a == 0:
            continue  
        for b in range(b_min, b_max + 1):
            for c in range(c_min, c_max + 1):
                roots = find_roots(a, b, c)
                if roots:
                    if len(roots) == 1:
                        print(f"Коефіцієнти: a={a}, b={b}, c={c}. Єдиний корінь: x={roots[0]}")
                    else:
                        print(f"Коефіцієнти: a={a}, b={b}, c={c}. Корені: x1={roots[0]}, x2={roots[1]}")
                else:
                    print(f"Коефіцієнти: a={a}, b={b}, c={c}. Немає розв'язків.")


main()
