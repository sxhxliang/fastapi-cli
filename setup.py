# -*- coding: utf-8 -*-
from setuptools import setup

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
    'name': 'fastapi-cli',
    'version': '1.0.0',
    'description': 'Managing FastAPI projects made easy.',
    'long_description': '<h3 align="center">\n    <strong>Manage FastAPI projects easily</strong>\n</h3>\n<p align="center">\n    <a href="https://github.com/sxhxliang/fastapi-cli" target="_blank">\n        <img src="https://img.shields.io/github/last-commit/ycd/fastapi-cli?style=for-the-badge" alt="Latest Commit">\n    </a>\n        <img src="https://img.shields.io/github/workflow/status/ycd/fastapi-cli/Test?style=for-the-badge">\n        <img src="https://img.shields.io/codecov/c/github/ycd/fastapi-cli?style=for-the-badge">\n    <br />\n    <a href="https://pypi.org/project/fastapi-cli" target="_blank">\n        <img src="https://img.shields.io/pypi/v/fastapi-cli?style=for-the-badge" alt="Package version">\n    </a>\n    <img src="https://img.shields.io/pypi/pyversions/fastapi-cli?style=for-the-badge">\n    <img src="https://img.shields.io/github/license/ycd/fastapi-cli?style=for-the-badge">\n</p>\n\n\n\n\n---\n\n**Source Code**: View it on [Github](https://github.com/sxhxliang/fastapi-cli/)\n\n---\n\n<a href="https://asciinema.org/a/377829" target="_blank"><img src="https://asciinema.org/a/377829.svg" /></a>\n\n##  Features 🚀\n\n* #### Creates customizable **project boilerplate.**\n* #### Creates customizable **app boilerplate.**\n* #### Handles the project structuring for you.\n* #### Optional Dockerfile generation.\n* #### Optional docker-compose generation for your project needs.\n* #### Optional pre-commit hook generation.\n\n\n## Installation\n\n* Prerequisites\n    * Python 3.6 +\n\nManage FastAPI can be installed by running \n\n```python\npip install fastapi-cli \n```\n\n\n## Usage\n\nTo get started right away with sensible defaults:\n\n```bash\nfastapi startproject [name]\n```\n\nYou can also use **interactive** mode!\n\n```bash\nfastapi startproject [name] --interactive\n```\n\n\n\n## Command line options\n\nManage FastAPI has three commands for now. You can list them by running `fastapi --help`:\n\n<img src="docs/docs_assets/fastapi-help.png" width=700>\n\nThe idea is to have a highly customizable CLI, but at the same time a simple interface for new users. You can see the available options for `startproject` running `fastapi startproject --help`:\n\n<img src="docs/docs_assets/startproject-help.png" width=700>\n\nThe other commands are already available but the current implementation is too shallow. More details about `startapp` and `run` commands will be provided once they have more functionalities, at the moment you can run `startapp` by just:\n\n```bash\nfastapi startapp {name}\n```\n\nOn the other hand, the `run` command expects you to have a `startproject` structure:\n\n```bash\nfastapi run\n```\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n',
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
