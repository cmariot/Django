import sys


def parse_argument():
    if len(sys.argv) != 2:
        exit()
    return sys.argv[1]


def search_by_value(value, _dict: dict):
    for key, val in _dict.items():
        if val == value:
            return key
    print("Unknown capital city")
    exit()


if __name__ == '__main__':
    try:

        city_input = parse_argument()

        capital_cities = {
            "OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"
        }

        capital = search_by_value(city_input, capital_cities)

        states = {
            "Oregon": "OR",
            "Alabama": "AL",
            "New Jersey": "NJ",
            "Colorado": "CO"
        }

        state = search_by_value(capital, states)

        print(state)

    except Exception as e:
        print(e)
