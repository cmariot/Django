def my_sort(d):

    # Create a dictionary with the year as key and a list of names as value
    grouped_by_year = {}
    for key, value in d.items():
        if value not in grouped_by_year:
            grouped_by_year[value] = [key]
        else:
            grouped_by_year[value].append(key)

    # Sort the dictionary by year
    sorted_dict = dict(sorted(grouped_by_year.items()))

    # Sort the names in each list and print them
    for key, value in sorted_dict.items():
        value.sort()
        for name in value:
            print(name)
            # print(key, name)


if __name__ == '__main__':
    try:
        d = {
            'Hendrix': '1942',
            'Allman': '1946',
            'King': '1925',
            'Clapton': '1945',
            'Johnson': '1911',
            'Berry': '1926',
            'Vaughan': '1954',
            'Cooder': '1947',
            'Page': '1944',
            'Richards': '1943',
            'Hammett': '1962',
            'Cobain': '1967',
            'Garcia': '1942',
            'Beck': '1944',
            'Santana': '1947',
            'Ramone': '1948',
            'White': '1975',
            'Frusciante': '1970',
            'Thompson': '1949',
            'Burton': '1939',
        }
        my_sort(d)
    except Exception as e:
        print(e)
