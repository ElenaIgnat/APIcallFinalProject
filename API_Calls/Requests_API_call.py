import Utils as utils
import ConfigData as cd
import json

config_data = cd.ConfigData().get_instance()

geo_url = config_data.get_value(cd.GEO_URL)
scanner_url = config_data.get_value(cd.SCANNER_URL)
x_rapidapi_key = config_data.get_value(cd.X_RAPIDAPI_KEY)


def geo_api():
    headers = {
        'x-rapidapi-host': config_data.get_value(cd.GEO_RAPIDAPI_HOST),
        'x-rapidapi-key': x_rapidapi_key
    }

    response = utils.get_api_call_response(geo_url, headers)
    data = json.loads(response.text)
    return data


def sky_scanner():
    querystring = {"query": "Stockholm"}
    headers = {
        'x-rapidapi-host': config_data.get_value(cd.SCANNER_RAPIDAPI_HOST),
        'x-rapidapi-key': x_rapidapi_key
    }

    scanner = utils.get_api_call_response(scanner_url, headers, querystring)
    scanner_content = json.loads(scanner.text)
    return scanner_content


if __name__ == '__main__':
    print(json.dumps(geo_api(), indent=2))
    lista=[]
    for item in geo_api()['data']:
        lista.append(item['code'])
    [print(dict_val['code']) for dict_val in geo_api()['data']]
    # print('-----------flight data response-----------------')
    # print(json.dumps(sky_scanner(), indent=2))
    # list_IDs = []
    # list_names = []
    # for item in sky_scanner()['Places']:
    #     list_IDs.append(item['PlaceId'])
    #     list_names.append(item['PlaceName'])
    # print(list_IDs)
    # print(list_names)
