import random


def main():
    """------------------List slice/split/obtain last_item---------"""
    # convert a string type into a list type
    players = 'player_one, player_two, player_three, player_four'
    print(type(players), 'players list:\t', players)
    players_list = players.split()
    print(type(players_list), 'players_list :\t', players_list)

    # list slice example
    last_item = players_list[3]
    print("\nList last element:\t", last_item)

    # list slice example with negative index
    second_item = players_list[-3]
    print('second item from the EOL:\t', second_item)

    # slice a lists in a interval index
    slice_elements = players_list[0:2]
    print('slice elements of a list:\t', slice_elements)

    """------------------List append/insert/pop/sort/sorted/reverse/remove/del---------"""
    list_numbers = [3, 6, 2, 13, 1, 99, 100]
    print('\ninitial list:\t', list_numbers)
    # add element into the list on the last position
    list_numbers.append(101)
    print("updated list:\t" + str(list_numbers))

    # sort the list in decreasing order
    list_numbers.sort(reverse=True)
    print('\nReverse list:\t' + str(list_numbers))

    # delete the last element of the list
    list_numbers.pop()
    print("Remove last element in a list:\t", list_numbers)

    # add element to the list at a specific position
    list_numbers.insert(2, 50)
    print('Insert element at a specific position:\t', list_numbers)

    # makes a permanent modification of the list
    list_numbers.sort()
    print('\npermanent sorted list_numbers in asc order:\t', list_numbers)

    # for a temporary sorted list we can use sorted method
    print("temporally sorted list in desc order\t:", sorted(list_numbers, reverse=True))

    # delete an item of a list by position index
    del list_numbers[0]
    print('\nRemoved "1" item using del:\t' + str(list_numbers))

    # remove accepts the value(int or str type) of the item and not the index
    list_numbers.remove(99)
    print('Delete item "99" using remove method:\t', list_numbers)

    """------------------extend/min/max/sum of elements---------"""
    # create a new list
    list_numbers_2 = [45, 21, 87, 36, 27]
    print('\nList number 2:\t', list_numbers_2)

    # merge 2 lists
    list_numbers.extend(list_numbers_2)
    print('Merge list_numbers with list_numbers_ in one single list:\t', list_numbers)

    # sort the list in descending order
    list_numbers.sort(reverse=True)
    print('Apply reverse method:\t', list_numbers)

    # return the maximum value from a list
    max_value = max(list_numbers)
    print('maximum value:\t', max_value)

    # return the minimum value from a list
    min_value = min(list_numbers)
    print('minimum value:\t', min_value)

    # obtain the sum of elem of the list
    sum_list = sum(list_numbers)
    print('sum of the entire value of the list:\t', sum_list)

    """-------------------retrieve the position of a specific value from the list------------"""
    list_seasons = ["summer", "spring", "winter", "autumn"]
    print('\nlist_seasons:\t', list_seasons)
    # Retrieve the position of spring element from the seasons list
    print('spring elem position:\t', list_seasons.index('spring'))

    # return random value from a list using choice function
    random_value = random.choice(list_seasons)
    print('list random value:\t', random_value)
    print("\nCurrent seasons list:\t", list_seasons)
    sorted_seasons = sorted(list_seasons)
    print('Sorted seasons list:\t', sorted_seasons)

    """-----------------------transform a list in a string using join-----------------------"""
    seasons_str = ','.join(list_seasons)
    print('\n', type(seasons_str), seasons_str)

    """-----------------------custom format the list into desired pattern---------------"""
    # Transform each elem of the list to start with capital letter and replace e with 3
    custom_list = [x.capitalize().replace('e', '3') for x in list_seasons]
    print('\nCustom format list:\t' + str(custom_list))

    # remove quotes from the final list and convert into a str
    custom_list_1 = ', '.join(map(str, custom_list))
    print('Convert list items into a string:\t' + custom_list_1)

    print('filter_even_numbers:\t', filter_even_numbers())


def filter_even_numbers():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x if not x % 2 in input_list else None, input_list))
    return even_numbers


if __name__ == '__main__':
    main()
