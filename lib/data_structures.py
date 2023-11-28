spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food.get('name') for food in spicy_foods]
    return (names)
        
# get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    spiciest_food =[food for food in spicy_foods if food.get('heat_level') >= 5]
    return(spiciest_food)

# get_spiciest_foods(spicy_foods)
    
        
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return(food)
    return None



def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] >=5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    num_of_foods = len(spicy_foods)

    if num_of_foods == 0:
        return 0
    else:
        return total_heat/num_of_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
