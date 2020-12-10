from itertools import cycle
from itertools import count

def salary(hours, pay, prize):
    return hours * pay + prize

def more_before_going(origin_list):
    try_cost = 0
    new_origin_list = []
    for origin_list[try_cost] in origin_list:
        if len(origin_list) - 1 == try_cost:
            yield new_origin_list
        elif origin_list[try_cost + 1] > origin_list[try_cost]:
            new_origin_list.append(origin_list[try_cost + 1])
        try_cost += 1

def multiplicity():
    return (el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0)

def no_repetitions():
    random_numbs = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    print("Исходный список задание 4:", random_numbs)
    return (el for el in random_numbs if random_numbs.count(el) == 1)

def random_numbers():
    return (el for el in range(100, 1001) if el % 2 == 0)

def random_numb_multiplication(previous, current):
    return previous * current

def task_six(user_answer):
    print("Задание 6 скрипт (а):", list((el for el in range(user_answer, user_answer + 10))))
    pre_assigned = [10, "eg", False, 456, "Dek"]
    try_cost = 0
    for el in cycle(pre_assigned):
        if try_cost > 10:
            break
        print("Скрипт (б), элемент №", try_cost + 1, ":", el)
        try_cost += 1

def user_factorial(user_answer):
    final_fact = 1
    for el in range(2, user_answer + 1):
        final_fact *= el
    yield final_fact
