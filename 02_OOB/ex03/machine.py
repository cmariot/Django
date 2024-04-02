from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random


class CoffeeMachine:

    def __init__(self) -> None:
        self.served_drinks = 0
        self.is_broken = False

    class EmptyCup(HotBeverage):

        def __init__(self) -> None:
            self.name = "empty cup"
            self.price = 0.90
            self._description = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            exception_message = "This coffee machine has to be repaired."
            super().__init__(exception_message)

    def repair(self) -> None:
        self.is_broken = False
        self.served_drinks = 0

    def serve(self, beverage: HotBeverage) -> HotBeverage:

        random_number = random.randint(0, 1)

        if random_number == 1:
            self.served_drinks += 1
            if self.served_drinks >= 10 or self.is_broken:
                self.is_broken = True
                raise self.BrokenMachineException()
            return beverage
        else:
            if self.served_drinks >= 10 or self.is_broken:
                raise self.BrokenMachineException()
            return self.EmptyCup()


if __name__ == "__main__":

    try:

        machine = CoffeeMachine()

        drinks = {
            "HotBeverage": HotBeverage,
            "Coffee": Coffee,
            "Tea": Tea,
            "Chocolate": Chocolate,
            "Cappuccino": Cappuccino
        }

        while (True):

            user_input = input("What drink do you want?\n")

            if user_input == "exit":
                break
            elif user_input == "":
                user_input = "Coffee"

            if user_input not in drinks.keys():
                print("This drink is not available.")
                continue

            try:
                drink = machine.serve(drinks[user_input]())
                print(drink, "\n")
            except machine.BrokenMachineException as error:
                print(error)

                repair = input("Do you want to repair the machine? (yes/no)\n")

                if repair == "yes":
                    machine.repair()
                    print("The machine has been repaired.")
                else:
                    print("The machine is still broken.")

            except Exception as error:
                print(error)
                break

    except KeyboardInterrupt:
        print("\nGoodbye!")
