class HotBeverage:

    price = 0.30
    name = "hot beverage"
    _description = "Just some hot water in a cup."

    def description(self) -> str:
        return self._description

    def __str__(self):
        str = f"name : {self.name}\n" + \
              f"price : {self.price}\n" +\
              f"description : {self.description()}"
        return str


class Coffee(HotBeverage):

    def __init__(self) -> None:
        self.name = "coffee"
        self.price = 0.40
        self._description = "A coffee, to stay awake."


class Tea(HotBeverage):

    def __init__(self) -> None:
        super().__init__()
        self.name = "tea"
        self.price = 0.30
        self._description = "Just some hot water in a cup."


class Chocolate(HotBeverage):

    def __init__(self) -> None:
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50
        self._description = "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):

    def __init__(self) -> None:
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45
        self._description = "Un po’ di Italia nella sua tazza!"


if __name__ == "__main__":
    try:

        classes = (
            HotBeverage(),
            Coffee(),
            Tea(),
            Chocolate(),
            Cappuccino()
        )

        for item in classes:
            print(item, "\n")

    except Exception as error:
        print(error)
