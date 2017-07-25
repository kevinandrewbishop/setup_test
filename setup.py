from setuptools import setup

setup(name = 'setup_test',
    version = '0.1',
    description = 'used as a test to make packages easily installed via github',
    url = 'http://github.com/kevinandrewbishop/setup_test',
    author = 'Kevin Bishop',
    author_email = 'kevinandrewbishop@gmail.com',
    license = 'MIT',
    packages = ['setup_test'],
    zip_safe = False,
    scripts = ['bin/setup_test'])
