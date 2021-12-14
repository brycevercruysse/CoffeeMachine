from coffee import MENU, resources


def update_resources(drink_type):
    """Updates the coffee machine resources based on the type of drink selected"""
    for ingredient in MENU[drink_type]['ingredients']:
        resources[ingredient] = resources[ingredient] - MENU[drink_type]['ingredients'][ingredient]


def check_resources(drink_type):
    """Checks to see if there are enough resources in coffee machine to create selected drink"""
    for ingredient in MENU[drink_type]['ingredients']:
        if resources[ingredient] < MENU[drink_type]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return


def process_coins():
    """Calculates the total from the amount of coins inserted and returns the total amount"""
    print("Please insert coins.")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How may dimes? "))
    nickles = float(input("How may nickles? "))
    pennies = float(input("How may pennies? "))
    money_inserted = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
    return money_inserted


good_to_go = True
while good_to_go:
    user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_answer == "espresso" or user_answer == "latte" or user_answer == "cappuccino":
        total = process_coins()
        if total >= MENU[user_answer]['cost']:
            check_resources(user_answer)
            update_resources(user_answer)
            change_due = float(total - MENU[user_answer]['cost'])
            print(f"${round(change_due, 2)} is your change.")
            resources['money'] += MENU[user_answer]['cost']
            print(f"Enjoy your {user_answer}!")
            # print(resources)
        elif total < MENU[user_answer]['cost']:
            print("Sorry. That's not enough money. Money refunded.")
    elif user_answer == "report":
        for item in resources:
            print(f" {item}: {resources[item]}")
    elif user_answer == "off":
        good_to_go = False
