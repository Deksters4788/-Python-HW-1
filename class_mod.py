class TrafficLight:
    __color = ["red", "yellow", "green"]

    def starting(self):
        print(f"{TrafficLight.__color[0]}: 7 sec")
        print(f"{TrafficLight.__color[1]}: 2 sec")
        print(f"{TrafficLight.__color[2]}: 7 sec")

class Road:
    _length = 5000
    _width = 20

    def calculation(self):
        mass_asphalt = int(input("Введите массу асфальта в килограммах на квадратный метр: "))
        thickness = int(input("Введите толщену слоя в сантиметрах: "))
        thickness = thickness / 100
        weight = Road._length * Road._width * mass_asphalt * thickness
        print(f"Толщина асфальта составит: {int(weight)} тонн")

dictionary_income = {"wage": 50000, "bonus": 10000}
class Worker:
    name = "Vasya"
    surname = "Pupkin"
    position = "manager"
    _income = dictionary_income.get("wage") + dictionary_income.get("bonus")
    next_count = 0

class Position(Worker):
    def get_full_name(self):
        full_name = Worker.name + " " + Worker.surname
        Worker.next_count += 1
        return full_name
    def get_total_income(self):
        total_income = Worker._income
        Worker.next_count += 1
        return total_income

def car_class(car):
    car.lower()
    if car == "towncar":
        next_car = TownCar
    elif car == "sportncar":
        next_car = SportCar
    elif car == "workcar":
        next_car = WorkCar
    else:
        next_car = PoliceCar
    return next_car

class Car:
    speed = int(input("Введите скорость: "))
    color = input("Введите цвет: ")
    name = input("Введите название: ")
    is_police = bool(input("Введите полицейская ли это машина(если да то 1, если нет то 0): "))
    def go(self):
        if Car.speed > 0:
            return "Машина поехала\n"
        else:
            return ""
    def stop(self):
        if Car.speed == 0:
            return "Машина остановилась\n"
        else:
            return ""
    def turn(self):
        direction = input("Куда повернула машина: ")
        return f"Машина повернула на {direction}"
class TownCar(Car):
    def show_speed(self):
        print(f"{Car.go(Car)}{Car.stop(Car)}{Car.turn(Car)}")
        if Car.speed > 60:
            print("Машина превысила скорость")
class SportCar(Car):
    def feature(self):
        print(f"{Car.go(Car)}{Car.stop(Car)}{Car.turn(Car)}")
class WorkCar(Car):
    def show_speed(self):
        if Car.speed > 60:
            print(f"{Car.go(Car)}{Car.stop(Car)}{Car.turn(Car)}")
            print("Машина превысила скорость")

class PoliceCar(Car):
    def feature(self):
        print(f"{Car.go(Car)}{Car.stop(Car)}{Car.turn(Car)}")

class Stationery:
    title = ["pen", "pencil", "handle"]

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки с помощью:", Stationery.title[0])
class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки с помощью:", Stationery.title[1])
class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки с помощью:", Stationery.title[2])