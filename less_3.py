def degree(user_answer_one, user_answer_two):
    if user_answer_one == 0 or user_answer_two == 0:
        print("На ноль делить нельзя!!!")
    else:
        print(user_answer_one/user_answer_two)
        return user_answer_one/user_answer_two

def user_info(name, surname, age, city, email, number):
    user_information = "Имя: " + name + "; Фамилия: " + surname + "; Врзраст: " + age +\
                       "; Город проживания: " + city + "; Email: " + email + "; Телефоный номер: " + number
    return user_information

def most_sum_num(first, second, third):
    if first > third and second > third:
        return first + second
    elif first > second and third > second:
        return first +third
    elif second > first and third > second:
        return second + third

def exponentiation (one, two):
    return one**two

def total_amount(string):
    all_sum = 0
    try_cost = 0
    while True:
        if string[try_cost] == "q":
            return all_sum
        elif try_cost != len(string) - 1:
            all_sum += int(string[try_cost])
            try_cost += 1
        else:
            all_sum += int(string[try_cost])
            print(all_sum, "Введите числа разделяя их пробелами, (Чтобы закончить введите (q)): ")
            string = input()
            string = string.split()

def uppercase(user_words):
    return user_words.title()

first_answer = int(input("Введите первое число: "))
second_answer = int(input("Введите второе число: "))
degree(first_answer, second_answer)

user_name = input("Введите имя: ")
user_surname = input("Введите фамилию: ")
user_age = input("Введите возраст: ")
user_city_residence = input("Введите город проживания: ")
user_email = input("Введите email: ")
user_phone_number = input("Введите телефоный номер: ")

print(user_info(name=user_name, surname=user_surname, age=user_age,
                city=user_city_residence, email=user_email, number=user_phone_number))

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
third_num = int(input("Введите третье число: "))
print(most_sum_num(first_num, second_num, third_num))

first_arg = int(input("Введите целое положительное число: "))
second_arg = int(input("Введите целое отрицательное число: "))
print(exponentiation(first_arg, second_arg))

user_string = input("Введите числа разделяя их пробелами: ")
new_string = user_string.split()
print(total_amount(new_string))

user_word = input("Введите слова прописными латинскими буквами разделяя их пробелами: ")
print(uppercase(user_word))
