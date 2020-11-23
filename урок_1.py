print("Укажите первое число: ")
a = int(input())
print("Укажите второе число: ")
b = int(input())
print("Укажите третье число: ")
c = int(input())
print("Первое:", a, "; Второе:", b, "; Третье:", c)

print("Введите время в секундах")
seconds = int(input())
seconds_remainder = int(seconds%60)
minutes = seconds//60
minutes_remainder = int(minutes%60)
hour = seconds//360
print(hour, ":", minutes_remainder, ":", seconds_remainder)

print("Укажите число")
numb_one = input()
numb_two = numb_one + numb_one
numb_three = numb_two + numb_one
numb_one = int(numb_one)
numb_two = int(numb_two)
numb_three = int(numb_three)
total = numb_one + numb_two + numb_three
print(numb_one, "+", numb_two, "+", numb_three, "=", total)

print("Введите целое положительное число: ")
result = input()
result = list(result)
max = result[0]
pos = 0
for i in range(len(result)):
    if result[i] > max: max = result[i]; pos=i
print("Максимальная цифра: ", max)

print("Введите сумму выручки: ")
proceeds = int(input())
print("Введите сумму издержек: ")
costs = int(input())
print("Введите количество сотрудников фирмы: ")
employees = int(input())
value = proceeds - costs
if value > 0:
    print("Прибыль фирмы состовляет: ", value)
    profitability = value / proceeds
    print("Рентабельность выручки: ", profitability)
    value_for_each = value // employees
    print("Прибыль фирмы на каждого сотрудника: ", value_for_each)
else:
    value= value * -1
    print("Убыток фирмы составляет: ", value)

print("Введите количество километров в первый день: ")
first_day = int(input())
print("Введите общий результат спортсмена составить не менее: ")
last_day = int(input())
i = 2
next_day = first_day + (first_day / 10)
while True:
    if last_day <= next_day:
        print("Номер дня:", i, ",на который общий результат спортсмена составить не менее ", last_day, "километров")
        break
    else:
        i = i + 1
        next_day = next_day + (next_day / 10)