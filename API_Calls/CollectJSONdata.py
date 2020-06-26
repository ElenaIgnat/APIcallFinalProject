"""THe purpose of this file is to gather qpi calls json data and store them
in specific data structures such asa lists or dictionaries"""
import Utils as utils
from API_Calls import Requests_API_call as ApiCalls

geo_data = ApiCalls.geo_api()
city_data = ApiCalls.sky_scanner()
quotes_json = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\quotes.json'


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


@utils.request_duration
def get_quotes_language():
    json_data = utils.read_json_file(quotes_json)
    return [key for key in json_data.keys()]


def get_sky_scanner_place_id():
    return [item['PlaceId'] for item in city_data['Places']]


def get_sky_scanner_place_name():
    return [item['PlaceName'] for item in city_data['Places']]


if __name__ == '__main__':
    print(get_geo_db_data())
    # print(get_geo_db_links())
    # print(get_geo_db_total_count())
    #
    # print(get_quotes_language())
    #
    # print(get_sky_scanner_place_name())
    # print(get_sky_scanner_place_id())

