from setuptools import setup, find_packages
from pyFAI_calibrants import VERSION

setup(
    name='pyFAI_calibrants',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pyFAI'],
    url='https://github.com/kremeyer/pyFAI_calibrants',
    license='',
    author='Laurenz Kremeyer',
    author_email='laurenz.kremeyer@mail.mcgill.ca',
    description='Collection of pyFAI calibration files'
)