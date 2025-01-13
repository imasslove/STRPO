def factorial(n):
    if n < 0:
        return "Факториал определяется только для неотрицательных чисел."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Пример использования
n = int(input("Введите натуральное число n: "))
print(f"Факториал числа {n} равен {factorial(n)}")
