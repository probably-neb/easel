
from setuptools import setup, find_packages
from easel.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='easel',
    version=VERSION,
    description='Cli interface for interacting with the Canvas LMS REST API',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Ben Kunkle',
    author_email='ben.kunkle@gmail.com',
    url='https://github.com/probably-neb/easel',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'easel': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        easel = easel.main:main
    """,
)
