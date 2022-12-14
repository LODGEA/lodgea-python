# lodgea-python.LocationApi

All URIs are relative to *https://api.eu.lodgea.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_location_search_post**](LocationApi.md#v1_location_search_post) | **POST** /v1/location/search | Search for Location


# **v1_location_search_post**
> V1LocationSearchPost200Response v1_location_search_post(location_search)

Search for Location

Get a location by search text in free from. This parameter is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import location_api
from lodgea-python.model.location_search import LocationSearch
from lodgea-python.model.v1_location_search_post200_response import V1LocationSearchPost200Response
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
    api_instance = location_api.LocationApi(api_client)
    location_search = LocationSearch(
        search_text="Hotel Stadt Hamburg",
        currency_code="EUR",
        language_code="en",
    ) # LocationSearch | Free-text search criteria

    # example passing only required values which don't have defaults set
    try:
        # Search for Location
        api_response = api_instance.v1_location_search_post(location_search)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling LocationApi->v1_location_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_search** | [**LocationSearch**](LocationSearch.md)| Free-text search criteria |

### Return type

[**V1LocationSearchPost200Response**](V1LocationSearchPost200Response.md)

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

