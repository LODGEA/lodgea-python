"""
    lodgea-python

    LODGEA SDK for python. Check out https://docs.lodgea.io for more information.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: support@lodgea.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "lodgea-python"
VERSION = "1.2.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="lodgea-python",
    author="OpenAPI Generator community",
    author_email="support@lodgea.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "lodgea-python"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    LODGEA SDK for python. Check out https://docs.lodgea.io for more information.  # noqa: E501
    """
)
