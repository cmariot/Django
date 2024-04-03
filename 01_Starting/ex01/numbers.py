def print_numbers():
    file_content = ""
    with open("numbers.txt", "r") as file:
        file_content = file.read()
    numbers_list = file_content.split(",")
    for number in numbers_list:
        print(number.strip('\n'))


if __name__ == "__main__":
    try:
        print_numbers()
    except Exception as e:
        print(e)
