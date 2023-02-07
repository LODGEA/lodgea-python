"""
    lodgea-python

    LODGEA SDK for python. Check out https://docs.lodgea.io for more information.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: support@lodgea.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import lodgea-python
from com.lodgea.controllers.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_availability_search_post(self):
        """Test case for availability_search_post

        Search for availability  # noqa: E501
        """
        pass

    def test_location_search_post(self):
        """Test case for location_search_post

        Search for location  # noqa: E501
        """
        pass

    def test_properties_get(self):
        """Test case for properties_get

        List (filtered) properties  # noqa: E501
        """
        pass

    def test_properties_property_id_availability_get(self):
        """Test case for properties_property_id_availability_get

        Get a properties availability  # noqa: E501
        """
        pass

    def test_properties_property_id_get(self):
        """Test case for properties_property_id_get

        Get a properties details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
