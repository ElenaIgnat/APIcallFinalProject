import sys
import random
from math import sqrt as sqrt


def main():

    """------------------List slice/split/obtain last_item---------"""
    # convert string into a list
    players = 'player_one, player_two, player_three, player_four'
    players_list = players.split()
    last_list_item = players_list[2]
    print(last_list_item)
    second_item_from_the_EOL = players_list[-2]
    print(second_item_from_the_EOL)
    slice_elements = players_list[0:2]
    print(slice_elements)


    """------------------List append/insert/pop/sort/sorted/reverse/remove/del---------"""
    list_numbers = [3, 6, 2, 13, 1, 99, 100]
    print('initial list\n' + str(list_numbers))
    # add element into the list on the last position
    list_numbers.append(101)
    print("Add element at the end of the list\n" + str(list_numbers))
    list_numbers.sort(reverse=True)
    print('Reverse the list\n' + str(list_numbers))
    # delete the last element on the list
    list_numbers.pop()
    print("Remover last element in a list\n" + str(list_numbers))
    # add element on the list at a specific position
    list_numbers.insert(2, 50)
    print('Insert element at a specific position\n' + str(list_numbers))

    # for a temporary sorted list we can use sorted method
    print("temporally sorted list in descending order\n:", str(sorted(list_numbers, reverse=True)))


    # display 5 elements from the list
    print('Display first 5 element of the list\n' + str(list_numbers[0:4]))
    # delete an item of a list by position index
    del list_numbers[0]
    print('Removed "1" item using del\n' + str(list_numbers))
    # remove accepts the value(int or str type) of the item and not the index
    list_numbers.remove(99)
    print('Delete item "99" using remove method\n' + str(list_numbers))


    """------------------extend/min/max/sum of elements---------"""
    list_numbers_2 = [45, 21, 87, 36, 27]
    print('List number 2\n' + str(list_numbers_2))
    # merge 2 lists
    list_numbers.extend(list_numbers_2)
    print('Bind list one with list two in one single list\n' + str(list_numbers))
    list_numbers.sort(reverse=True)
    print('Apply reverse method\n' + str(list_numbers))
    # return the maximum value from a list
    max_value = max(list_numbers)
    print('maximum value: ' + str(max_value))
    # return the minimum value from a list
    min_value = min(list_numbers)
    print('minimum value: ' + str(min_value))
    # make a sum of the entire values of the list
    sum_list = sum(list_numbers)
    print('sum of the entire value of the list: ' + str(sum_list))


    """-------------------retrieve the position of a specific value from the list------------"""
    list_seasons = ["summer", "spring", "winter", "autumn"]
    print('retrieve the position of spring element from the seasons list: ' + str(list_seasons.index('spring')))
    # return random value from a list using choice function
    random_value = random.choice(list_seasons)
    print('Extracted random value from season list: ' + str(random_value))
    print("Seasons list\n" + str(list_seasons))
    sorted_seasons = sorted(list_seasons)
    print('Sorted seasons\n' + str(sorted_seasons))

    """-----------------------transform a list in a string using join-----------------------"""
    seasons_str = ','.join(list_seasons)
    print('Convert list in to one string = ' + str(seasons_str))

    """-----------------------custom format the list into desired pattern---------------"""
    custom_list = [x.capitalize().replace('e', '3') for x in list_seasons]
    print('Custom format list:\n' + str(custom_list))
    # remove quotes from the final list and convert into a str
    custom_list_1 = ', '.join(map(str, custom_list))
    print('Convert list items into a string:\n' + custom_list_1)

    # check if a value is present in a specific list
    print('Check {} is present in list = '.format('spring') + str('spring' in list_seasons))


    """----------------------Iteration protocols over the list-----------------"""
    seasons = ['winter', 'spring', 'summer', 'autumn']


if __name__ == '__main__':
    main()

