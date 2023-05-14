cook_book = {}
with open('recipes.txt', encoding='utf8') as recipes:
    for recept in recipes:
        dish_name = recept.strip()
        ingredients = []
        ingredients_count = recipes.readline()
        for i in range(int(ingredients_count)):
            ingr = recipes.readline()
            ingredient_name, quantity, measure = ingr.split(" | ")
            ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
            ingredients.append(ingredient)
        recipes.readline()
        cook_book[dish_name] = ingredients


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        for dish_name, ingredients in cook_book.items():
            if dish_name == dish:
                for ingredient in ingredients:
                    ingredient_name, quantity, measure = ingredient.values()
                    measure_quantity_dict = {'measure': measure, 'quantity': int(quantity) * person_count}
                    shop_list_by_dishes[ingredient_name] = measure_quantity_dict
    print(shop_list_by_dishes)

get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 10)


