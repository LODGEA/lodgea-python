"""
    lodgea-python

    LODGEA SDK for python. Check out https://docs.lodgea.io for more information.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: support@lodgea.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lodgea-python.api_client import ApiClient, Endpoint as _Endpoint
from lodgea-python.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lodgea-python.model.inline_object import InlineObject
from lodgea-python.model.inline_object1 import InlineObject1
from lodgea-python.model.inline_response200 import InlineResponse200
from lodgea-python.model.inline_response2001 import InlineResponse2001
from lodgea-python.model.inline_response2002 import InlineResponse2002
from lodgea-python.model.inline_response2003 import InlineResponse2003
from lodgea-python.model.inline_response2004 import InlineResponse2004
from lodgea-python.model.inline_response400 import InlineResponse400
from lodgea-python.model.inline_response4001 import InlineResponse4001


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.availability_search_post_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2001,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/availability/search',
                'operation_id': 'availability_search_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'inline_object1',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'inline_object1':
                        (InlineObject1,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'inline_object1': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.location_search_post_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/location/search',
                'operation_id': 'location_search_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'inline_object',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'inline_object':
                        (InlineObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'inline_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.properties_get_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2002,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/properties',
                'operation_id': 'properties_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'keyword',
                    'page_token',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'keyword':
                        (str,),
                    'page_token':
                        (str,),
                },
                'attribute_map': {
                    'keyword': 'keyword',
                    'page_token': 'pageToken',
                },
                'location_map': {
                    'keyword': 'query',
                    'page_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.properties_property_id_availability_get_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2004,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/properties/{propertyId}/availability',
                'operation_id': 'properties_property_id_availability_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'property_id',
                    'currency_code',
                ],
                'required': [
                    'property_id',
                    'currency_code',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'property_id',
                ]
            },
            root_map={
                'validations': {
                    ('property_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'property_id':
                        (str,),
                    'currency_code':
                        (str,),
                },
                'attribute_map': {
                    'property_id': 'propertyId',
                    'currency_code': 'currencyCode',
                },
                'location_map': {
                    'property_id': 'path',
                    'currency_code': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.properties_property_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2003,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/properties/{propertyId}',
                'operation_id': 'properties_property_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'property_id',
                ],
                'required': [
                    'property_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'property_id',
                ]
            },
            root_map={
                'validations': {
                    ('property_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'property_id':
                        (str,),
                },
                'attribute_map': {
                    'property_id': 'propertyId',
                },
                'location_map': {
                    'property_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def availability_search_post(
        self,
        **kwargs
    ):
        """Search for availability  # noqa: E501

        Get availability information based on search criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.availability_search_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            inline_object1 (InlineObject1): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2001
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.availability_search_post_endpoint.call_with_http_info(**kwargs)

    def location_search_post(
        self,
        **kwargs
    ):
        """Search for location  # noqa: E501

        Get a list of locations and their lowest available rate related to a given keyword.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.location_search_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            inline_object (InlineObject): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse200
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.location_search_post_endpoint.call_with_http_info(**kwargs)

    def properties_get(
        self,
        **kwargs
    ):
        """List (filtered) properties  # noqa: E501

        List properties, optionally filtered by a keyword.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.properties_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            keyword (str): [optional]
            page_token (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2002
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.properties_get_endpoint.call_with_http_info(**kwargs)

    def properties_property_id_availability_get(
        self,
        property_id,
        currency_code,
        **kwargs
    ):
        """Get a properties availability  # noqa: E501

        Get detailed availability information for a specific property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.properties_property_id_availability_get(property_id, currency_code, async_req=True)
        >>> result = thread.get()

        Args:
            property_id (str):
            currency_code (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2004
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['property_id'] = \
            property_id
        kwargs['currency_code'] = \
            currency_code
        return self.properties_property_id_availability_get_endpoint.call_with_http_info(**kwargs)

    def properties_property_id_get(
        self,
        property_id,
        **kwargs
    ):
        """Get a properties details  # noqa: E501

        Get all information about a specific property by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.properties_property_id_get(property_id, async_req=True)
        >>> result = thread.get()

        Args:
            property_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2003
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['property_id'] = \
            property_id
        return self.properties_property_id_get_endpoint.call_with_http_info(**kwargs)

