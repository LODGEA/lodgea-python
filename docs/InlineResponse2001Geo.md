# InlineResponse2001Geo

A geographical information set describing the location of this property.<br><br>See also <a href=\"#locationtypes\">in the appendix</a>.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The language of the localizable fields ot this geographical information set.&lt;p&gt;Please note that beside the general restrictions listed below only languages configured during system setup for your respective tenant are allowed.&lt;/p&gt;&lt;p&gt;See also &lt;a href&#x3D;\&quot;#isolanguage-codes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**formatted_address** | **str** | The formatted address in the local format of the properties location. | 
**location** | [**InlineResponse2001GeoLocation**](InlineResponse2001GeoLocation.md) |  | 
**place_id** | **str** | Uniquely identifies a place in our database. | 
**route** | **str** | The name of the route or street. | [optional] 
**street_number** | **str** | The number of the street. | [optional] 
**postal_code** | **str** | The postal code of the location. | [optional] 
**locality** | **str** | A city or town. | [optional] 
**sublocality** | **str** | A smaller area within a locality. | [optional] 
**sublocality_level_1** | **str** | A smaller area within a locality at level 1. | [optional] 
**sublocality_level_2** | **str** | A smaller area within a locality at level 2. | [optional] 
**sublocality_level_3** | **str** | A smaller area within a locality at level 3. | [optional] 
**sublocality_level_4** | **str** | A smaller area within a locality at level 4. | [optional] 
**sublocality_level_5** | **str** | A smaller area within a locality at level 5. | [optional] 
**administrative_area_level_1** | **str** | A level 1 administrative area, such as a state or province. | [optional] 
**administrative_area_level_2** | **str** | A level 2 administrative area. | [optional] 
**administrative_area_level_3** | **str** | A level 3 administrative area | [optional] 
**administrative_area_level_4** | **str** | A level 4 administrative area. | [optional] 
**administrative_area_level_5** | **str** | A level 5 administrative area | [optional] 
**state_code** | **str** | The state or province code for the administrative area. | [optional] 
**country** | **str** | The country of this geographical information set. | [optional] 
**country_code** | **str** | The country code for the country. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


