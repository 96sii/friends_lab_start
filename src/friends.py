def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            return True
    return False

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(people):
    total = 0
    for person in people:
        total += person["monies"]
    return total

def lend_money(person_1, person_2, money):
    person_1["monies"] -= money
    person_2["monies"] += money

def all_favourite_foods(people):
    lists_foods = []
    for person in people:
        lists_foods.append(["favourites"] ["snacks"])
    return lists_foods
