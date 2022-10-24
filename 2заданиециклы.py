print("Нажмите Enter, когда возраст каждого посетителя будет введён.")
age = input("Введите возраст посетителя: ")
if age == '':
    print("Ошибка.")
    exit(0)

price = 0

while age != '':
    if 3 < int(age) < 12:
        price += 14
    elif 13 < int(age) < 65:
        price += 23
    elif int(age) > 65:
        price += 18
    else:
        price += 0
    age = input("Введите возраст посетителя: ")

print("Общая стоимость: ", price)





