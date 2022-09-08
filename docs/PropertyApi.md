# lodgea-python.PropertyApi

All URIs are relative to *https://api.eu.lodgea.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_property_get_post**](PropertyApi.md#v1_property_get_post) | **POST** /v1/property/get | Get Property by ID
[**v1_property_list_post**](PropertyApi.md#v1_property_list_post) | **POST** /v1/property/list | List properties by a specific keyword


# **v1_property_get_post**
> V1PropertyGetPost200Response v1_property_get_post(property_get)

Get Property by ID

Get all information about a specific property by its ID. This parameter is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import property_api
from lodgea-python.model.property_get import PropertyGet
from lodgea-python.model.v1_property_get_post200_response import V1PropertyGetPost200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.eu.lodgea.io
# See configuration.py for a list of all supported configuration parameters.
configuration = lodgea-python.Configuration(
    host = "https://api.eu.lodgea.io"
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
    api_instance = property_api.PropertyApi(api_client)
    property_get = PropertyGet(
        property_id="strandresidenz-sylt",
    ) # PropertyGet | Provide the property ID to get more information about it

    # example passing only required values which don't have defaults set
    try:
        # Get Property by ID
        api_response = api_instance.v1_property_get_post(property_get)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling PropertyApi->v1_property_get_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_get** | [**PropertyGet**](PropertyGet.md)| Provide the property ID to get more information about it |

### Return type

[**V1PropertyGetPost200Response**](V1PropertyGetPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request - missing parameter |  * apiKey -  <br>  |
**401** | API Key is missing or invalid |  * apiKey -  <br>  |
**403** | Forbidden |  * apiKey -  <br>  |
**404** | Not Found |  * apiKey -  <br>  |
**405** | Invalid input |  * apiKey -  <br>  |
**429** | Rate Limiting |  * apiKey -  <br>  |
**500** | Internal server error |  * apiKey -  <br>  |
**503** | Server error |  * apiKey -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_property_list_post**
> V1PropertyListPost200Response v1_property_list_post(property_list)

List properties by a specific keyword

List properties by a specific keyword.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import property_api
from lodgea-python.model.v1_property_list_post200_response import V1PropertyListPost200Response
from lodgea-python.model.property_list import PropertyList
from pprint import pprint
# Defining the host is optional and defaults to https://api.eu.lodgea.io
# See configuration.py for a list of all supported configuration parameters.
configuration = lodgea-python.Configuration(
    host = "https://api.eu.lodgea.io"
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
    api_instance = property_api.PropertyApi(api_client)
    property_list = PropertyList(
        keyword="Strandresidenz Sylt",
        page_token="eyJ0ZW5hbnRDb2RlIjoiZG1vLWRlbW8iLCJuYW1lIjoiTGFuZGhhdXMgVHJlc2tlcnNhbmQiLCJwcm9wZXJ0eUlkIjoibGFuZGhhdXMtdHJlc2tlcnNhbmQifQ==",
    ) # PropertyList | Provide the search keyword and optionally a page token to fetch further responses. The page token can be added if additional results should be returned. It is a base64 encoded dictionary and included in the first response in case not all results were delivered

    # example passing only required values which don't have defaults set
    try:
        # List properties by a specific keyword
        api_response = api_instance.v1_property_list_post(property_list)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling PropertyApi->v1_property_list_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_list** | [**PropertyList**](PropertyList.md)| Provide the search keyword and optionally a page token to fetch further responses. The page token can be added if additional results should be returned. It is a base64 encoded dictionary and included in the first response in case not all results were delivered |

### Return type

[**V1PropertyListPost200Response**](V1PropertyListPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request - missing parameter |  * apiKey -  <br>  |
**401** | API Key is missing or invalid |  * apiKey -  <br>  |
**403** | Forbidden |  * apiKey -  <br>  |
**404** | Not Found |  * apiKey -  <br>  |
**405** | Invalid input |  * apiKey -  <br>  |
**429** | Rate Limiting |  * apiKey -  <br>  |
**500** | Internal server error |  * apiKey -  <br>  |
**503** | Server error |  * apiKey -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

