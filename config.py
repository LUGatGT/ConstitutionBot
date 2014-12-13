import json
import re

def _config():
    """
    Returnsa map of the required configuration keys, and a compiled regex
    matcher to verify their values.
    """

    return {
        # Map that holds metadata on the repository we are monitoring.
        "repository": {
            # The name of the repository we are monitoring.
            "name": re.compile(".*"),
            # The handle of group/user that owns the repository.
            "owner": re.compile(".*"),
            # Holds metadata on the three branches that should exist in the reposository.
            "branch": {
                # The name of the branch that represents the senate.
                "senate": re.compile(".*"),
                # The name of the branch that represents the house.
                "house": re.compile(".*"),
                # The name of the branch that represents the president.
                "president": re.compile(".*")
            }
        },
        "user": {
            "token": re.compile("[0123456789abcdef]*"),
            "handle": re.compile(".*")
        }
    }

def _verify_good(config, config_map = _config()):
    """
    Takes in a configuration for this bot, and throws an exception if
    the configuration file is missing required optionss
    """
    print(config_map)
    for key, value in config_map.items():
        try:
            print(key)
            config[key]

        except:
            return False

        if type(value) is dict:
            return _verify_good(config[key], config_map = value)

        elif not value.match(config[key]):
            return False

    return True


def default_config():
    """
    Returns the default configuration.
    """

    def copy_submaps(value):
        if type(value) is dict:
            return {k: copy_submaps(v) for k, v in value.items()}
        else:
            return ""

    return copy_submaps(_config())

class BadConfiguration(Exception):
    pass

def parse(config_file):


    config = {}
    bad_config = False
    try:
        config = json.load(open(config_file))
    except:
        bad_config = True

    if not _verify_good(config):
        bad_config = True
    if bad_config:
        raise BadConfiguration("Bad configuration detected. To print out a "
                               + "default configuration, use the -c flag")

    return config

def print(config):
    return json.dumps(config, sort_keys=True, indent=4, separators=(",", ": "))
