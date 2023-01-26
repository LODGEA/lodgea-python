# PropertiesPropertyIdGet200ResponseProductListInner

A list of available products for this property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | The ID of the property. | 
**name** | **str** | The name of the product. | 
**meal_plan_list** | **[float]** | A list of meal type codes included in this product. | 
**room_type_list** | **[str]** | An array of strings describing the room types included in this product. | 
**rate_plan_list** | [**[PropertiesPropertyIdGet200ResponseProductListInnerRatePlanListInner]**](PropertiesPropertyIdGet200ResponseProductListInnerRatePlanListInner.md) | The rate plans for this product. | 
**is_los_pricing** | **bool** | Whether this product is length of stay pricing. | [optional] 
**is_obp_pricing** | **bool** | Whether this product is occupancy based pricing. | [optional] 
**policy_info** | [**PropertiesPropertyIdGet200ResponseProductListInnerPolicyInfo**](PropertiesPropertyIdGet200ResponseProductListInnerPolicyInfo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


