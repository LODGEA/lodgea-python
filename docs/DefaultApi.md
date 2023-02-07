# lodgea-python.DefaultApi

All URIs are relative to *https://api.eu.lodgea.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availability_search_post**](DefaultApi.md#availability_search_post) | **POST** /availability/search | Search for availability
[**location_search_post**](DefaultApi.md#location_search_post) | **POST** /location/search | Search for location
[**properties_get**](DefaultApi.md#properties_get) | **GET** /properties | List (filtered) properties
[**properties_property_id_availability_get**](DefaultApi.md#properties_property_id_availability_get) | **GET** /properties/{propertyId}/availability | Get a properties availability
[**properties_property_id_get**](DefaultApi.md#properties_property_id_get) | **GET** /properties/{propertyId} | Get a properties details


# **availability_search_post**
> InlineResponse2001 availability_search_post()

Search for availability

Get availability information based on search criteria.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import default_api
from lodgea-python.model.inline_object1 import InlineObject1
from lodgea-python.model.inline_response4001 import InlineResponse4001
from lodgea-python.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://api.eu.lodgea.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lodgea-python.Configuration(
    host = "https://api.eu.lodgea.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lodgea-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    inline_object1 = InlineObject1(
        adult_count=2,
        child_count=2,
        child_age_list=[4,7],
        currency_code="EUR",
        language_code="en",
        unit_system="metric",
        min_length_of_stay=1,
        max_length_of_stay=27,
        location_name="Oberbayern",
        location_type="locality",
        earliest_arrival="2022-09-01",
        latest_return="2022-09-08",
        sort="price",
        service_list=[1,2],
        type_list=[3,4],
        unit_type_list=[5,6],
        unit_amenity_list=[7,8],
        meal_plan_list=[9,10],
    ) # InlineObject1 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for availability
        api_response = api_instance.availability_search_post(inline_object1=inline_object1)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling DefaultApi->availability_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful, a list of available properties matching the given criteria is returned. |  -  |
**400** | We validate all calls to our API in a strict manner using Zod. In case of any validation errors, we send back a 400 response with a list of all validation errors. For more info see https://github.com/colinhacks/zod/blob/master/ERROR_HANDLING.md. |  -  |
**403** | Unauthorized, the api key in the \&quot;apiKey\&quot; header field is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_search_post**
> InlineResponse200 location_search_post()

Search for location

Get a list of locations and their lowest available rate related to a given keyword.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import default_api
from lodgea-python.model.inline_response200 import InlineResponse200
from lodgea-python.model.inline_response400 import InlineResponse400
from lodgea-python.model.inline_object import InlineObject
from pprint import pprint
# Defining the host is optional and defaults to https://api.eu.lodgea.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lodgea-python.Configuration(
    host = "https://api.eu.lodgea.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lodgea-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    inline_object = InlineObject(
        search_text="Hotel Stadt Hamburg",
        currency_code="EUR",
        language_code="en",
    ) # InlineObject |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for location
        api_response = api_instance.location_search_post(inline_object=inline_object)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling DefaultApi->location_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful, a list of locations matching the given location search text is returned. |  -  |
**400** | We validate all calls to our API in a strict manner using Zod. In case of any validation errors, we send back a 400 response with a list of all validation errors. For more info see https://github.com/colinhacks/zod/blob/master/ERROR_HANDLING.md. |  -  |
**403** | Unauthorized, the api key in the \&quot;apiKey\&quot; header field is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_get**
> InlineResponse2002 properties_get()

List (filtered) properties

List properties, optionally filtered by a keyword.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import default_api
from lodgea-python.model.inline_response4001 import InlineResponse4001
from lodgea-python.model.inline_response2002 import InlineResponse2002
from pprint import pprint
# Defining the host is optional and defaults to https://api.eu.lodgea.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lodgea-python.Configuration(
    host = "https://api.eu.lodgea.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lodgea-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    keyword = "Strandresidenz Sylt" # str |  (optional)
    page_token = "eyJ0ZW5hbnRDb2RlIjoiZG1vLWRlbW8iLCJuYW1lIjoiTGFuZGhhdXMgVHJlc2tlcnNhbmQiLCJwcm9wZXJ0eUlkIjoibGFuZGhhdXMtdHJlc2tlcnNhbmQifQ==" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List (filtered) properties
        api_response = api_instance.properties_get(keyword=keyword, page_token=page_token)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling DefaultApi->properties_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**|  | [optional]
 **page_token** | **str**|  | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful, a list of properties matching the given keyword is returned. |  -  |
**400** | We validate all calls to our API in a strict manner using Zod. In case of any validation errors, we send back a 400 response with a list of all validation errors. For more info see https://github.com/colinhacks/zod/blob/master/ERROR_HANDLING.md. |  -  |
**403** | Unauthorized, the api key in the \&quot;apiKey\&quot; header field is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_property_id_availability_get**
> InlineResponse2004 properties_property_id_availability_get(property_id, currency_code)

Get a properties availability

Get detailed availability information for a specific property.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import default_api
from lodgea-python.model.inline_response4001 import InlineResponse4001
from lodgea-python.model.inline_response2004 import InlineResponse2004
from pprint import pprint
# Defining the host is optional and defaults to https://api.eu.lodgea.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lodgea-python.Configuration(
    host = "https://api.eu.lodgea.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lodgea-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    property_id = "strandresidenz-sylt" # str | 
    currency_code = "EUR" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a properties availability
        api_response = api_instance.properties_property_id_availability_get(property_id, currency_code)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling DefaultApi->properties_property_id_availability_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**|  |
 **currency_code** | **str**|  |

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful, a list of properties matching the given keyword is returned. |  -  |
**400** | We validate all calls to our API in a strict manner using Zod. In case of any validation errors, we send back a 400 response with a list of all validation errors. For more info see https://github.com/colinhacks/zod/blob/master/ERROR_HANDLING.md. |  -  |
**403** | Unauthorized, the api key in the \&quot;apiKey\&quot; header field is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_property_id_get**
> InlineResponse2003 properties_property_id_get(property_id)

Get a properties details

Get all information about a specific property by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import default_api
from lodgea-python.model.inline_response4001 import InlineResponse4001
from lodgea-python.model.inline_response2003 import InlineResponse2003
from pprint import pprint
# Defining the host is optional and defaults to https://api.eu.lodgea.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lodgea-python.Configuration(
    host = "https://api.eu.lodgea.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lodgea-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    property_id = "strandresidenz-sylt" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a properties details
        api_response = api_instance.properties_property_id_get(property_id)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling DefaultApi->properties_property_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**|  |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful, property found, the whole property object is returned. |  -  |
**400** | We validate all calls to our API in a strict manner using Zod. In case of any validation errors, we send back a 400 response with a list of all validation errors. For more info see https://github.com/colinhacks/zod/blob/master/ERROR_HANDLING.md. |  -  |
**403** | Unauthorized, the api key in the \&quot;apiKey\&quot; header field is invalid. |  -  |
**404** | The requested resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

