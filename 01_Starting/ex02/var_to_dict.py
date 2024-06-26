def var_to_dict(d):
    """
    Return a dictionary with a year as key and a set of string as value.
    """
    dict = {}
    for key, value in d:
        if value not in dict:
            dict[value] = set()
        dict[value].add(key)
    return dict


def print_dict(dict):
    for year, set_of_value in dict.items():
        print(f"{year} : {' '.join(set_of_value)}")


if __name__ == '__main__':
    try:

        d = [
            ('Hendrix', '1942'),
            ('Allman', '1946'),
            ('King', '1925'),
            ('Clapton', '1945'),
            ('Johnson', '1911'),
            ('Berry', '1926'),
            ('Vaughan', '1954'),
            ('Cooder', '1947'),
            ('Page', '1944'),
            ('Richards', '1943'),
            ('Hammett', '1962'),
            ('Cobain', '1967'),
            ('Garcia', '1942'),
            ('Beck', '1944'),
            ('Santana', '1947'),
            ('Ramone', '1948'),
            ('White', '1975'),
            ('Frusciante', '1970'),
            ('Thompson', '1949'),
            ('Burton', '1939')
        ]

        dict = var_to_dict(d)
        print_dict(dict)

    except Exception as e:
        print(e)
