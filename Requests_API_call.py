from requests import request
import json
import time
import logging

geo_url = "https://wft-geo-db.p.rapidapi.com/v1/locale/locales"
quotes_url = "https://quotes15.p.rapidapi.com/quotes/random/"
scanner_url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"
x_rapidapi_key = '07170cf1bfmsh75255af62dcbb94p1f8b04jsn83e66ae5964a'


def get_api_call_response(url, headers, querystring=None):

    if url == geo_url:
        return request('GET', url, headers=headers)
    return request('GET', url, headers=headers, params=querystring)


def geo_api():
    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
    }

    response = get_api_call_response(geo_url, headers)
    data = json.loads(response.text)
    return data


def quotes_api():
    """concatenate json response using querystring iteration list"""
    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
    }
    compose_json = {}
    querystring = [{"language_code": "fr"},
                   {"language_code": "en"},
                   {"language_code": "es"},
                   {"language_code": "it"}]

    for item in querystring:
        response_quote = get_api_call_response(quotes_url, headers, item)
        time.sleep(2)
        results = json.loads(response_quote.text)
        compose_json[item['language_code']] = results
    return compose_json


def sky_scanner():

    querystring = {"query": "Stockholm"}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
    }

    scanner = get_api_call_response(scanner_url, headers, querystring)
    scanner_content = json.loads(scanner.text)
    return scanner_content


if __name__ == '__main__':
    print(geo_api())
    # print('-----------quotes response-----------------')
    # print(json.dumps(quotes_api(), indent=2))

    # print('-----------flight data response-----------------')
    # # print(json.dumps(sky_scanner(), indent=2))
    # list_IDs = []
    # list_names = []
    # for item in sky_scanner()['Places']:
    #     list_IDs.append(item['PlaceId'])
    #     list_names.append(item['PlaceName'])
    # print(list_IDs)
    # print(list_names)
