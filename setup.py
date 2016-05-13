# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "docraptor"
VERSION = "1.0.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="A wrapper for the DocRaptor HTML to PDF/XLS service.",
    author="Elijah Miller",
    author_email="elijah.miller@gmail.com",
    maintainer="DocRaptor Support",
    maintainer_email="support@docraptor.com",
    url="https://github.com/docraptor/docraptor-python",
    keywords=["DocRaptor", "API", "PDF", "XLS", "XLSX", "HTML"],
    classifiers=[ # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",

        "Environment :: Web Environment",

        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",

        "License :: OSI Approved :: Apache Software License",

        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",

        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial :: Spreadsheet",

        "Topic :: Printing",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    license="Apache V2.0 License",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A native client library for the DocRaptor HTML to PDF/XLS service.
    """
)
