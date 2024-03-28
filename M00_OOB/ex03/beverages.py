class HotBeverage:

    price = 0.30
    name = "hot beverage"

    def description(self) -> str:
        return "Just some hot water in a cup."

    def __str__(self):
        str = f"name : {self.name}\n" + \
              f"price : {self.price}\n" +\
              f"description : {self.description()}"
        return str


class Coffee(HotBeverage):

    def __init__(self) -> None:
        self.name = "coffee"
        self.price = 0.40

    def description(self) -> str:
        return "A coffee, to stay awake."


class Tea(HotBeverage):

    def __init__(self) -> None:
        super().__init__()
        self.name = "tea"
        self.price = 0.30

    def description(self) -> str:
        return "Just some hot water in a cup."


class Chocolate(HotBeverage):

    def __init__(self) -> None:
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):

    def __init__(self) -> None:
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45

    def description(self) -> str:
        return "Un po’ di Italia nella sua tazza!"


if __name__ == "__main__":
    try:

        classes = [
            HotBeverage(),
            Coffee(),
            Tea(),
            Chocolate(),
            Cappuccino()
        ]

        for item in classes:
            print(item, "\n")

    except Exception as error:
        print(error)
