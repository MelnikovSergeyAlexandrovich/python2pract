stroka = input("Введите строку\n")
if stroka == '':
    print("Ошибка.")
    exit(0)

palendrom = ''.join(reversed(stroka))

if palendrom == stroka:
    print ("Данная строка является палиндромом")
else:
    print("Данная строка не является палиндромом")
