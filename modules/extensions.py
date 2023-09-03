"""Module containing shared helper functions"""

import json


with open("module_config.json", "r") as json_file:
    config = json.load(json_file)
