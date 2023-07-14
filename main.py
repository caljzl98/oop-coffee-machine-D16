from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# treat the imports above as an external library

menu = Menu()
cash_register = MoneyMachine()
coffee_machine = CoffeeMaker()

# until user types "off", the program is in an infinite loop.
while True:
    # get order
    prompt_message = f"What would you like? ({menu.get_items()}): "
    order = input(prompt_message).lower()
    
    coffee = None
    match order:
        # show amount of resources still available, and profits gained
        case "report":
            coffee_machine.report()
            cash_register.report()
        # stop the program
        case "off":
            break
        case _:
            coffee = menu.find_drink(order)
        
    # `coffee` may be `None` if customer enters an order that is not in the menu.
    if coffee and coffee_machine.is_resource_sufficient(coffee):
        print(f"The cost for {coffee.name} is: ${coffee.cost:.2f}")
        if cash_register.make_payment(coffee.cost):
            coffee_machine.make_coffee(coffee)