person = {"имя": "Виктор", "возраст": "27", "рост": "193"}

# Добавляем элементы
person["вес"] = 93
person["любимое блюдо"] = "карбонара"
print(person)


# Изменяем элементы
person["вес"] = 139
print(person)

# Удаляем элементы
del person["любимое блюдо"]
print(person)

# Перебираем элементы с помощью цикла
for k, v in person.items():
    print(f"{k}: {v} ")


print("Ключи:")
# Перебор элементов по ключам
for i in person:
    print(i)

print("."*20)

if "рост" in person.keys():
        print("Есть")
else:
        print("Нет")



print("-"*20)
print("Значения:")
# Перебор элементов по значениям
for i in person.values():
    print(i)


# Полезные методы
print(person.get("имя"))

print(person.pop("рост")) #удаляет элемент из словаря
print(person)


