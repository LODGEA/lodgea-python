# InlineResponse2003Property

An object containing all available base data for the requested property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The properties unique identifier. | 
**name** | **str** | The properties name. | 
**record_created** | [**InlineResponse2003PropertyRecordCreated**](InlineResponse2003PropertyRecordCreated.md) |  | 
**record_modified** | [**InlineResponse2003PropertyRecordModified**](InlineResponse2003PropertyRecordModified.md) |  | 
**property_info** | [**InlineResponse2003PropertyPropertyInfo**](InlineResponse2003PropertyPropertyInfo.md) |  | 
**award_list** | [**[InlineResponse2003PropertyAwardList]**](InlineResponse2003PropertyAwardList.md) | A list of the ratings available for this property. | 
**contact_list** | [**[InlineResponse2003PropertyContactList]**](InlineResponse2003PropertyContactList.md) | A contact with a profile type and a list of addresses | 
**media_list** | [**[InlineResponse2003PropertyMediaList]**](InlineResponse2003PropertyMediaList.md) | A list of media objects for the property. | 
**published** | **bool** | Indicates whether the policy has been published or not. | 
**policy_list** | [**[InlineResponse2003PropertyPolicyList]**](InlineResponse2003PropertyPolicyList.md) | A list of policies associated with the property. | 
**service_list** | [**[InlineResponse2003PropertyServiceList]**](InlineResponse2003PropertyServiceList.md) | A list of objects each describing an available service, its pricing and its availability. | 
**guest_info** | [**InlineResponse2003PropertyGuestInfo**](InlineResponse2003PropertyGuestInfo.md) |  | [optional] 
**facility_info** | [**InlineResponse2003PropertyFacilityInfo**](InlineResponse2003PropertyFacilityInfo.md) |  | [optional] 
**geo** | [**{str: (InlineResponse2001Geo,)}**](InlineResponse2001Geo.md) | An object containing language codes as keys and objects describing the properties geographical location as values. | [optional] 
**uri** | **str** | A unique identifier for the accommodation. | [optional] 
**cancellation_grace_period** | [**InlineResponse2003PropertyCancellationGracePeriod**](InlineResponse2003PropertyCancellationGracePeriod.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


