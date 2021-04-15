"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
 толщиной в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""


class Road:
    _length = 0
    _width = 0
    weight_of_asphalt = 3
    thickness = 5

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calculate(self):
        return self._length * self._width * self.weight_of_asphalt * self.thickness


amount = Road(length=20, width=25)
print(amount.calculate())
