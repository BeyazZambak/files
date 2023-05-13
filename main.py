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

print(cook_book)

