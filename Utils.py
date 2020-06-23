import functools
from requests import request
from timeit import default_timer as timer


def get_api_call_response(url, headers, querystring=None):

    if querystring is None:
        return request('GET', url, headers=headers)
    return request('GET', url, headers=headers, params=querystring)


def request_duration(input_function):
    @functools.wraps(input_function)
    def new_function(*args, **kwargs):
        start_time = timer()
        value = input_function(*args, **kwargs)
        end_time = timer()
        duration = end_time - start_time
        print("\n{} method duration: {:.3f}".format(input_function.__name__, duration))
        return value
    return new_function

