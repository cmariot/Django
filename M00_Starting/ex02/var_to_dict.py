def var_to_dict():

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

    dict = {}

    for elem in d:

        if len(elem) != 2:
            raise Exception("Tuple must have 2 elements")
        value, key = elem
        dict[key] = value

    return dict


def print_dict(dict):
    for key, value in dict.items():
        print(f"{key} : {value}")


if __name__ == '__main__':
    try:
        dict = var_to_dict()
        print_dict(dict)
    except Exception as e:
        print(e)
