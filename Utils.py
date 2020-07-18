"""
This file contains util functions that are used in different python files.
The purpose of this file is to avoid duplicate code and unnecessary memory
allocation using different functions from the same file"""

import os
import simplejson as json
from requests import request


def get_api_call_response(url, headers, querystring=None):
    """ function that returns a response of an API call"""
    if querystring is None:
        return request('GET', url, headers=headers)
    return request('GET', url, headers=headers, params=querystring)


def read_json_file(response_file):
    """Function that opens and reads a json file after validate it"""
    if os.path.isfile(response_file) and os.stat(response_file).st_size != 0:
        try:
            print("Read JSON from path: {}".format(response_file))
            with open(str(response_file), 'r', encoding="utf-8") as input_json:
                inp_data = input_json.read()
                inp_data = json.loads(inp_data)
                return inp_data
        except Exception as err_error:
            print(err_error)
            return ""
    else:
        print("File not found under: {}".format(response_file))
        return ""


def read_csv_specific_column(input_file, column_index):
    """Function that reads specific column from csv file and return a list"""
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
        except Exception as error_e:
            return str(error_e)
    else:
        print("NO SUCH FILE OR DIRECTORY!\n\t", input_file)
        return ""


if __name__ == '__main__':
    TEST_JSON = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\quotes.json'
    TEST_CSV_GEO = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\Geo_code.csv'
    TEST_CSV_CITY = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\City.csv'
    print(json.dumps(read_json_file(TEST_JSON), indent=2))
    print(read_csv_specific_column(TEST_CSV_GEO, 2))
    print(read_csv_specific_column(TEST_CSV_CITY, 1))
    print(read_csv_specific_column(TEST_CSV_CITY, 0))
