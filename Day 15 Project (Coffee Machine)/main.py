from resources import resources, MENU, coins


def brew_coffee(resources, MENU, coins, choice):

    total_coins = 0
    paid = False
    sufficient = True
    coffee = MENU[choice]

    while total_coins <= coffee["cost"] and sufficient:
        print("Please insert coins.")
        a = int(input("How many quarters inserted? "))
        b = int(input("How many dimes inserted? "))
        c = int(input("How many nickle inserted? "))
        d = int(input("How many pennies inserted? "))
        total_coins = round(a * coins["quarters"] + b * coins["dimes"] + c * coins["nickles"] + d * coins["quarters"], 2)
        if total_coins < coffee["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            total_coins = 0
            sufficient = False
        elif total_coins > coffee["cost"]:
            change = total_coins - coffee["cost"]
            print(f"Here is ${round(change, 2)} dollars in change.")
            paid = True
            coins["total_money"] += total_coins - change
        elif total_coins == coffee["cost"]:
            coins["total_money"] += total_coins
            paid = True

        if paid:
            ingredients = coffee["ingredients"]
            for ingredient, amount in ingredients.items():
                if amount > resources[ingredient]:
                    print(f"Sorry there is not enough water. Money refunded.")
                    sufficient = False
                    break
                else:
                    resources[ingredient] -= amount
            if sufficient:
                print(f"Here is your {choice} ☕. Enjoy!")
            else:
                coins["total_money"] -= coffee["cost"]

            return resources, coins


def report():
    for key in resources:
        print(f"{key.title()}: {resources[key]}")
    print(f"Total money: ${coins["total_money"]}")


def coffee_machine():
    while True:

        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == 'report':
            report()
        elif choice == 'off':
            print('Thank you...')
            exit()
        elif choice in MENU:
            brew_coffee(resources, MENU, coins, choice)
        else:
            print("Please enter a valid input")
            coffee_machine()


coffee_machine()

# if choice == "espresso":
            #     if coffee["ingredients"]["water"] <= resources["water"]:
            #         sufficient = True
            #     else:
            #         print(f"Sorry there is not enough water. Money refunded.")
            #         sufficient = False
            #     if coffee["ingredients"]["coffee"] <= resources["coffee"]:
            #         sufficient = True
            #     else:
            #         print("Sorry there is not enough coffee. Money refunded.")
            #         sufficient = False
            #
            # else:
            #     if coffee["ingredients"]["water"] <= resources["water"]:
            #         sufficient = True
            #     else:
            #         print(f"Sorry there is not enough water. Money refunded.")
            #         sufficient = False
            #     if coffee["ingredients"]["coffee"] <= resources["coffee"]:
            #         sufficient = True
            #     else:
            #         print("Sorry there is not enough coffee. Money refunded.")
            #         sufficient = False
            #     if coffee["ingredients"]["milk"] <= resources["milk"]:
            #         sufficient = True
            #     else:
            #         print("Sorry there is not enough milk. Money refunded.")
            #         sufficient = False
            #
            # if sufficient:
            #     if choice == "espresso":
            #         resources["water"] -= coffee["ingredients"]["water"]
            #         resources["coffee"] -= coffee["ingredients"]["coffee"]
            #     else:
            #         resources["water"] -= coffee["ingredients"]["water"]
            #         resources["coffee"] -= coffee["ingredients"]["coffee"]
            #         resources["milk"] -= coffee["ingredients"]["milk"]
            #
            #     print(f"Here is your {choice} ☕. Enjoy!")
            # else:
            #     resources["money"] -= coffee["cost"]