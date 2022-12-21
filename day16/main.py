from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    command = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    menu_item = menu.find_drink(command)
    if command == "report":
        coffee_maker.report()
        money_machine.report()
    elif command == "off":
        is_on = False
    elif menu_item is not None:
        if coffee_maker.is_resource_sufficient(command):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)

