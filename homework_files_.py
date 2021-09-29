from pprint import pprint

cook_book = {}


# readlines().count()

def add_cook(file_name):
    with open(file_name) as f:
        for line in f:
            cook_name = line.strip()
            counter = int(f.readline())
            temp_list = []
            for cook in range(counter):
                ingredient, quantity, measure = f.readline().split("|")
                temp_list.append({'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure})
            cook_book[cook_name] = temp_list
            f.readline()
    return cook_book


add_cook("recipes.txt")
# pprint(cook_book)

shopping_dict = {}

def get_shop_list_by_dishes(dishes, person_count):
    temp_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shopping_dict:
                    temp_dict = {'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure'].strip("\n")}
                    shopping_dict[ingredient['ingredient_name']] = temp_dict
                else:
                    shopping_dict[ingredient]['quantity'] += int(ingredient['quantity']) * person_count
    return shopping_dict


get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 5)
pprint(shopping_dict)
