def solution(n, recipes, orders):
    answer = 0
    fire_places = [0 for _ in range(n)]

    recipes_dict = {}
    for recipe in recipes:
        menu, cooking_time = recipe.split()
        recipes_dict[menu] = int(cooking_time)

    for order in orders:
        menu_name, order_time = order.split()
        order_time = int(order_time)
        cooking_time = recipes_dict[menu_name]

        min_fire_place = fire_places[0]
        for fire_place in fire_places:
            min_fire_place = min(min_fire_place, fire_place)
        
        for i in range(len(fire_places)):
            if fire_places[i] == min_fire_place:
                fire_places[i] = max(fire_places[i], order_time) + cooking_time
                answer = fire_places[i]
                break

    return answer


print(solution(2, ["A 3","B 2"], ["A 1","A 2","B 3","B 4"]))
print(solution(3, ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"], ["PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "SPAGHETTI 6", "PIZZA 7", "SPAGHETTI 8"]))
print(solution(1, ["COOKIE 10000"], ["COOKIE 300000"]))