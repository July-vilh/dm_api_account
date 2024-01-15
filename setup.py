from setuptools import setup
REQUESTS = [
    'allure-pytest',
    'restclient',
    'requests'
]

setup(
    name='dm_api_account',
    version='0.0.2',
    packages=['dm_api_account', 'dm_api_account.apis', 'dm_api_account.models'],
    url='https://github.com/July-vilh/dm_api_account.git',
    license='MIT',
    author='Yuliya Vilchynskaya',
    author_email='-',
    install_reqirements=REQUESTS,
    description='dm_api_account'
)
