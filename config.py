""" config.py ? Loads runtime configuration """

import yaml

def get_config():
    with open("./config/config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
