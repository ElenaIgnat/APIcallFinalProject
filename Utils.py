import functools
import os
import simplejson as json
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


def read_json_file(response_file):
    if os.path.isfile(response_file) and os.stat(response_file).st_size != 0:
        try:
            print("Read JSON from path: {}".format(response_file))
            with open(str(response_file), 'r', encoding="utf-8") as input_json:
                inp_data = input_json.read()
                inp_data = json.loads(inp_data)
                return inp_data
        except Exception as e:
            print(e)
            return ""
    else:
        print("File not found under: {}".format(response_file))
        return ""


def read_csv_specific_column(input_file, column_index):
    """Read specific column from csv file and return a list"""
    if os.path.isfile(input_file) and os.stat(input_file).st_size != 0:
        try:
            with open('{}'.format(input_file), 'r') as csv_read:
                csv_reader = csv_read.read().splitlines()
                # remove the first line with headers
                del csv_reader[0]
                column_list = []
                for line in csv_reader:
                    line = line.split(",")
                    if line[column_index] == "":
                        continue
                    column_list.append(line[column_index])
            return column_list
        except Exception as e:
            return str(e)
    else:
        print("NO SUCH FILE OR DIRECTORY!\n\t", input_file)
        return ""


if __name__ == '__main__':
    test_json = r'C:\Users\elena\PycharmProjects\API_call_project\ResorceFiles\quotes.json'
    test_csv = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\Geo_code.csv'
    print(json.dumps(read_json_file(test_json), indent=2))
    print(read_csv_specific_column(test_csv, 2))

