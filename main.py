import Functions
from functools import reduce

working_in_hours = int(input("Введите количество часов: "))
rate_in_hours = int(input("Введите плату за час: "))
prize = int(input("Введите премию: "))
print("Задание 1, зарплата составляет:", Functions.salary(working_in_hours, rate_in_hours, prize))

original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print("Оригинальный список задание 2:", original_list)
print("Итоговый список задание 2:", list(Functions.more_before_going(original_list)))

print("Задание 3:", list(Functions.multiplicity()))

print("Итоговый список задание 4:", list(Functions.no_repetitions()))

random_numbs = list(Functions.random_numbers())
print("Задание 5:", reduce(Functions.random_numb_multiplication, random_numbs))

user_numb = int(input("Введите число: "))
Functions.task_six(user_numb)

user_answer = int(input("Введите число: "))
print("Задание 7, факториал числа", user_answer, "=", list(Functions.user_factorial(user_answer))[0])
