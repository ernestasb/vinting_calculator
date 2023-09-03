"""Module containing shared helper functions"""

import json

# this file is created to define custom code snipets that can be used in the application
with open("module_config.json", "r", encoding="UTF-8") as json_file:
    config = json.load(json_file)
