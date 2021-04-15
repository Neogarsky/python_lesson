"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) —
2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее
сообщение и завершать скрипт.
ДОП ЗАДАЧА
** менять цвет вывода
"""
import time
from colorama import Fore, Style


class TrafficLight:
    __color = None

    def running(self):
        print('Светофор работает\n')
        self.__color = 'Красный'
        print(f'Установлен цвет:{Fore.RED} {self.__color}')
        print(Style.RESET_ALL)
        time.sleep(7)

        self.__color = 'Жёлтый'
        print(f'Установлен цвет:{Fore.YELLOW} {self.__color}')
        print(Style.RESET_ALL)
        time.sleep(2)

        self.__color = 'Зелёный'
        print(f'Установлен цвет:{Fore.GREEN} {self.__color}')
        print(Style.RESET_ALL)
        time.sleep(5)
        while True:
            self.running()


t_light = TrafficLight()
print(t_light.running())
