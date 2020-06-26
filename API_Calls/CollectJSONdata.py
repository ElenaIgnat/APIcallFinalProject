"""THe purpose of this file is to gather qpi calls json data and store them
in specific data structures such asa lists or dictionaries"""
import os
import Utils as utils
import ConfigData as cd
from API_Calls import Requests_API_call as ApiCalls

# Get a single instance of the ConfigData class
config_data = cd.ConfigData().get_instance()

# Create dynamic path for current_json
current_json = os.path.join(cd.PROJECT_DIRECTORY_PATH, config_data.get_value(cd.QUOTES_JSON))

geo_data = ApiCalls.geo_api()
city_data = ApiCalls.sky_scanner()


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
    """read from local json file and key values in a list"""
    json_data = utils.read_json_file(current_json)
    print(json_data)
    return [key for key in json_data.keys()]


def get_sky_scanner_place_id():
    return [item['PlaceId'] for item in city_data['Places']]


def get_sky_scanner_place_name():
    return [item['PlaceName'] for item in city_data['Places']]


if __name__ == '__main__':
    print(get_geo_db_data())
    # print(current_json)
    # print(get_geo_db_links())
    # print(get_geo_db_total_count())

    # print(get_quotes_language())

    # print(get_sky_scanner_place_name())
    # print(get_sky_scanner_place_id())


