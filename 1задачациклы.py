number = float(input("Введите числа для нахождения среднего значения\n"))
if (number == 0):
   print("Ошибка.Попробуйте ввести числа ещё раз")
   exit(0)


summa = 0
amount = 0

while number != 0:

   summa += number
   amount += 1
   number = float(input())

print("Среднее значения равно ", summa / amount)