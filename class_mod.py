import numpy as np


class Matrix:
    first_matrix = []
    second_matrix = []
    total_matrix = []

    def __init__(self, first_matrix_string, second_matrix_sting):
        self.first_matrix = np.matrix(first_matrix_string)
        self.second_matrix = np.matrix(second_matrix_sting)

    def __add__(self, other):
        return self.first_matrix + self.second_matrix

    def __str__(self):
        return f"Итоговая матрица:\n{self.first_matrix + self.second_matrix}"


class Clothes:
    consumption_costume = 0
    consumption_coat = 0

    def coat_and_costume(self, coat_options, costume_options):
        self.consumption_coat = int(coat_options / 6.5 + 0.5)
        self.consumption_costume = int(2 * costume_options + 0.3)
        print(f"Общий расход ткани составляет:{self.consumption_coat} + {self.consumption_costume} = "
              f"{self.consumption_coat + self.consumption_costume}")

    @property
    def test_decorator(self):
        return f"Атрибуты класса: {self.consumption_costume}, {self.consumption_coat}"


class Cell:
    first_cell = int(input("Введите количество ячеек в первой клетке: "))
    second_cell = int(input("Введите количество ячеек во второй клетке: "))

    def __add__(self):
        return self.first_cell + self.second_cell

    def __sub__(self):
        return self.first_cell - self.second_cell

    def __mul__(self):
        return self.first_cell * self.second_cell

    def __truediv__(self):
        return self.first_cell // self.second_cell

    def __str__(self):
        return f"Все проведенные операции:\n" \
               f"1){self.first_cell} + {self.second_cell} = {self.first_cell + self.second_cell}\n" \
               f"2){self.first_cell} - {self.second_cell} = {self.first_cell - self.second_cell}\n" \
               f"3){self.first_cell} * {self.second_cell} = {self.first_cell * self.second_cell}\n" \
               f"4){self.first_cell} / {self.second_cell} = {self.first_cell // self.second_cell}\n"

    def make_order(self):
        try_cost = 1
        cell_str = "*"
        sum_cell = self.first_cell + self.second_cell
        sub_cell = self.first_cell - self.second_cell
        mul_cell = self.first_cell * self.second_cell
        truediv_cell = self.first_cell // self.second_cell
        while True:
            if sum_cell == try_cost:
                break
            elif try_cost % 5 == 0:
                try_cost += 1
                cell_str += "*\n"
            else:
                try_cost += 1
                cell_str += "*"
        print(f"Сложение\n{cell_str}")
        try_cost = 1
        cell_str = "*"
        while True:
            if sub_cell == try_cost:
                break
            elif try_cost % 5 == 0:
                try_cost += 1
                cell_str += "*\n"
            else:
                try_cost += 1
                cell_str += "*"
        print(f"Вычетание\n{cell_str}")
        try_cost = 1
        cell_str = "*"
        while True:
            if mul_cell == try_cost:
                break
            elif try_cost % 5 == 0:
                try_cost += 1
                cell_str += "*\n"
            else:
                try_cost += 1
                cell_str += "*"
        print(f"Умножение\n{cell_str}")
        try_cost = 1
        cell_str = "*"
        while True:
            if truediv_cell == try_cost:
                break
            elif try_cost % 5 == 0:
                try_cost += 1
                cell_str += "*\n"
            else:
                try_cost += 1
                cell_str += "*"
        print(f"Деление\n{cell_str}")



