
"""A setuptools based setup module.
"""

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))
with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='panda3d-assetcoop',
    version='0.013',
    description='Free to use panda3d models.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/thecheapestpixels/panda3d-assetcoop',
    author='thecheapestpixels',
    keywords='panda3d',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['panda3d'],
)
