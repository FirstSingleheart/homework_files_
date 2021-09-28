from pprint import pprint


# readlines().count()

def add_cook(file_name):
    cook_book = {}
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


pprint(add_cook("recipes.txt"))
