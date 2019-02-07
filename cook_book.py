def get_recipes(recipes_file='list_recipes.txt'):
    with open(recipes_file, encoding='utf8') as file:
        cook_book = dict()
        for line in file:
            dish = line.strip()
            number_ingridients = int(file.readline())
            ingridients_list = []
            for line in file:
                if len(line) > 1:
                    ingridients = dict()
                    value = line.split("|")
                    ingridients["ingridient_name"] = value[0]
                    ingridients["quantity"] = int(value[1])
                    ingridients["measure"] = value[2].strip()
                    ingridients_list.append(ingridients)
                else:
                    break
            cook_book[dish] = ingridients_list

        cook_book = list(cook_book.items())
        for key, value in cook_book[0:3]:
            print("  {}: ".format(key))
            for ingredients in value:
                print("    {}".format(ingredients))


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {
        'Омлет': [
            {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
            {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ]
    }

    cook_book = {k.lower(): v for k, v in cook_book.items()}
    dishes_list = {}

    for dish in dishes:
        for ingridients in cook_book[dish]:
            ingridient_list = dict(ingridients)
            ingridient_list['quantity'] *= person_count
            if ingridient_list['ingridient_name'] not in dishes_list:
                dishes_list[ingridient_list['ingridient_name']] = ingridient_list
            else:
                dishes_list[ingridient_list['ingridient_name']]['quantity'] += ingridient_list['quantity']


    print('Cписок продуктов с названием ингредиентов(и их количество)для блюд на', person_count, 'человека:')
    for dishes in dishes_list.values():
        print('  {}: {} {} '.format(dishes['ingridient_name'], dishes['measure'], dishes['quantity']))


def main_menu():
    recipes_file = input('Введите имя файла с рецептами ( list_recipes.txt ): ')
    get_recipes(recipes_file)

    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    get_shop_list_by_dishes(dishes, person_count)

main_menu()
# print(globals())

