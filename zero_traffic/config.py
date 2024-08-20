
from .imports import * 
PATH_CONFIG = join(expanduser('~'), '.config', 'wrong-average.yaml')

CONFIG_TEMPLATE = """{'api_key': '<api key>',
'path_data_archive': '<path to project archive>',
'id_latlon': [['name1', 1, -1], ['name2', 1, -1], 
['name3', 1, -1]]}
"""


def write_template_config():
    """Write out a config template"""
    c = eval(CONFIG_TEMPLATE)
    with open(PATH_CONFIG, 'w') as f:
        yaml.dump(c, f, default_flow_style=False)
    print(f"wrote config template to '{PATH_CONFIG}'")


def check_config():
    if not exists(PATH_CONFIG):
        print(f"Need to have config @ '{PATH_CONFIG}'")
        a = input('setup config template? (y) > ')
        if a == 'y':
            write_template_config()
        else:
            print('doing nothing')


def load_config():
    check_config()
    with open(PATH_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    return config

