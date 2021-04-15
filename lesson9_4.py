"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
 go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
 и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""

class Car:
    speed = 0
    Color = None
    Name = None
    Is_police = False

    def go(self):
        print('Автомобиль находится в движении')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self, direction):
        print(f'Автомобиль направляется{direction}')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    speed = 80
    Color = 'RED'
    name = 'AUDI'
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'превышение скорости{self.speed}')

class SportCar(Car):
    speed = 100
    Color = 'BLACK'
    name = 'Porsche'
    is_police = False


class WorkCar(Car):
    speed = 40
    Color = 'BLACK'
    name = 'FORD'
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'превышение скорости{self.speed}')


class PoliceCar(Car):
    speed = 110
    Color = 'White'
    name = 'SUBARU'
    is_police = True


auto = TownCar()
auto1 = SportCar()
auto2 = WorkCar()
auto3 = PoliceCar()
print(TownCar.speed)
auto.go()
auto.stop()
auto.turn(direction=' на запад')
auto.show_speed()
print('')
auto2.turn(direction=' на восток')
print('')
auto3.speed = 100
print(auto3.name)
print(auto3.Color)
print(auto3.speed)
