prices = (4.95, 9.95, 14.95, 19.95, 24.95)
print("Цены. Скидка. Цены со скидкой.")
for i in prices:
    print(i,"\t", round(i*0.6,2) ,"\t",round(i-i*0.6,2))

