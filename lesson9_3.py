"""
Реализовать базовый класс Worker (работник):
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
 содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать
данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": None, "bonus": None}


class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position(name="Mariya ", surname='Moroz', wage=11000, bonus=3000)
print(position.get_full_name())
print(position.get_total_income())
