"""The file contains the function responsible for configuration loading.
"""
from pathlib import Path
import yaml

__all__ = ('upload_config',)


def upload_config(cfg_file=None):
    """The function which uploads a config from whether the default config-file nor passed config-file.
    :param cfg_file: passed config-file.
    :return: config-dict.
    """
    # Set the default path to the configuration file.
    # Technically this path looks like <root directory>/config.yaml
    default_file = Path(__file__).parent.parent.parent / 'config.yaml'

    # Using PyYaml read the configuration file and store to to the dict.
    with open(default_file, 'r') as f:
        config = yaml.safe_load(f)

    # In the case an user passed custom configuration file. Read it and update the default one.
    cfg_dict = {}
    # if custom configuration file exists then upload the config as dict.
    if cfg_file:
        cfg_dict = yaml.safe_load(cfg_file)

    # if dict doesn't empty then update the main config.
    if cfg_dict:
        config.update(**cfg_dict)

    return config
