from igm.conf import igm_setup
from inquirer import inquire_func

igm_setup(
    name='simple',
    version='0.0.1',
    description='This is a simplest IGM template',
    inquire=inquire_func,
)
