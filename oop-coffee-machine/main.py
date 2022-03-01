from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Creating Objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice ==  "off":
        is_on = False
# TODO 1. Print Report
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()

    else:
        drink = menu.find_drink(choice)
# TODO 2. Resources are sufficient


        if coffee_maker.is_resource_sufficient(drink):
# TODO 3. Process Coins
# TODO 4. Check Transaction successful
            if money_machine.make_payment(drink.cost):
# TODO 5. Make coffee
                coffee_maker.make_coffee(drink)

