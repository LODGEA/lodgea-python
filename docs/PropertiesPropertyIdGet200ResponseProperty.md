# PropertiesPropertyIdGet200ResponseProperty

An object containing all available base data for the requested property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The properties unique identifier. | 
**name** | **str** | The properties name. | 
**record_created** | [**PropertiesPropertyIdGet200ResponsePropertyRecordCreated**](PropertiesPropertyIdGet200ResponsePropertyRecordCreated.md) |  | 
**record_modified** | [**PropertiesPropertyIdGet200ResponsePropertyRecordModified**](PropertiesPropertyIdGet200ResponsePropertyRecordModified.md) |  | 
**property_info** | [**PropertiesPropertyIdGet200ResponsePropertyPropertyInfo**](PropertiesPropertyIdGet200ResponsePropertyPropertyInfo.md) |  | 
**award_list** | [**[PropertiesPropertyIdGet200ResponsePropertyAwardListInner]**](PropertiesPropertyIdGet200ResponsePropertyAwardListInner.md) | A list of the ratings available for this property. | 
**contact_list** | [**[PropertiesPropertyIdGet200ResponsePropertyContactListInner]**](PropertiesPropertyIdGet200ResponsePropertyContactListInner.md) | A contact with a profile type and a list of addresses | 
**media_list** | [**[PropertiesPropertyIdGet200ResponsePropertyFacilityInfoGuestRoomListInnerMediaListInner]**](PropertiesPropertyIdGet200ResponsePropertyFacilityInfoGuestRoomListInnerMediaListInner.md) | A list of media objects for the property. | 
**published** | **bool** | Indicates whether the policy has been published or not. | 
**policy_list** | [**[PropertiesPropertyIdGet200ResponsePropertyPolicyListInner]**](PropertiesPropertyIdGet200ResponsePropertyPolicyListInner.md) | A list of policies associated with the property. | 
**service_list** | [**[PropertiesPropertyIdGet200ResponsePropertyServiceListInner]**](PropertiesPropertyIdGet200ResponsePropertyServiceListInner.md) | A list of objects each describing an available service, its pricing and its availability. | 
**guest_info** | [**PropertiesPropertyIdGet200ResponsePropertyGuestInfo**](PropertiesPropertyIdGet200ResponsePropertyGuestInfo.md) |  | [optional] 
**facility_info** | [**PropertiesPropertyIdGet200ResponsePropertyFacilityInfo**](PropertiesPropertyIdGet200ResponsePropertyFacilityInfo.md) |  | [optional] 
**geo** | [**{str: (AvailablePropertiesInner1Geo,)}**](AvailablePropertiesInner1Geo.md) | An object containing language codes as keys and objects describing the properties geographical location as values. | [optional] 
**uri** | **str** | A unique identifier for the accommodation. | [optional] 
**cancellation_grace_period** | [**PropertiesPropertyIdGet200ResponsePropertyCancellationGracePeriod**](PropertiesPropertyIdGet200ResponsePropertyCancellationGracePeriod.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


