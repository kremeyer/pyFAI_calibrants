from setuptools import setup, find_packages

VERSION = 0.1

with open("requirements.txt") as f:
    REQUIREMENTS = [line for line in f.read().split("\n") if len(line.strip())]

setup(
    name='pyFAI_calibrants',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    url='https://github.com/kremeyer/pyFAI_calibrants',
    author='Laurenz Kremeyer',
    author_email='laurenz.kremeyer@mail.mcgill.ca',
    description='Collection of pyFAI calibration files'
)
