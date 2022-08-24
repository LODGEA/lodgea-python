# lodgea-python.AvailabilityApi

All URIs are relative to *https://api.eu.lodgea.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_availability_search_post**](AvailabilityApi.md#v1_availability_search_post) | **POST** /v1/availability/search | Search for Availability


# **v1_availability_search_post**
> V1AvailabilitySearchPost200Response v1_availability_search_post()

Search for Availability

Get availability information based on search criteria. The possible values for the different content parameters are listed below. All parameters are optional.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import lodgea-python
from com.lodgea.controllers import availability_api
from lodgea-python.model.v1_availability_search_post200_response import V1AvailabilitySearchPost200Response
from lodgea-python.model.availability_search import AvailabilitySearch
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
    api_instance = availability_api.AvailabilityApi(api_client)
    availability_search = AvailabilitySearch(
        adult_count=2,
        child_count=2,
        child_age_list=[
            3,
        ],
        currency_code="EUR",
        min_length_of_stay=1,
        max_length_of_stay=27,
        location_name="Oberbayern",
        location_type="locality",
        earliest_arrival=dateutil_parser('Thu Sep 01 00:00:00 UTC 2022').date(),
        latest_return=dateutil_parser('Thu Sep 08 00:00:00 UTC 2022').date(),
        sort="quality",
        service_list=[
            242,
        ],
        type_list=[
            20,
        ],
        unit_type_list=[
            9,
        ],
        unit_amenity_list=[
            50,
        ],
        meal_plan_list=[
            19,
        ],
    ) # AvailabilitySearch | Search Criteria, all parameters are optional (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for Availability
        api_response = api_instance.v1_availability_search_post(availability_search=availability_search)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling AvailabilityApi->v1_availability_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **availability_search** | [**AvailabilitySearch**](AvailabilitySearch.md)| Search Criteria, all parameters are optional | [optional]

### Return type

[**V1AvailabilitySearchPost200Response**](V1AvailabilitySearchPost200Response.md)

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

