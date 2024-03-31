def var_to_dict(d):
    dict = {}
    for key, value in d:
        if value in dict:
            dict[value].append(key)
        else:
            dict[value] = [key]
    return dict


def print_dict(dict):
    for key, value in dict.items():
        print(f"{key} : {' '.join(value)}")


if __name__ == '__main__':
    try:

        d = [
            ('Hendrix', '1942'),
            ('Allman', '1946'),  # cSpell:ignore Allman
            ('King', '1925'),
            ('Clapton', '1945'),
            ('Johnson', '1911'),
            ('Berry', '1926'),
            ('Vaughan', '1954'),
            ('Cooder', '1947'),  # cSpell:ignore Cooder
            ('Page', '1944'),
            ('Richards', '1943'),
            ('Hammett', '1962'),
            ('Cobain', '1967'),
            ('Garcia', '1942'),
            ('Beck', '1944'),
            ('Santana', '1947'),  # cSpell:ignore Ramone
            ('Ramone', '1948'),  # cSpell:ignore Ramone
            ('White', '1975'),
            ('Frusciante', '1970'),  # cSpell:ignore Frusciante
            ('Thompson', '1949'),
            ('Burton', '1939')
        ]

        dict = var_to_dict(d)
        print_dict(dict)

    except Exception as e:
        print(e)
