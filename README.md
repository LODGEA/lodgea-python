# lodgea-python
LODGEA SDK for Python. Check out https://docs.lodgea.io for more information.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.2
- Package version: 1.0.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import lodgea-python
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import lodgea-python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import lodgea-python
from pprint import pprint
from com.lodgea.controllers import availability_api
from lodgea-python.model.availability_get import AvailabilityGet
from lodgea-python.model.availability_search import AvailabilitySearch
from lodgea-python.model.v1_availability_get_post200_response import V1AvailabilityGetPost200Response
from lodgea-python.model.v1_availability_search_post200_response import V1AvailabilitySearchPost200Response
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
    availability_get = AvailabilityGet(
        property_code="strandresidenz-sylt",
        currency_code="EUR",
    ) # AvailabilityGet | Availability get parameter

    try:
        # Get Availability for Property
        api_response = api_instance.v1_availability_get_post(availability_get)
        pprint(api_response)
    except lodgea-python.ApiException as e:
        print("Exception when calling AvailabilityApi->v1_availability_get_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.eu.lodgea.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AvailabilityApi* | [**v1_availability_get_post**](docs/AvailabilityApi.md#v1_availability_get_post) | **POST** /v1/availability/get | Get Availability for Property
*AvailabilityApi* | [**v1_availability_search_post**](docs/AvailabilityApi.md#v1_availability_search_post) | **POST** /v1/availability/search | Search for Availability
*LocationApi* | [**v1_location_search_post**](docs/LocationApi.md#v1_location_search_post) | **POST** /v1/location/search | Search for Location
*PropertyApi* | [**v1_property_get_post**](docs/PropertyApi.md#v1_property_get_post) | **POST** /v1/property/get | Get Property by ID
*PropertyApi* | [**v1_property_list_post**](docs/PropertyApi.md#v1_property_list_post) | **POST** /v1/property/list | List properties by a specific keyword


## Documentation For Models

 - [AvailabilityGet](docs/AvailabilityGet.md)
 - [AvailabilitySearch](docs/AvailabilitySearch.md)
 - [LocationSearch](docs/LocationSearch.md)
 - [PropertyGet](docs/PropertyGet.md)
 - [PropertyList](docs/PropertyList.md)
 - [V1AvailabilityGetPost200Response](docs/V1AvailabilityGetPost200Response.md)
 - [V1AvailabilityGetPost200ResponseRatePlanListInner](docs/V1AvailabilityGetPost200ResponseRatePlanListInner.md)
 - [V1AvailabilityGetPost200ResponseRatePlanListInnerPricingListInner](docs/V1AvailabilityGetPost200ResponseRatePlanListInnerPricingListInner.md)
 - [V1AvailabilityGetPost200ResponseRatePlanListInnerPricingListInnerPriceList](docs/V1AvailabilityGetPost200ResponseRatePlanListInnerPricingListInnerPriceList.md)
 - [V1AvailabilityGetPost200ResponseRoomTypeListInner](docs/V1AvailabilityGetPost200ResponseRoomTypeListInner.md)
 - [V1AvailabilitySearchPost200Response](docs/V1AvailabilitySearchPost200Response.md)
 - [V1AvailabilitySearchPost200ResponseListInner](docs/V1AvailabilitySearchPost200ResponseListInner.md)
 - [V1AvailabilitySearchPost200ResponseListInnerAttractionListInner](docs/V1AvailabilitySearchPost200ResponseListInnerAttractionListInner.md)
 - [V1AvailabilitySearchPost200ResponseListInnerAttractionListInnerDistance](docs/V1AvailabilitySearchPost200ResponseListInnerAttractionListInnerDistance.md)
 - [V1AvailabilitySearchPost200ResponseListInnerGeo](docs/V1AvailabilitySearchPost200ResponseListInnerGeo.md)
 - [V1AvailabilitySearchPost200ResponseListInnerGeoLocation](docs/V1AvailabilitySearchPost200ResponseListInnerGeoLocation.md)
 - [V1AvailabilitySearchPost200ResponseListInnerLowestPrice](docs/V1AvailabilitySearchPost200ResponseListInnerLowestPrice.md)
 - [V1AvailabilitySearchPost200ResponseListInnerMediaListInner](docs/V1AvailabilitySearchPost200ResponseListInnerMediaListInner.md)
 - [V1LocationSearchPost200Response](docs/V1LocationSearchPost200Response.md)
 - [V1LocationSearchPost200ResponseListInner](docs/V1LocationSearchPost200ResponseListInner.md)
 - [V1PropertyGetPost200Response](docs/V1PropertyGetPost200Response.md)
 - [V1PropertyGetPost200ResponseProductListInner](docs/V1PropertyGetPost200ResponseProductListInner.md)
 - [V1PropertyGetPost200ResponseProductListInnerMealPlanListInner](docs/V1PropertyGetPost200ResponseProductListInnerMealPlanListInner.md)
 - [V1PropertyGetPost200ResponseProductListInnerPolicyInfo](docs/V1PropertyGetPost200ResponseProductListInnerPolicyInfo.md)
 - [V1PropertyGetPost200ResponseProductListInnerPolicyInfoCancellationPolicyListInner](docs/V1PropertyGetPost200ResponseProductListInnerPolicyInfoCancellationPolicyListInner.md)
 - [V1PropertyGetPost200ResponseProductListInnerRatePlanListInner](docs/V1PropertyGetPost200ResponseProductListInnerRatePlanListInner.md)
 - [V1PropertyGetPost200ResponseProductListInnerRatePlanListInnerPricingListInner](docs/V1PropertyGetPost200ResponseProductListInnerRatePlanListInnerPricingListInner.md)
 - [V1PropertyGetPost200ResponseProductListInnerRatePlanListInnerPricingListInnerPriceList](docs/V1PropertyGetPost200ResponseProductListInnerRatePlanListInnerPricingListInnerPriceList.md)
 - [V1PropertyGetPost200ResponseProductListInnerRoomTypeListInner](docs/V1PropertyGetPost200ResponseProductListInnerRoomTypeListInner.md)
 - [V1PropertyGetPost200ResponseProperty](docs/V1PropertyGetPost200ResponseProperty.md)
 - [V1PropertyGetPost200ResponsePropertyAwardListInner](docs/V1PropertyGetPost200ResponsePropertyAwardListInner.md)
 - [V1PropertyGetPost200ResponsePropertyCancellationGracePeriod](docs/V1PropertyGetPost200ResponsePropertyCancellationGracePeriod.md)
 - [V1PropertyGetPost200ResponsePropertyContactListInner](docs/V1PropertyGetPost200ResponsePropertyContactListInner.md)
 - [V1PropertyGetPost200ResponsePropertyContactListInnerAddressListInner](docs/V1PropertyGetPost200ResponsePropertyContactListInnerAddressListInner.md)
 - [V1PropertyGetPost200ResponsePropertyFacilityInfo](docs/V1PropertyGetPost200ResponsePropertyFacilityInfo.md)
 - [V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInner](docs/V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInner.md)
 - [V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerAmenityListInner](docs/V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerAmenityListInner.md)
 - [V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerMediaListInner](docs/V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerMediaListInner.md)
 - [V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerMediaListInnerRoomAmenityListInner](docs/V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerMediaListInnerRoomAmenityListInner.md)
 - [V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerMediaListInnerTagListInner](docs/V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerMediaListInnerTagListInner.md)
 - [V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerMessageListInner](docs/V1PropertyGetPost200ResponsePropertyFacilityInfoGuestRoomListInnerMessageListInner.md)
 - [V1PropertyGetPost200ResponsePropertyGeo](docs/V1PropertyGetPost200ResponsePropertyGeo.md)
 - [V1PropertyGetPost200ResponsePropertyGeoDa](docs/V1PropertyGetPost200ResponsePropertyGeoDa.md)
 - [V1PropertyGetPost200ResponsePropertyGeoDe](docs/V1PropertyGetPost200ResponsePropertyGeoDe.md)
 - [V1PropertyGetPost200ResponsePropertyGeoDeLocation](docs/V1PropertyGetPost200ResponsePropertyGeoDeLocation.md)
 - [V1PropertyGetPost200ResponsePropertyGeoEn](docs/V1PropertyGetPost200ResponsePropertyGeoEn.md)
 - [V1PropertyGetPost200ResponsePropertyGeoNl](docs/V1PropertyGetPost200ResponsePropertyGeoNl.md)
 - [V1PropertyGetPost200ResponsePropertyGuestInfo](docs/V1PropertyGetPost200ResponsePropertyGuestInfo.md)
 - [V1PropertyGetPost200ResponsePropertyMediaListInner](docs/V1PropertyGetPost200ResponsePropertyMediaListInner.md)
 - [V1PropertyGetPost200ResponsePropertyMediaListInnerTagListInner](docs/V1PropertyGetPost200ResponsePropertyMediaListInnerTagListInner.md)
 - [V1PropertyGetPost200ResponsePropertyPolicyListInner](docs/V1PropertyGetPost200ResponsePropertyPolicyListInner.md)
 - [V1PropertyGetPost200ResponsePropertyPolicyListInnerPetsPolicy](docs/V1PropertyGetPost200ResponsePropertyPolicyListInnerPetsPolicy.md)
 - [V1PropertyGetPost200ResponsePropertyPolicyListInnerTaxPolicyListInner](docs/V1PropertyGetPost200ResponsePropertyPolicyListInnerTaxPolicyListInner.md)
 - [V1PropertyGetPost200ResponsePropertyPropertyInfo](docs/V1PropertyGetPost200ResponsePropertyPropertyInfo.md)
 - [V1PropertyGetPost200ResponsePropertyPropertyInfoAcceptedPaymentListInner](docs/V1PropertyGetPost200ResponsePropertyPropertyInfoAcceptedPaymentListInner.md)
 - [V1PropertyGetPost200ResponsePropertyPropertyInfoCategoryListInner](docs/V1PropertyGetPost200ResponsePropertyPropertyInfoCategoryListInner.md)
 - [V1PropertyGetPost200ResponsePropertyPropertyInfoLocation](docs/V1PropertyGetPost200ResponsePropertyPropertyInfoLocation.md)
 - [V1PropertyGetPost200ResponsePropertyPropertyInfoMessageListInner](docs/V1PropertyGetPost200ResponsePropertyPropertyInfoMessageListInner.md)
 - [V1PropertyGetPost200ResponsePropertyRecordCreated](docs/V1PropertyGetPost200ResponsePropertyRecordCreated.md)
 - [V1PropertyGetPost200ResponsePropertyRecordModified](docs/V1PropertyGetPost200ResponsePropertyRecordModified.md)
 - [V1PropertyGetPost200ResponsePropertyServiceListInner](docs/V1PropertyGetPost200ResponsePropertyServiceListInner.md)
 - [V1PropertyGetPost200ResponsePropertyTransaction](docs/V1PropertyGetPost200ResponsePropertyTransaction.md)
 - [V1PropertyGetPost200ResponsePropertyTransactionExternalListInner](docs/V1PropertyGetPost200ResponsePropertyTransactionExternalListInner.md)
 - [V1PropertyListPost200Response](docs/V1PropertyListPost200Response.md)
 - [V1PropertyListPost200ResponseListInner](docs/V1PropertyListPost200ResponseListInner.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: apiKey
- **Location**: HTTP header


## Author

support@lodgea.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in lodgea-python.apis and lodgea-python.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from lodgea-python.api.default_api import DefaultApi`
- `from lodgea-python.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import lodgea-python
from lodgea-python.apis import *
from lodgea-python.models import *
```

