import configparser
import sys
def get_config(config_section):
    config = configparser.ConfigParser()
    config.read(['config.ini', './config.ini', '../config.ini'])
    if config_section not in config or config[config_section] == "":
        sys.stderr.write("Could not find the section in the config.ini file", config_section)  
    return config[config_section]