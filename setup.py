from setuptools import setup
REQUIRES = [
    'allure-pytest',
    'restclient',
    'requests'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['apis', 'models'],
    url='https://github.com/July-vilh/dm_api_account.git',
    license='MIT',
    author='Yuliya Vilchynskaya',
    author_email='-',
    install_requirements=REQUIRES,
    description='dm api account'
)
