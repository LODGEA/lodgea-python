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


def lazy_import():
    from lodgea-python.model.available_properties_inner1_geo_location import AvailablePropertiesInner1GeoLocation
    from lodgea-python.model.properties_property_id_get200_response_property_property_info_accepted_payment_list_inner import PropertiesPropertyIdGet200ResponsePropertyPropertyInfoAcceptedPaymentListInner
    from lodgea-python.model.properties_property_id_get200_response_property_property_info_message_list_inner import PropertiesPropertyIdGet200ResponsePropertyPropertyInfoMessageListInner
    globals()['AvailablePropertiesInner1GeoLocation'] = AvailablePropertiesInner1GeoLocation
    globals()['PropertiesPropertyIdGet200ResponsePropertyPropertyInfoAcceptedPaymentListInner'] = PropertiesPropertyIdGet200ResponsePropertyPropertyInfoAcceptedPaymentListInner
    globals()['PropertiesPropertyIdGet200ResponsePropertyPropertyInfoMessageListInner'] = PropertiesPropertyIdGet200ResponsePropertyPropertyInfoMessageListInner


class PropertiesPropertyIdGet200ResponsePropertyPropertyInfo(ModelNormal):
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
        ('category_list',): {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            '11': 11,
            '12': 12,
            '13': 13,
            '14': 14,
            '15': 15,
            '16': 16,
            '17': 17,
            '18': 18,
            '19': 19,
            '20': 20,
            '21': 21,
            '22': 22,
            '23': 23,
            '24': 24,
            '25': 25,
            '26': 26,
            '27': 27,
            '28': 28,
            '29': 29,
            '30': 30,
            '31': 31,
            '32': 32,
            '33': 33,
            '34': 34,
            '35': 35,
            '36': 36,
            '37': 37,
            '38': 38,
            '39': 39,
            '40': 40,
            '41': 41,
            '42': 42,
            '43': 43,
            '44': 44,
            '45': 45,
            '46': 46,
            '47': 47,
            '48': 48,
            '49': 49,
            '50': 50,
            '51': 51,
            '52': 52,
            '53': 53,
            '54': 54,
            '55': 55,
            '56': 56,
            '57': 57,
            '58': 58,
            '59': 59,
            '60': 60,
            '61': 61,
            '62': 62,
            '5000': 5000,
            '5001': 5001,
            '5002': 5002,
            '5003': 5003,
            '5004': 5004,
            '5005': 5005,
            '5006': 5006,
            '5007': 5007,
            '5008': 5008,
            '5009': 5009,
        },
        ('language_list',): {
            'AF': "af",
            'AR': "ar",
            'AZ': "az",
            'BE': "be",
            'BG': "bg",
            'CA': "ca",
            'CS': "cs",
            'DA': "da",
            'DE': "de",
            'EL': "el",
            'EN': "en",
            'EN-GB': "en-gb",
            'EN-US': "en-us",
            'ES': "es",
            'ES-AR': "es-ar",
            'ET': "et",
            'FR': "fr",
            'FI': "fi",
            'HE': "he",
            'HI': "hi",
            'HR': "hr",
            'HU': "hu",
            'ID': "id",
            'IS': "is",
            'IT': "it",
            'JA': "ja",
            'KM': "km",
            'KO': "ko",
            'LO': "lo",
            'LT': "lt",
            'LV': "lv",
            'MS': "ms",
            'NL': "nl",
            'NO': "no",
            'PL': "pl",
            'PT': "pt",
            'PT-BR': "pt-br",
            'PT-PT': "pt-pt",
            'RO': "ro",
            'RU': "ru",
            'SK': "sk",
            'SL': "sl",
            'SR': "sr",
            'SV': "sv",
            'TL': "tl",
            'TH': "th",
            'TR': "tr",
            'UK': "uk",
            'VI': "vi",
            'XA': "xa",
            'XB': "xb",
            'XS': "xs",
            'XT': "xt",
            'XU': "xu",
            'ZH': "zh",
            'ZH-CN': "zh-cn",
            'ZH-TW': "zh-tw",
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
        lazy_import()
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
        lazy_import()
        return {
            'message_list': ([PropertiesPropertyIdGet200ResponsePropertyPropertyInfoMessageListInner],),  # noqa: E501
            'category_list': ([float],),  # noqa: E501
            'language_list': ([str],),  # noqa: E501
            'accepted_payment_list': ([PropertiesPropertyIdGet200ResponsePropertyPropertyInfoAcceptedPaymentListInner],),  # noqa: E501
            'unit_count': (float,),  # noqa: E501
            'location': (AvailablePropertiesInner1GeoLocation,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'message_list': 'messageList',  # noqa: E501
        'category_list': 'categoryList',  # noqa: E501
        'language_list': 'languageList',  # noqa: E501
        'accepted_payment_list': 'acceptedPaymentList',  # noqa: E501
        'unit_count': 'unitCount',  # noqa: E501
        'location': 'location',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, message_list, category_list, language_list, accepted_payment_list, *args, **kwargs):  # noqa: E501
        """PropertiesPropertyIdGet200ResponsePropertyPropertyInfo - a model defined in OpenAPI

        Args:
            message_list ([PropertiesPropertyIdGet200ResponsePropertyPropertyInfoMessageListInner]): Contains a descriptive message for this property in all supported languages.
            category_list ([float]): A list of code of the property class types that apply to the property.
            language_list ([str]): The codes of languages the staff of this property can speak. Please note that these codes partially differ from the two character ISO language codes widely used throughout the API as they partially include country specific language code.<p>See also <a href=\"#languagecountry-code\">in the appendix</a>.</p>
            accepted_payment_list ([PropertiesPropertyIdGet200ResponsePropertyPropertyInfoAcceptedPaymentListInner]): A list of the accepted payment methods. Payment methods might subject to frequent change as payment providers come and go. You should always implement a way to handle new, unexpected payment methods.<p>See also <a href=\"#paymenttypes\">in the appendix</a>.</p>

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
            unit_count (float): The amount of units the property has.. [optional]  # noqa: E501
            location (AvailablePropertiesInner1GeoLocation): [optional]  # noqa: E501
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

        self.message_list = message_list
        self.category_list = category_list
        self.language_list = language_list
        self.accepted_payment_list = accepted_payment_list
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
    def __init__(self, message_list, category_list, language_list, accepted_payment_list, *args, **kwargs):  # noqa: E501
        """PropertiesPropertyIdGet200ResponsePropertyPropertyInfo - a model defined in OpenAPI

        Args:
            message_list ([PropertiesPropertyIdGet200ResponsePropertyPropertyInfoMessageListInner]): Contains a descriptive message for this property in all supported languages.
            category_list ([float]): A list of code of the property class types that apply to the property.
            language_list ([str]): The codes of languages the staff of this property can speak. Please note that these codes partially differ from the two character ISO language codes widely used throughout the API as they partially include country specific language code.<p>See also <a href=\"#languagecountry-code\">in the appendix</a>.</p>
            accepted_payment_list ([PropertiesPropertyIdGet200ResponsePropertyPropertyInfoAcceptedPaymentListInner]): A list of the accepted payment methods. Payment methods might subject to frequent change as payment providers come and go. You should always implement a way to handle new, unexpected payment methods.<p>See also <a href=\"#paymenttypes\">in the appendix</a>.</p>

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
            unit_count (float): The amount of units the property has.. [optional]  # noqa: E501
            location (AvailablePropertiesInner1GeoLocation): [optional]  # noqa: E501
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

        self.message_list = message_list
        self.category_list = category_list
        self.language_list = language_list
        self.accepted_payment_list = accepted_payment_list
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
