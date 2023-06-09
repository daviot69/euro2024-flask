import yaml
from definitions import CONFIG_PATH


def get_config():
    config_path = CONFIG_PATH / "config.yaml"

    try:
        with open(config_path, "r") as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        return {}
