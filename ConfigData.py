import os
import json

CONFIGFILE = 'config.json'
PROJECT_DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))
GEO_URL = 'geo_url'
GEO_RAPIDAPI_HOST = 'geo-rapidapi-host'
SCANNER_URL = 'scanner_url'
SCANNER_RAPIDAPI_HOST = 'scanner-rapidapi-host'
X_RAPIDAPI_KEY = 'x_rapidapi_key'
QUOTES_JSON = 'quotes_json'
CITY_CSV = 'city_csv'
GEO_CODE_CSV = 'geo_code_csv'


class ConfigData:
    config = None

    @staticmethod
    def get_instance():
        """
        Verifies if an instance is already created, otherwise create one and store it,
        to avoid multiple reads of the same file
        :return: ConfigData.config instance
        """
        if not ConfigData.config:
            ConfigData.config = ConfigData()
        return ConfigData.config

    def __init__(self):
        self.param_dict = {}
        self.config_file = os.path.join(PROJECT_DIRECTORY_PATH, CONFIGFILE)
        self.read_from_config_file()

    def read_from_config_file(self):
        if os.path.isfile(self.config_file) and os.stat(self.config_file).st_size != 0:
            try:
                # read config file and load the content as a json object
                with open(self.config_file) as f:
                    data = json.load(f)
                    for item in data['config']['url_servers']['geo_api']:
                        self.param_dict.update(item)
                    for item in data['config']['url_servers']['scanner_api']:
                        self.param_dict.update(item)
                    for item in data['config']['authenticator']:
                        self.param_dict.update(item)
                    for item in data['config']['files']:
                        self.param_dict.update(item)
                return self.param_dict
            except Exception as e:
                return str(e)
        else:
            print("File {} not found".format(CONFIGFILE))
        return ""

    def get_value(self, param):
        if self.param_dict.__contains__(param):
            return self.param_dict[param]
        else:
            print(f"Parameter {param} not found!")
            return ""


if __name__ == '__main__':
    config_data = ConfigData().get_instance()
    second_instance = ConfigData().get_instance()
    print(config_data == second_instance)
    print(ConfigData().config_file)
    print(ConfigData().get_value(GEO_URL))
    dict_values = ConfigData().read_from_config_file()
    for item in dict_values.items():
        print(item)

