import Utils as utils
import json

geo_url = "https://wft-geo-db.p.rapidapi.com/v1/locale/locales"
scanner_url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"
x_rapidapi_key = '07170cf1bfmsh75255af62dcbb94p1f8b04jsn83e66ae5964a'


@utils.request_duration
def geo_api():
    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
    }

    response = utils.get_api_call_response(geo_url, headers)
    data = json.loads(response.text)
    return data


@utils.request_duration
def sky_scanner():
    querystring = {"query": "Stockholm"}
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
    }

    scanner = utils.get_api_call_response(scanner_url, headers, querystring)
    scanner_content = json.loads(scanner.text)
    return scanner_content


if __name__ == '__main__':
    # print(json.dumps(geo_api(), indent=2))

    # print('-----------flight data response-----------------')
    print(json.dumps(sky_scanner(), indent=2))
    # list_IDs = []
    # list_names = []
    # for item in sky_scanner()['Places']:
    #     list_IDs.append(item['PlaceId'])
    #     list_names.append(item['PlaceName'])
    # print(list_IDs)
    # print(list_names)
