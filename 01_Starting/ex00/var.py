def print_var(var):
    print(f"{var} est de type {type(var)}")


def my_var():
    vars = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]
    for var in vars:
        print_var(var)


if __name__ == "__main__":
    my_var()
