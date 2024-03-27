import sys


def parse_argument():
    if len(sys.argv) != 2:
        exit()
    return sys.argv[1]


def get_capital(state_input):

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    if state_input not in states:
        print("Unknown state")
        exit()

    state = states[state_input]

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if state not in capital_cities:
        print(f"Unknown capital city for state {state}")
        exit()

    return capital_cities[state]


if __name__ == '__main__':
    try:
        state_input = parse_argument()
        capital_city = get_capital(state_input)
        print(capital_city)
    except Exception as e:
        print(e)
