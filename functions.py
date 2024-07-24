from info import *


def get_ingredient_list(coffee):
    """Make a list of the ingredients needed for the order"""
    ingredients_needed = []
    for ingredient in MENU[coffee]['ingredients']:
        ingredients_needed.append(ingredient)
    return ingredients_needed


def verify_sufficient_resources(coffee, ingredients_needed):
    """Verify that the available resources are sufficient for the order"""
    sufficient_resources = True
    for ingredient in ingredients_needed:
        amount_needed = MENU[coffee]['ingredients'][ingredient]
        amount_available = resources[ingredient]
        if amount_needed > amount_available:
            print(f"Insufficient {ingredient} for {coffee}.")
            sufficient_resources = False
    return sufficient_resources


def show_report():
    """Display the available resources"""
    for resource, amount in resources.items():
        if resource == 'money':
            print(f"{resource.title()}: ${amount:.2f}")
        else:
            print(f"{resource.title()}: {amount}")


def show_price(coffee):
    """Display the price of the order"""
    price = MENU[coffee]['cost']
    print(f"Your price is ${price:.2f}")
    return price


def get_payment():
    """Get user input for the payment of the order"""
    print("Insert money")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickles = int(input("Nickles: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies


def verify_payment(payment, coffee):
    """Verify that the payment is sufficient"""
    price = MENU[coffee]['cost']
    if payment < price:
        print("Insufficient payment.\nOrder Canceled\n")
        print(f"Change: ${payment:.2f}")
        return False
    else:
        try:
            resources["money"] += price
        except KeyError:
            resources["money"] = price
        change = payment - price
        if change > 0.0:
            print(f"Change: ${change:.2f}")
        return True


def pour_coffee(coffee, ingredients_needed):
    """Remove the resources used and simulate pouring the coffee"""
    for ingredient in ingredients_needed:
        resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]
    print(f"Here is your {coffee}. Enjoy!")
    return resources
