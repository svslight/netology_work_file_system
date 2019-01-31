with open('list_recipes.txt', encoding='utf8') as file:
    for line in file:
        dish1 = line.rstrip('\n')
        number = file.readline().rstrip('\n')
        ingredients1 = file.readline().rstrip('\n').split('|')
        ingredients2 = file.readline().rstrip('\n').split('|')
        ingredients3 = file.readline().rstrip('\n').split('|')
        ingredients4 = file.readline().rstrip('\n').split('|')
        dish2 = file.readline().rstrip('\n')
        number1 = file.readline().rstrip('\n')
        ingredients5 = file.readline().rstrip('\n').split('|')
        ingredients6 = file.readline().rstrip('\n').split('|')
        ingredients7 = file.readline().rstrip('\n').split('|')
        ingredients8 = file.readline().rstrip('\n').split('|')
        ingredients9 = file.readline().rstrip('\n').split('|')

        # print('dish1', dish1)
        # print('number', number)
        # print('ingredients1:', ingredients1)
        # print('ingredients2:', ingredients2)
        # print('ingredients3:', ingredients3)
        # print('ingredients4:', ingredients4)
        # print('dish2:', dish2)
        # print('number1:', number1)
        # print('ingredients5:', ingredients5)
        # print('ingredients6:', ingredients6)
        # print('ingredients7:', ingredients7)
        # print('ingredients8:', ingredients8)
        # print('--ingredients9:', ingredients9)

        keys = ['ingridient_name', 'quantity', 'measure']

        ingredient_1 = ingredients1
        dict_one = {}
        for k in keys:
            if k == 'ingridient_name':
                dict_one.setdefault(k, []).append(ingredient_1[0])
            elif k == 'quantity':
                dict_one.setdefault(k, []).append(ingredient_1[1])
            elif k == 'measure':
                dict_one.setdefault(k, []).append(ingredient_1[2])

        ingredient_2 = ingredients2
        dict_two = {}
        for k in keys:
            if k == 'ingridient_name':
                dict_two.setdefault(k, []).append(ingredient_2[0])
            elif k == 'quantity':
                dict_two.setdefault(k, []).append(ingredient_2[1])
            elif k == 'measure':
                dict_two.setdefault(k, []).append(ingredient_2[2])

        ingredient_3 = ingredients3
        dict_three = {}
        for k in keys:
            if k == 'ingridient_name':
                dict_three.setdefault(k, []).append(ingredient_3[0])
            elif k == 'quantity':
                dict_three.setdefault(k, []).append(ingredient_3[1])
            elif k == 'measure':
                dict_three.setdefault(k, []).append(ingredient_3[2])

        ingredient_5 = ingredients5
        dict_five = {}
        for k in keys:
            if k == 'ingridient_name':
                dict_five.setdefault(k, []).append(ingredient_5[0])
            elif k == 'quantity':
                dict_five.setdefault(k, []).append(ingredient_5[1])
            elif k == 'measure':
                dict_five.setdefault(k, []).append(ingredient_5[2])

        ingredient_6 = ingredients6
        dict_six = {}
        for k in keys:
            if k == 'ingridient_name':
                dict_six.setdefault(k, []).append(ingredient_6[0])
            elif k == 'quantity':
                dict_six.setdefault(k, []).append(ingredient_6[1])
            elif k == 'measure':
                dict_six.setdefault(k, []).append(ingredient_6[2])

        ingredient_7 = ingredients7
        dict_seven = {}
        for k in keys:
            if k == 'ingridient_name':
                dict_seven.setdefault(k, []).append(ingredient_7[0])
            elif k == 'quantity':
                dict_seven.setdefault(k, []).append(ingredient_7[1])
            elif k == 'measure':
                dict_seven.setdefault(k, []).append(ingredient_7[2])

        ingredient_8 = ingredients8
        dict_eight = {}
        for k in keys:
            if k == 'ingridient_name':
                dict_eight.setdefault(k, []).append(ingredient_8[0])
            elif k == 'quantity':
                dict_eight.setdefault(k, []).append(ingredient_8[1])
            elif k == 'measure':
                dict_eight.setdefault(k, []).append(ingredient_8[2])

        ingredient_9 = ingredients9
        len_ingredient_9 = len(ingredient_9)
        dict_nine = {}
        if len_ingredient_9 > 1:
             for k in keys:
                if k == 'ingridient_name':
                    dict_nine.setdefault(k, []).append(ingredient_9[0])
                elif k == 'quantity':
                    dict_nine.setdefault(k, []).append(ingredient_9[1])
                elif k == 'measure':
                    dict_nine.setdefault(k, []).append(ingredient_9[2])

        cook = {}
        cook.setdefault(dish1, list())
        ing_info1 = {"ingridient_name": dict_one["ingridient_name"], "quantity": dict_one["quantity"], "measure": dict_one["measure"]}
        ing_info2 = {"ingridient_name": dict_two["ingridient_name"], "quantity": dict_two["quantity"], "measure": dict_two["measure"]}
        ing_info3 = {"ingridient_name": dict_three["ingridient_name"], "quantity": dict_three["quantity"], "measure": dict_three["measure"]}
        cook[dish1].append(ing_info1)
        cook[dish1].append(ing_info2)
        cook[dish1].append(ing_info3)

        cook2 = {}
        cook2.setdefault(dish2, list())
        ing_info5 = {"ingridient_name": dict_five["ingridient_name"], "quantity": dict_five["quantity"], "measure": dict_five["measure"]}
        ing_info6 = {"ingridient_name": dict_six["ingridient_name"], "quantity": dict_six["quantity"], "measure": dict_six["measure"]}
        ing_info7 = {"ingridient_name": dict_seven["ingridient_name"], "quantity": dict_seven["quantity"], "measure": dict_seven["measure"]}
        ing_info8 = {"ingridient_name": dict_eight["ingridient_name"], "quantity": dict_eight["quantity"], "measure": dict_eight["measure"]}
        cook2[dish2].append(ing_info5)
        cook2[dish2].append(ing_info6)
        cook2[dish2].append(ing_info7)
        cook2[dish2].append(ing_info8)

        if len_ingredient_9 > 1:
            ing_info9 = {"ingridient_name": dict_nine["ingridient_name"], "quantity": dict_nine["quantity"], "measure": dict_nine["measure"]}
            cook2[dish2].append(ing_info9)

        cook_book = {}

        for cook3 in [cook, cook2]:
            cook_book.update(cook3)

        for key, value in cook_book.items():
            print("{}: ".format(key))
            for ingredients in value:
                print("{}".format(ingredients))

        # print(cook_book)

def get_shop_list_by_dishes(arg_dishes, arg_person_count):
    for dishes in cook_book:
        print(dishes[0:])
        # print('Блюда:'.format(key["Фахитос"]))
        # print('Блюда:'.format(key[arg_dishes]))
        # print('Блюда:', values["ingridient_name"])

get_shop_list_by_dishes(input('\nВведите название блюд: '),
                        input('Введите количество приглашенных: '))



# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количетсва для блюда. Например, для такого вызова

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 8},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Обратите внимание, что ингредиенты могут повторяться
