from pprint import pprint


def main():
    country_iso_code = {'romania': 'RO',
                        'holland': 'AMS',
                        'france': 'FR',
                        'italy': 'IT',
                        'germany': 'de'}
    print("default dictionary:\n", country_iso_code)

    "-----------print keys of dict------------------"
    print('keys= ', country_iso_code.keys())

    "-----------print keys of dict------------------"
    print('values= ', country_iso_code.values())

    "-----------print items of dict------------------"
    print('items= ', country_iso_code.items())

    "-----------get a specific value for a key------------------"
    print('Value= ', country_iso_code['italy'])

    "-----------get value using get method------------------"
    print('Value with get method= ', country_iso_code.get('croatia'))

    "-----------add new item to the current dict------------------"
    country_iso_code['croatia'] = 'CR'
    print("updated dictionary:\n", country_iso_code)

    "-----------iterate a dict------------------"
    for key, value in country_iso_code.items():
        print('key= ' + key, ': value= ' + value)

    "-----------dict comprehension example------------------"
    countries = {key: value for key, value in country_iso_code.items()}
    pprint(countries)

    '--------------DELETE FROM DICT-------------------'
    print('BEFORE: ', country_iso_code)
    country_iso_code.pop('romania')
    print('AFTER:', country_iso_code)

    print('\nBEFORE: ', country_iso_code)
    del country_iso_code['italy']
    print('AFTER:', country_iso_code)


if __name__ == '__main__':
    main()

