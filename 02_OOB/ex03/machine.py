from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random


class CoffeeMachine:

    def __init__(self) -> None:
        self.served_drinks = 0
        self.is_broken = False

    class EmptyCup(HotBeverage):

        def __init__(self) -> None:
            super().__init__()
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

        BLUE = '\033[94m'
        RED = '\033[91m'
        ORANGE = '\033[93m'
        GREEN = '\033[92m'
        RESET = '\033[0m'

        while True:

            user_input = input(f"👋 {BLUE}What drink do you want?\n{RESET}")

            if user_input == "exit":
                break
            elif user_input == "":
                user_input = "Coffee"
            elif user_input not in drinks.keys():
                print(f"{RED}This drink is not available.{RESET}\n")
                continue

            try:
                drink = machine.serve(drinks[user_input]())
                print(f"{drink}\n")
            except machine.BrokenMachineException as broken_machine:
                print(f"{RED}{broken_machine}{RESET}\n")
                repair = input(
                    f"🧑‍🔧 {BLUE}Do you want to repair the machine? " +
                    f"(yes/no){RESET}\n"
                )
                if repair == "yes":
                    machine.repair()
                    print(f"🧑‍🔧 {GREEN}The machine has been repaired.{RESET}\n")
                else:
                    print(f"🧑‍🔧 {ORANGE}The machine is still broken.{RESET}\n")

    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as error:
        print(error)
