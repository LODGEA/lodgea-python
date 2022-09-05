"""
    lodgea-python

    LODGEA SDK for Python. Check out https://docs.lodgea.io for more information.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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
    from lodgea-python.model.v1_property_get_post200_response_product_list_inner_policy_info_cancellation_policy_list_inner import V1PropertyGetPost200ResponseProductListInnerPolicyInfoCancellationPolicyListInner
    from lodgea-python.model.v1_property_get_post200_response_property_policy_list_inner_pets_policy import V1PropertyGetPost200ResponsePropertyPolicyListInnerPetsPolicy
    from lodgea-python.model.v1_property_get_post200_response_property_policy_list_inner_tax_policy_list_inner import V1PropertyGetPost200ResponsePropertyPolicyListInnerTaxPolicyListInner
    globals()['V1PropertyGetPost200ResponseProductListInnerPolicyInfoCancellationPolicyListInner'] = V1PropertyGetPost200ResponseProductListInnerPolicyInfoCancellationPolicyListInner
    globals()['V1PropertyGetPost200ResponsePropertyPolicyListInnerPetsPolicy'] = V1PropertyGetPost200ResponsePropertyPolicyListInnerPetsPolicy
    globals()['V1PropertyGetPost200ResponsePropertyPolicyListInnerTaxPolicyListInner'] = V1PropertyGetPost200ResponsePropertyPolicyListInnerTaxPolicyListInner


class V1PropertyGetPost200ResponseProductListInnerPolicyInfo(ModelNormal):
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
            'check_in_time': (float,),  # noqa: E501
            'check_out_time': (float,),  # noqa: E501
            'total_guest_count': (float,),  # noqa: E501
            'cancellation_policy_list': ([V1PropertyGetPost200ResponseProductListInnerPolicyInfoCancellationPolicyListInner],),  # noqa: E501
            'advance_booking_min': (float,),  # noqa: E501
            'advance_booking_max': (float,),  # noqa: E501
            'pets_policy': (V1PropertyGetPost200ResponsePropertyPolicyListInnerPetsPolicy,),  # noqa: E501
            'prepayment_policy': (str,),  # noqa: E501
            'guarantee_policy': (str,),  # noqa: E501
            'tax_policy_list': ([V1PropertyGetPost200ResponsePropertyPolicyListInnerTaxPolicyListInner],),  # noqa: E501
            'fee_policy_list': ([str],),  # noqa: E501
            'name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'check_in_time': 'checkInTime',  # noqa: E501
        'check_out_time': 'checkOutTime',  # noqa: E501
        'total_guest_count': 'totalGuestCount',  # noqa: E501
        'cancellation_policy_list': 'cancellationPolicyList',  # noqa: E501
        'advance_booking_min': 'advanceBookingMin',  # noqa: E501
        'advance_booking_max': 'advanceBookingMax',  # noqa: E501
        'pets_policy': 'petsPolicy',  # noqa: E501
        'prepayment_policy': 'prepaymentPolicy',  # noqa: E501
        'guarantee_policy': 'guaranteePolicy',  # noqa: E501
        'tax_policy_list': 'taxPolicyList',  # noqa: E501
        'fee_policy_list': 'feePolicyList',  # noqa: E501
        'name': 'name',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """V1PropertyGetPost200ResponseProductListInnerPolicyInfo - a model defined in OpenAPI

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
            check_in_time (float): [optional]  # noqa: E501
            check_out_time (float): [optional]  # noqa: E501
            total_guest_count (float): [optional]  # noqa: E501
            cancellation_policy_list ([V1PropertyGetPost200ResponseProductListInnerPolicyInfoCancellationPolicyListInner]): [optional]  # noqa: E501
            advance_booking_min (float): [optional]  # noqa: E501
            advance_booking_max (float): [optional]  # noqa: E501
            pets_policy (V1PropertyGetPost200ResponsePropertyPolicyListInnerPetsPolicy): [optional]  # noqa: E501
            prepayment_policy (str): [optional]  # noqa: E501
            guarantee_policy (str): [optional]  # noqa: E501
            tax_policy_list ([V1PropertyGetPost200ResponsePropertyPolicyListInnerTaxPolicyListInner]): [optional]  # noqa: E501
            fee_policy_list ([str]): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """V1PropertyGetPost200ResponseProductListInnerPolicyInfo - a model defined in OpenAPI

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
            check_in_time (float): [optional]  # noqa: E501
            check_out_time (float): [optional]  # noqa: E501
            total_guest_count (float): [optional]  # noqa: E501
            cancellation_policy_list ([V1PropertyGetPost200ResponseProductListInnerPolicyInfoCancellationPolicyListInner]): [optional]  # noqa: E501
            advance_booking_min (float): [optional]  # noqa: E501
            advance_booking_max (float): [optional]  # noqa: E501
            pets_policy (V1PropertyGetPost200ResponsePropertyPolicyListInnerPetsPolicy): [optional]  # noqa: E501
            prepayment_policy (str): [optional]  # noqa: E501
            guarantee_policy (str): [optional]  # noqa: E501
            tax_policy_list ([V1PropertyGetPost200ResponsePropertyPolicyListInnerTaxPolicyListInner]): [optional]  # noqa: E501
            fee_policy_list ([str]): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
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
