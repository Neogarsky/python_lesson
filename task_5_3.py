"""
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None)

"""


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_klassa(name_tutors, number_klasses):
    """
    Генератор, возвращающий кортежи вида (<tutor>, <klass>)
    :param name_tutors: передает список tutors
    :param number_klasses: передает список klasses
    """

    klass_id = number_klasses[:]
    if len(name_tutors) > len(number_klasses):  # делаем проверку длины списков
        for element in range(len(name_tutors) - len(klass_id)):  # если список tutors больше
            klass_id.append(None)  # добавляем None в конце списка
    for tutors_result, klasses_result in zip(name_tutors, klass_id):  # преобразуем 2 списка в картеж по параметрам
        yield tutors_result, klasses_result


result = gen_klassa(tutors, klasses)
print(*result)
