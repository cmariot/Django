def print_numbers():
    with open("numbers.txt", "r") as f:
        file_content = f.read()
        numbers_list = file_content.split(",")
        for number in numbers_list:
            print(number)


if __name__ == "__main__":
    try:
        print_numbers()
    except Exception as e:
        print(e)
