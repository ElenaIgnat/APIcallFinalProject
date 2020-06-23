r"""python -m pytest C:\Users\elena\PycharmProjects\API_call_project\TestAPI\tests.py -v"""

from API_Calls import CollectJSONdata as jsonData
import logging
from datetime import datetime

file_date = datetime.now().strftime("%Y%m%d-%H%M%S")
logging.basicConfig(level=logging.INFO,
                    filename=f'tests_{file_date}.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m-%d-%Y %I:%M:%S %p')


def test_geo_db_data():
    logging.info(f'Regression Test: {test_geo_db_data.__name__}')
    actual_results = jsonData.get_geo_db_data()
    logging.info(f'{test_geo_db_data.__name__} api call actual results: {actual_results}')
    expected_results = ['nn', 'ar_JO', 'bg', 'kea', 'nds']
    logging.info(f'{test_geo_db_data.__name__} api call expected results: {expected_results}')
    logging.info(f'Test {test_geo_db_data.__name__} status: {actual_results == expected_results}')
    assert actual_results == expected_results


def test_geo_db_links():
    logging.info(f'Regression Test: {test_geo_db_links.__name__}')
    actual_results = jsonData.get_geo_db_links()
    expected_results = ['/v1/locale/locales?offset=0&limit=5',
                        '/v1/locale/locales?offset=5&limit=5',
                        '/v1/locale/locales?offset=745&limit=5']
    logging.info(f'Test {test_geo_db_links.__name__} status: {len(actual_results) == len(expected_results)}')
    assert len(actual_results) == len(expected_results)


def test_geo_db_total_count():
    logging.info(f'Regression Test: {test_geo_db_total_count.__name__}')
    actual_results = jsonData.get_geo_db_total_count()
    logging.warning(f'actual_results = {actual_results}')
    expected_results = 743
    logging.info(f'Test {test_geo_db_total_count.__name__} status: {actual_results != expected_results}')
    assert actual_results != expected_results


# def test_quotes_language():
#     actual_results = jsonData.get_quotes_language()
#     expected_results = ['fr', 'en', 'es', 'it']
#     for item in range(len(expected_results)):
#         assert actual_results[item] == expected_results[item]


