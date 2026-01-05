from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    action = input(f"What would you like? ({menu.get_items()}): ").lower()
    if action == "espresso" or  action == "latte" or  action == "cappuccino":
        menuItem = menu.find_drink(action)
        if coffee_maker.is_resource_sufficient(menuItem):
            if money_machine.make_payment(menuItem.cost):
                coffee_maker.make_coffee(menuItem)      
        continue
    elif action == "report":
        coffee_maker.report()
        money_machine.report()
    elif action == "off":
        is_on = False