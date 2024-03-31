import sys


def parse_argument():
    if len(sys.argv) != 2:
        exit()
    return sys.argv[1]


def search_by_key(key, _dict: dict):
    if key not in _dict:
        print("Unknown state")
        exit()
    return _dict[key]


if __name__ == '__main__':
    try:

        state_input = parse_argument()

        states = {
            "Oregon": "OR",
            "Alabama": "AL",
            "New Jersey": "NJ",
            "Colorado": "CO"
        }

        abbr = search_by_key(state_input, states)

        capital_cities = {
            "OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"
        }

        capital_city = search_by_key(abbr, capital_cities)

        print(capital_city)

    except Exception as e:
        print(e)
