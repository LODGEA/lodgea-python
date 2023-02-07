# InlineResponse2003PolicyInfo

The policy info for this product.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_in_time** | **float** | Check-in time (unix timestamp in ms). | 
**check_out_time** | **float** | Check-out time (unix timestamp in ms). | 
**cancellation_policy_list** | [**[InlineResponse2003PropertyCancellationPolicyList]**](InlineResponse2003PropertyCancellationPolicyList.md) | List of cancellation policies. | 
**advance_booking_min** | **float** | The minimum number of days in advance a booking must be made | 
**advance_booking_max** | **float** | The maximum number of days in advance a booking can be made | 
**tax_policy_list** | [**[InlineResponse2003PolicyInfoTaxPolicyList]**](InlineResponse2003PolicyInfoTaxPolicyList.md) | A list of taxes and their policies. | 
**fee_policy_list** | [**[InlineResponse2003PolicyInfoFeePolicyList]**](InlineResponse2003PolicyInfoFeePolicyList.md) | A list of fees and their policies. | 
**total_guest_count** | **float** | The maximum number of guests allowed. | [optional] 
**pets_policy** | [**InlineResponse2003PropertyPetsPolicy**](InlineResponse2003PropertyPetsPolicy.md) |  | [optional] 
**prepayment_policy** | **str** | The type of the prepayment policy. | [optional] 
**guarantee_policy** | [**InlineResponse2003PropertyGuaranteePolicy**](InlineResponse2003PropertyGuaranteePolicy.md) |  | [optional] 
**name** | **str** | The name of this policy. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


