# Creating the menu (ingredients, cost)
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
# Determining the resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine = True
money=0
money_given=0
decision=""
reducer = "True"

# Calculating the money given
def money_givenn():
    global money_given
    print ("Please insert coins.")
    quarter = int(input("How many quarters: "))
    quarter *= 0.25
    dimes = int(input("How many dimes: "))
    dimes *= 0.1
    nickels = int(input("How many nickel: "))
    nickels *= 0.05
    pennies = int(input("How many dimes: "))
    pennies *= 0.01
    money_given = quarter + dimes + nickels + pennies
    return money_given

#
def get_key(val,resource):
    for key, value in resource.items():
        if val == value:
            return key
        return "key doesn't exist"

# Updating the remaining resource
def resource_reducer(resource,menu,decide):
    for i in list(menu[decide]["ingredients"].keys()):
        resource[i] = resource[i] - menu[decide]["ingredients"][i]

# To keep the resources positive values
def resource_increase(resource,menu,decide):
    for i in list(menu[decide]["ingredients"].keys()):
        resource[i] = resource[i] + menu[decide]["ingredients"][i]

# Calculating the change
def calculate_change(x,y):
    change = round((x-y),2)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is {change} in change.")

# Getting order from the customer, checking the resources, giving change to the customer
def decision():
    global money,machine
    decision = input("What would you like? (espresso/latte/cappuccino): ")
    if decision == "off":
        machine = False
    elif decision == "report":
        print(f"Water: {resources['water']} ml \nMilk: {resources['milk']} ml \nCoffee: {resources['coffee']} gr \nMoney: ${money} ")
    elif decision == "espresso" or "latte" or "cappuccino":

        resource_reducer(resources, MENU, decision)
        for i in resources:
            if resources[i] < 0:
                print(f"Sorry there is not enough {get_key(resources[i],resources)}")
                resource_increase(resources, MENU, decision)
                return
            else:
                money_given = money_givenn()
                calculate_change(money_given, MENU[decision]["cost"])
                # Money in the machine
                money += MENU[decision]["cost"]
                print(f"Here is your {decision} ☕️. Enjoy!")
                break

while machine:
    decision()

# todo: 1. print report
# todo: 2. check resources
# todo: 3. add money to report
# todo : 4. refunded
