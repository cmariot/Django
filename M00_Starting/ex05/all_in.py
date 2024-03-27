import sys


def parse_argument():
    if len(sys.argv) != 2:
        exit()
    splitted_arg = sys.argv[1].split(",")
    elements = []
    for elem in splitted_arg:
        stripped_elem = elem.strip()
        if len(stripped_elem) != 0:
            elements.append(stripped_elem)
    return elements


def get_state(city_input):

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    state = None
    for key, value in capital_cities.items():
        if value.upper() == city_input.upper():
            state = key
            capital_city_correct = value
            break

    if state is None:
        return False, None, None

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    # Get the state name from the state abbreviation
    state_name = None
    for key, value in states.items():
        if value.upper() == state.upper():
            state_name = key
            break

    if state_name is None:
        return False, None, None

    return True, state_name, capital_city_correct


def get_capital(state_input):

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    state = None
    state_correct = None
    for key, value in states.items():
        if key.upper() == state_input.upper():
            state = value
            state_correct = key
            break

    if state is None:
        return False, None, None

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    capital_city = None

    for key, value in capital_cities.items():
        if key.upper() == state.upper():
            capital_city = value
            break

    if capital_city is None:
        return False, None, None

    return True, state_correct, capital_city


if __name__ == '__main__':
    try:

        elements = parse_argument()

        for elem in elements:

            # If the element is a capital city, we get the state
            is_a_capital_city, state, capital_city = get_state(elem)
            if is_a_capital_city:
                print(f"{capital_city} is the capital of {state}")
                continue

            # If the element is a state, we get the capital city
            is_a_state, state, capital_city = get_capital(elem)
            if is_a_state:
                print(f"{capital_city} is the capital of {state}")
                continue

            # If the element is neither a capital city nor a state
            print(f"{elem} is neither a capital city nor a state")

    except Exception as e:
        print(e)
