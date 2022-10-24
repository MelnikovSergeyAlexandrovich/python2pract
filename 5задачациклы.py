future_stroka = input("Введите строку:\n")

if future_stroka == '':
    print("Ошибка.")
    exit(0)

stroka = list(future_stroka)

for i in range(len(stroka)):
    if(i % 2 == 0):
        stroka[i] = stroka[i].upper()
        print(stroka[i], end='')
    else:
        stroka[i] = stroka[i].lower()
        print(stroka[i], end='')
print("\n\n")