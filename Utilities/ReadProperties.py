import configparser
import os

#use to read the configuration files without hardcoding the values
#change the values in the config.ini file to change the values in the test cases

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        config = configparser.RawConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../Configuration/config.ini'))
        return config.get('common info', 'baseURL')

    @staticmethod
    def getUserName():
        config = configparser.RawConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../Configuration/config.ini'))
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        config = configparser.RawConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../Configuration/config.ini'))
        return config.get('common info', 'password')
    