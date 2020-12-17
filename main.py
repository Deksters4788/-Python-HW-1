import class_mod

next_color = class_mod.TrafficLight()
next_color.starting()

volume_asphalt = class_mod.Road()
volume_asphalt.calculation()

next_worker = class_mod.Position
print(f"{next_worker.get_full_name(class_mod.Position)} {next_worker.get_total_income(class_mod.Position)}")


class_car = input("Введите класс машины слитно латиницей: ")
next_car = class_mod.car_class(class_car)
if next_car == class_mod.PoliceCar:
    next_car.feature(class_mod.PoliceCar)
elif next_car == class_mod.WorkCar:
    next_car.show_speed(class_mod.WorkCar)
elif next_car == class_mod.SportCar:
    next_car.feature(class_mod.SportCar)
else:
    next_car.show_speed(class_mod.TownCar)

first_stationery = class_mod.Pen
second_stationery = class_mod.Pencil
third_stationery = class_mod.Handle
first_stationery.draw(class_mod.Pen)
second_stationery.draw(class_mod.Pencil)
third_stationery.draw(class_mod.Handle)
