import sys


def parse_argument():
    if len(sys.argv) != 2:
        exit()
    return sys.argv[1]


def get_state(city_input):

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    state = None
    for key, value in capital_cities.items():
        if value == city_input:
            state = key
            break

    if state is None:
        print("Unknown capital city")
        exit()

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    # Get the state name from the state abbreviation
    state_name = None
    for key, value in states.items():
        if value == state:
            state_name = key
            break

    if state_name is None:
        print("Unknown state")
        exit()

    return state_name


if __name__ == '__main__':
    try:
        city_input = parse_argument()
        state = get_state(city_input)
        print(state)
    except Exception as e:
        print(e)
