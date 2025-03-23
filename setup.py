# Copyright (c) Mehmet Bektas <mbektasgh@outlook.com>

from setuptools import setup, find_packages
from .nbi_extension_plotting._version import __version__

setup(
    name='nbi_extension_plotting',
    version=__version__,
    packages=find_packages(),
    include_package_data=True
)
