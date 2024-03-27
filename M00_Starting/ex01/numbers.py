def print_numbers():
    with open("numbers.txt", "r") as f:
        file_lines = f.read().splitlines()
        for line in file_lines:
            numbers_list = line.split(",")
            for number in numbers_list:
                if not number.isdigit():
                    raise ValueError("The file contains non-integer values")
                print(number)


if __name__ == "__main__":
    try:
        print_numbers()
    except Exception as e:
        print(e)
