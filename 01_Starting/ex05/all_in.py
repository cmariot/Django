import sys


def parse_argument():

    """
    Get the argument of the program and split it by the commas
    Return a list of capitals/states
    """

    if len(sys.argv) != 2:
        exit()

    i = 0
    elements = []
    splitted_arg = sys.argv[1].split(",")

    for elem in splitted_arg:

        # Two ',' -> exit
        if len(elem) == 0 and i != len(splitted_arg) - 1:
            exit()

        stripped_elem = elem.strip()

        if len(stripped_elem) != 0:
            elements.append(stripped_elem)

        i += 1

    return elements


def get_state(city_input, states, capital_cities):
    """
    Search for the state of a capital city.
    """

    # Search for the state of the capital city by value
    abbreviation = None
    for state_abbr, capital_name in capital_cities.items():
        if capital_name.upper() == city_input.upper():
            abbreviation = state_abbr
            capital_city_correct = capital_name
            break

    if abbreviation is None:
        return False, None, None

    # Search for the state name by it's abbreviation
    state_name = None
    for state, state_abbr in states.items():
        if state_abbr.upper() == abbreviation.upper():
            state_name = state
            break

    if state_name is None:
        return False, None, None

    return True, state_name, capital_city_correct


def get_capital(state_input, states, capital_cities):

    """
    Search for the capital city of a state.
    """

    # Search for the abbreviation of the state
    abbreviation = None
    for state, state_abbr in states.items():
        if state.upper() == state_input.upper():
            abbreviation = state_abbr
            state_correct = state
            break

    if abbreviation is None:
        return False, None, None

    # Search for the capital city of the state
    capital_city = None
    for state_abbr, capital_name in capital_cities.items():
        if state_abbr.upper() == abbreviation.upper():
            capital_city = capital_name
            break

    if capital_city is None:
        return False, None, None

    return True, state_correct, capital_city


if __name__ == '__main__':
    try:

        elements = parse_argument()

        states = {
            "Oregon": "OR",
            "Alabama": "AL",
            "New Jersey": "NJ",
            "Colorado": "CO"
        }

        capital_cities = {
            "OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"
        }

        for elem in elements:

            # If the element is a capital city, we get the state
            is_a_capital_city, state, capital_city = get_state(
                elem, states, capital_cities
            )
            if is_a_capital_city:
                print(f"{capital_city} is the capital of {state}")
                continue

            # If the element is a state, we get the capital city
            is_a_state, state, capital_city = get_capital(
                elem, states, capital_cities
            )
            if is_a_state:
                print(f"{capital_city} is the capital of {state}")
                continue

            # If the element is neither a capital city nor a state
            print(f"{elem} is neither a capital city nor a state")

    except Exception as e:
        print(e)
