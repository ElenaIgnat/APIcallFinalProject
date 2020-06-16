from requests import request
import json


def geo_db():
    url = "https://wft-geo-db.p.rapidapi.com/v1/locale/locales"

    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "07170cf1bfmsh75255af62dcbb94p1f8b04jsn83e66ae5964a"
    }

    response = request("GET", url, headers=headers)
    # data = json.dumps(response.json(), indent=2)
    data = json.loads(response.text)
    return data


def currency_exchange():
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"q": "1.0",
                   "from": "SGD",
                   "to": "MYR"}

    headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': "07170cf1bfmsh75255af62dcbb94p1f8b04jsn83e66ae5964a"
    }

    response_data = request("GET", url, headers=headers, params=querystring)

    return response_data.text


if __name__ == '__main__':
    print('-----------geo data response-----------------')
    print(geo_db()['data'][2])

    # print('\n-----------currency exchange rate response-----------------')
    # print(currency_exchange())
