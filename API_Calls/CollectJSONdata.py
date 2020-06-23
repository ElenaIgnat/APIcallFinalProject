"""THe purpose of this file is to gather qpi calls json data and store them
in specific data structures such asa lists or dictionaries"""
from API_Calls import Requests_API_call as ApiCalls

geo_data = ApiCalls.geo_api()
quotes_data = ApiCalls.quotes_api()


def get_geo_db_data():
    """:returns: value_list for data dictionary from geo_db json"""
    value_list = []
    for item in geo_data['data']:
        value_list.append(item['code'])
    return value_list


def get_geo_db_links():
    """:returns: list of links from json"""

    links = []
    for item in geo_data['links']:
        links.append(item['href'])
    return links


def get_geo_db_total_count():
    """:returns: total count value from json"""
    return geo_data['metadata']['totalCount']


def get_quotes_language():
    language = [item for item in quotes_data.keys()]
    return language


if __name__ == '__main__':
    # print(get_geo_db_data())
    # print(get_geo_db_links())
    # print(get_geo_db_total_count())
    for item in range(len(get_quotes_language())):
        print(item)
