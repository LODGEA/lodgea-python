# InlineResponse2003PropertyServiceList

An object describing the service, its pricing and its availability.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** | The code of this service&lt;p&gt;See also &lt;a href&#x3D;\&quot;#servicecodes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**price** | **float** | The surcharge for this service. | 
**exists** | **bool** | Whether this service is available. | 
**included** | **bool** | Whether this service is complementary. | 
**currency_code** | **str** | The currency of the surcharge for this service | 
**feature_list** | **[str]** | A list of features. | 
**type_list** | **[float]** | A list of codes describing the available breakfast type.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#breakfasttype-codes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**item_list** | **[float]** | A list of codes describing the available breakfast items.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#breakfastitem-codes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**operation_time_list** | [**[InlineResponse2003PropertyOperationTimeList]**](InlineResponse2003PropertyOperationTimeList.md) | A list of operation times, including start and end times, and the days of the week on which the operation is open. | 
**name** | **str** | The name of this service. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


