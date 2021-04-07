"""
2.	*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно)
не используя ключевое слово yield.
"""

# генератор нечетных чисел без yield
n = 31
generator_number = (element for element in range(1, n, 2))
print(*generator_number)