r"""
run suite test command line example:
python -m pytest C:\Users\elena\PycharmProjects\API_call_project\TestAPI\tests.py -v
run a single test command line example:
python -m pytest C:\Users\elena\PycharmProjects\API_call_project\TestAPI\tests.py::test_geo_db_
data
"""

import logging
import Utils as utils
from datetime import datetime
from API_Calls import CollectJSONdata as jsonData

quotes_json = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\quotes.json'
expected_csv_values = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\Geo_code.csv'
expected_sky_scanner_values = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\City.csv'

file_date = datetime.now().strftime("%Y%m%d-%H%M%S")
logging.basicConfig(level=logging.DEBUG,
                    filename=f'tests_{file_date}.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m-%d-%Y %I:%M:%S %p')


def test_geo_db_data():
    logging.info(f'Regression Test: {test_geo_db_data.__name__}')
    actual_results = jsonData.get_geo_db_data()
    logging.info(f'Actual results {actual_results}:')
    expected_results = utils.read_csv_specific_column(expected_csv_values, 0)
    logging.info(f'Expected results {expected_results}:')
    logging.info(f'Test {test_geo_db_data.__name__} status: {actual_results == expected_results}')
    assert actual_results == expected_results


def test_geo_db_links():
    logging.info(f'Regression Test: {test_geo_db_links.__name__}')
    actual_results = jsonData.get_geo_db_links()
    expected_results = utils.read_csv_specific_column(expected_csv_values, 1)
    logging.info(f'Test {test_geo_db_links.__name__} status: {len(actual_results) == len(expected_results)}')
    assert len(actual_results) == len(expected_results)


def test_geo_db_total_count():
    logging.info(f'Regression Test: {test_geo_db_total_count.__name__}')
    actual_results = jsonData.get_geo_db_total_count()
    logging.warning(f'actual_results = {actual_results}')
    expected_results = utils.read_csv_specific_column(expected_csv_values, 2)
    logging.info(f'Test {test_geo_db_total_count.__name__} status: {actual_results != expected_results}')
    assert actual_results != expected_results


def test_quotes_language():
    logging.info(f'Regression Test: {test_quotes_language.__name__}')
    actual_results = jsonData.get_quotes_language()
    logging.info(f'{test_quotes_language.__name__} api call actual results: {actual_results}')
    expected_results = ['fr', 'en', 'es', 'it']
    logging.info(f'{test_quotes_language.__name__} api call expected results: {expected_results}')
    logging.info(f'Test {test_quotes_language.__name__} status: {actual_results == expected_results}')
    for item in range(len(expected_results)):
        assert actual_results[item] == expected_results[item]


def test_sky_scanner_city_id():
    logging.info(f'Regression Test: {test_sky_scanner_city_id.__name__}')
    actual_place_id = jsonData.get_sky_scanner_place_id()
    logging.info(f'{test_sky_scanner_city_id.__name__} api call actual results: {actual_place_id}')
    expected_place_id = utils.read_csv_specific_column(expected_sky_scanner_values, 1)
    logging.info(f'{test_sky_scanner_city_id.__name__} api call expected results: {expected_place_id}')
    logging.info(f'Test {test_quotes_language.__name__} status: {actual_place_id == expected_place_id}')
    for item in range(len(expected_place_id)):
        assert actual_place_id[item] == expected_place_id[item]


def test_sky_scanner_place_name():
    logging.info(f'Regression Test: {test_sky_scanner_place_name.__name__}')
    actual_place_name = jsonData.get_sky_scanner_place_name()
    logging.debug(f'{test_sky_scanner_place_name.__name__} api call actual results: {actual_place_name}')
    expected_place_name = utils.read_csv_specific_column(expected_sky_scanner_values, 0)
    logging.debug(f'{test_sky_scanner_place_name.__name__} api call expected results: {expected_place_name}')
    logging.debug(f'Test {test_quotes_language.__name__} status: {actual_place_name == expected_place_name}')
    for item in range(len(expected_place_name)):
        assert actual_place_name[item] == expected_place_name[item]


if __name__ == '__main__':
    test_quotes_language()
    # test_sky_scanner_city_id()
    # test_sky_scanner_place_name()
    # test_geo_db_data()
    # test_geo_db_links()
    # test_geo_db_total_count()

