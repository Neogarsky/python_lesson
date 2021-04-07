"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
"""


def odd_nums(n):
    """
    Генератор нечетный чисел, от 0 до n
    """

    # генерируем нечетные числа от 0 до n
    for index in (number for number in range(0, n) if number % 2):
        yield index


odd_to_31 = odd_nums(31)

# выводим результат генератора через next первых трех
print(next(odd_to_31))
print(next(odd_to_31))
print(next(odd_to_31))
print("*" * 25)  # разделяем результат вывода генератора

for i in odd_to_31:  # проходимся циклом по всем значениям генератора
    print(i)
