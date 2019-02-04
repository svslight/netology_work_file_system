with open('list_recipes.txt', encoding='utf8') as file:
    cook_book = dict()
    for line in file:
        dish = line.strip().lower()
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

print('Словарь рецептов')
for k, v in cook_book.items():
    print("  {}: ".format(k.capitalize()))
    for ingredients in v:
        print("    {}".format(ingredients))


def get_shop_list_by_dishes(dishes, person_count):
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
        print('  {}: '.format(dishes['ingridient_name']), dishes['measure'], dishes['quantity'])
    return dishes_list


def main_menu():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    get_shop_list_by_dishes(dishes, person_count)

main_menu()

