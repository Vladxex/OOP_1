from Pet_Home import Cat

cat_1 = Cat("Барон", "мальчик", 2)
cat_2 = Cat("Сэм", "мальчик", 2)

cats = [cat_1, cat_2]

for cat in cats:
    print("Имя:", cat.getName(),
          "Пол:", cat.getGender(),
          "Возраст:", cat.getAge())