
a =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
k = int(input("Введите шаг шифровки: ")) # Шаг шифровки
message = input("Введите сообщение: ").upper() # создаем переменнную, куда запишем сообщение
shifrovka = '' #создаем переменную для вывода итогового сообщения
deshifrovka = ''


for i in message:
    place = a.find(i) # Ищет элемент по индексу
    newPlace = place + k
    shifrovka = shifrovka + a[newPlace]
    deshifrovka = deshifrovka + a[newPlace - k]



print(shifrovka, deshifrovka)


# Что касается метода upper() в 4 строчке, то я хз почему но без него эта хрень выводит только символы BBBB
