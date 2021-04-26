"""
Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться только к
клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток соответственно.
"""
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f' Размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка стала меньше: а теперь {sub} ' if sub > 0 else 'Клетка исчезла :('

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(24)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell * cell_2)
print(cell.make_order(7))
print(cell - cell_2)
print(cell / cell_2)