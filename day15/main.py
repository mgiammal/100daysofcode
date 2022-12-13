MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01
PROFIT = 0.00


def get_order():
    """
    Get customer order. Return None if not valid order of espresso/latte/cappuccino
    :return:
    """
    customer_order = input("What would you like? (espresso/latte/cappuccino): ")
    if customer_order not in ["espresso", "latte", "cappuccino", "report", "off"]:
        return None
    return customer_order


def can_make_drink(drink_choice):
    """
    Takes in a drink order and checks to see if there are enough resources to make the drink
    :param drink_choice:
    :return: True or False
    """
    ingredients = drink_choice.get("ingredients")
    has_ingredients = True
    for key, value in ingredients.items():
        resource = resources.get(key)
        if resource < value:
            print(f"Sorry there is not enough {key}")
            has_ingredients = False
    return has_ingredients


def calculate_coins(coins):
    """
    Takes a dictionary of coin count inserted and returns the total value
    :param coins:
    :return: Coin sum
    """
    coin_sum = 0.0

    for key, value in coins.items():
        if key == "quarters":
            coin_sum += (value * QUARTER)
        elif key == "dimes":
            coin_sum += (value * DIME)
        elif key == "nickles":
            coin_sum += (value * NICKLE)
        elif key == "pennies":
            coin_sum += (value * PENNY)
    return coin_sum


def print_report():
    """
    Print resources and profit in a easy to read format
    :return:
    """
    print(f"Water: {resources.get('water')}ml\n"
          f"Milk: {resources.get('milk')}ml\n"
          f"Coffee: {resources.get('coffee')}g\n"
          f"Money: ${PROFIT}")


is_on = True

while is_on:
    customer_order = get_order()
    drink = MENU.get(customer_order)

    if customer_order == "off":
        is_on = False
    elif customer_order == "report":
        print_report()
    else:
        if can_make_drink(drink):
            print("Please insert coins.")
            coins = {
                "quarters": int(input("How many quarters? ")),
                "dimes": int(input("How many dimes? ")),
                "pennies": int(input("How many pennies? "))
            }
            customer_money = calculate_coins(coins)
            cost = drink.get("cost")
            if customer_money < cost:
                print("Sorry that's not enough money. Money refunded")
            else:
                PROFIT += customer_money
                if customer_money > cost:
                    change = round(customer_money - cost, 2)
                    print(f"Here is ${change} dollars change.")

                for key, value in drink.get("ingredients").items():
                    resources[key] -= value
                print(f"Here is your {customer_order}. Enjoy!")
