class Intern:

    def __init__(
        self,
        name: str = "My name? I’m nobody, an intern, I have no name."
    ):
        self.Name = name

    def __str__(self) -> str:
        return self.Name

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self) -> Coffee:
        return self.Coffee()


if __name__ == "__main__":

    try:

        first_intern = Intern()
        print(f"Name of the first_intern : {first_intern}")

        second_intern = Intern("Mark")
        print(f"Name of the second_intern : {second_intern}")

        coffee = second_intern.make_coffee()
        print(f"The coffee that Mark made me : {coffee}")

        try:
            first_intern.work()
        except Exception as error:
            print(f"Error : {error}")

    except Exception as error:
        print(f"Error : {error}")
