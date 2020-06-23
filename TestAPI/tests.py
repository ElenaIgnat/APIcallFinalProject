r"""python -m pytest C:\Users\elena\PycharmProjects\API_call_project\TestAPI\tests.py -v"""

import logging
import Utils as utils
from datetime import datetime
from API_Calls import CollectJSONdata as jsonData

expected_csv_values = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\Geo_code.csv'
expected_sky_scanner_values = r'C:\Users\elena\PycharmProjects\API_call_project\ResourceFiles\City.csv'

file_date = datetime.now().strftime("%Y%m%d-%H%M%S")
logging.basicConfig(level=logging.INFO,
                    filename=f'tests_{file_date}.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m-%d-%Y %I:%M:%S %p')


def test_geo_db_data():
    logging.info(f'Regression Test: {test_geo_db_data.__name__}')
    actual_results = jsonData.get_geo_db_data()
    logging.info(f'{test_geo_db_data.__name__} api call actual results: {actual_results}')
    expected_results = utils.read_csv_specific_column(expected_csv_values, 0)
    logging.info(f'{test_geo_db_data.__name__} api call expected results: {expected_results}')
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
    actual_results = jsonData.get_quotes_language()
    expected_results = ['fr', 'en', 'es', 'it']
    for item in range(len(expected_results)):
        assert actual_results[item] == expected_results[item]


def test_sky_scanner_city_id():
    actual_place_id = jsonData.get_sky_scanner_place_id()
    expected_place_id = utils.read_csv_specific_column(expected_sky_scanner_values, 1)
    for item in range(len(expected_place_id)):
        assert actual_place_id[item] == expected_place_id[item]


def test_sky_scanner_place_name():
    pass


if __name__ == '__main__':
    test_quotes_language()

