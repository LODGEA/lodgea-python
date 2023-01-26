"""
    lodgea-python

    LODGEA SDK for Python. Check out https://docs.lodgea.io for more information.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: support@lodgea.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lodgea-python.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from lodgea-python.exceptions import ApiAttributeError



class AvailablePropertiesInner1MediaListInner(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('tag_list',): {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '10': 10,
            '11': 11,
            '13': 13,
            '14': 14,
            '37': 37,
            '41': 41,
            '42': 42,
            '43': 43,
            '50': 50,
            '55': 55,
            '61': 61,
            '70': 70,
            '74': 74,
            '81': 81,
            '82': 82,
            '87': 87,
            '89': 89,
            '90': 90,
            '94': 94,
            '95': 95,
            '96': 96,
            '97': 97,
            '100': 100,
            '102': 102,
            '103': 103,
            '104': 104,
            '106': 106,
            '107': 107,
            '108': 108,
            '112': 112,
            '113': 113,
            '114': 114,
            '115': 115,
            '116': 116,
            '124': 124,
            '125': 125,
            '128': 128,
            '131': 131,
            '133': 133,
            '134': 134,
            '137': 137,
            '141': 141,
            '143': 143,
            '153': 153,
            '154': 154,
            '155': 155,
            '156': 156,
            '157': 157,
            '158': 158,
            '159': 159,
            '160': 160,
            '161': 161,
            '164': 164,
            '165': 165,
            '167': 167,
            '172': 172,
            '173': 173,
            '177': 177,
            '178': 178,
            '179': 179,
            '182': 182,
            '183': 183,
            '184': 184,
            '185': 185,
            '186': 186,
            '187': 187,
            '188': 188,
            '189': 189,
            '190': 190,
            '191': 191,
            '192': 192,
            '193': 193,
            '194': 194,
            '197': 197,
            '198': 198,
            '199': 199,
            '204': 204,
            '205': 205,
            '240': 240,
            '241': 241,
            '242': 242,
            '245': 245,
            '246': 246,
            '247': 247,
            '248': 248,
            '249': 249,
            '250': 250,
            '251': 251,
            '252': 252,
            '253': 253,
            '254': 254,
            '255': 255,
            '256': 256,
            '257': 257,
            '258': 258,
            '259': 259,
            '260': 260,
            '261': 261,
            '262': 262,
            '263': 263,
            '264': 264,
            '265': 265,
            '266': 266,
            '267': 267,
            '268': 268,
            '269': 269,
            '270': 270,
            '271': 271,
            '272': 272,
            '273': 273,
            '276': 276,
            '277': 277,
            '278': 278,
            '279': 279,
            '280': 280,
            '281': 281,
            '282': 282,
            '283': 283,
            '284': 284,
            '285': 285,
            '286': 286,
            '287': 287,
            '289': 289,
            '290': 290,
            '291': 291,
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'tag_list': ([float],),  # noqa: E501
            'is_main_image': (bool,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'sort_order': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tag_list': 'tagList',  # noqa: E501
        'is_main_image': 'isMainImage',  # noqa: E501
        'url': 'url',  # noqa: E501
        'sort_order': 'sortOrder',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, tag_list, is_main_image, url, sort_order, *args, **kwargs):  # noqa: E501
        """AvailablePropertiesInner1MediaListInner - a model defined in OpenAPI

        Args:
            tag_list ([float]): A list of tag codes for the media.<p>See also <a href=\"#imagetype-codes\">in the appendix</a>.</p>
            is_main_image (bool): Whether the media is the main image for the property.
            url (str): The URL for the media.
            sort_order (float): The sort order for the media.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.tag_list = tag_list
        self.is_main_image = is_main_image
        self.url = url
        self.sort_order = sort_order
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, tag_list, is_main_image, url, sort_order, *args, **kwargs):  # noqa: E501
        """AvailablePropertiesInner1MediaListInner - a model defined in OpenAPI

        Args:
            tag_list ([float]): A list of tag codes for the media.<p>See also <a href=\"#imagetype-codes\">in the appendix</a>.</p>
            is_main_image (bool): Whether the media is the main image for the property.
            url (str): The URL for the media.
            sort_order (float): The sort order for the media.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.tag_list = tag_list
        self.is_main_image = is_main_image
        self.url = url
        self.sort_order = sort_order
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")