# -*- coding: utf-8 -*-
from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

packages = \
['fastapi_cli',
 'fastapi_cli.templates',
 'fastapi_cli.templates.app',
 'fastapi_cli.templates.app.hooks',
 'fastapi_cli.templates.project',
 'fastapi_cli.templates.project.hooks',
]

package_data = \
{'': ['*'],
 'fastapi_cli.templates.project': ['{{ cookiecutter.folder_name }}/*']}

install_requires = \
['bullet>=2.2.0,<3.0.0',
 'cookiecutter>=1.7.2,<2.0.0',
 'pydantic[email]>=1.7.2,<2.0.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['fastapi = fastapi_cli.main:app']}


setup_kwargs = {
    'name': 'fastapi-cli-service',
    'version': '1.0.1',
    'description': 'Managing FastAPI projects made easy.',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'author': 'liangshihua',
    'author_email': 'shxh.liang@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sxhxliang/fastapi-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
