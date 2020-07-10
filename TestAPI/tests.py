r"""
run suite test command line example:
python -m pytest TestAPI\tests.py -vv --durations=0
#pytest --durations=0 — Show all times for tests and setup and teardown;
#pytest --durations=1 — Just show me the slowest
#pytest --durations=50 — Slowest 50, with times

run a single test command line example:
python -m pytest TestAPI\tests.py::test_geo_db_data -v
"""
import os
import logging
from datetime import datetime
import Utils as utils
import ConfigData as cd
from API_Calls import CollectJSONdata as jsonData


config_data = cd.ConfigData.get_instance()
quotes_json = os.path.join(cd.PROJECT_DIRECTORY_PATH, config_data.get_value(cd.QUOTES_JSON))
expected_csv_values = os.path.join(cd.PROJECT_DIRECTORY_PATH, config_data.get_value(cd.GEO_CODE_CSV))
expected_sky_scanner_values = os.path.join(cd.PROJECT_DIRECTORY_PATH, config_data.get_value(cd.CITY_CSV))

FILE_DATE = datetime.now().strftime("%Y%m%d-%H%M%S")
logging.basicConfig(level=logging.DEBUG,
                    filename=f'tests_{FILE_DATE}.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def test_geo_db_data():
    logging.info(f'Running Test: {test_geo_db_data.__name__}')
    actual_results = jsonData.get_geo_db_data()
    expected_results = utils.read_csv_specific_column(expected_csv_values, 0)
    logging.info(f'Test {test_geo_db_data.__name__} status: {actual_results == expected_results}')
    assert actual_results != expected_results


def test_geo_db_links():
    logging.info(f'Running Test: {test_geo_db_links.__name__}')
    actual_results = jsonData.get_geo_db_links()
    expected_results = utils.read_csv_specific_column(expected_csv_values, 1)
    logging.info(f'Test {test_geo_db_links.__name__} status: {len(actual_results) == len(expected_results)}')
    assert len(actual_results) == len(expected_results)


def test_geo_db_total_count():
    logging.info(f'Running Test: {test_geo_db_total_count.__name__}')
    actual_results = jsonData.get_geo_db_total_count()
    expected_results = utils.read_csv_specific_column(expected_csv_values, 2)
    logging.info(f'Test {test_geo_db_total_count.__name__} status: {actual_results != expected_results}')
    assert actual_results != expected_results


def test_quotes_language():
    logging.info(f'Running Test: {test_quotes_language.__name__}')
    actual_results = jsonData.get_quotes_language()
    expected_results = ['fr', 'en', 'es', 'it']
    logging.info(f'Test {test_quotes_language.__name__} status: {actual_results == expected_results}')
    for item in range(len(expected_results)):
        assert actual_results[item] == expected_results[item]


def test_sky_scanner_city_id():
    logging.info(f'Running Test: {test_sky_scanner_city_id.__name__}')
    actual_place_id = jsonData.get_sky_scanner_place_id()
    expected_place_id = utils.read_csv_specific_column(expected_sky_scanner_values, 1)
    logging.info(f'Test {test_quotes_language.__name__} status: {actual_place_id == expected_place_id}')
    for item in range(len(expected_place_id)):
        assert actual_place_id[item] == expected_place_id[item]


def test_sky_scanner_place_name():
    logging.info(f'Running Test: {test_sky_scanner_place_name.__name__}')
    actual_place_name = jsonData.get_sky_scanner_place_name()
    expected_place_name = utils.read_csv_specific_column(expected_sky_scanner_values, 0)
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

