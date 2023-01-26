# PropertiesPropertyIdGet200ResponsePropertyPropertyInfo

General information regarding the property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_list** | [**[PropertiesPropertyIdGet200ResponsePropertyPropertyInfoMessageListInner]**](PropertiesPropertyIdGet200ResponsePropertyPropertyInfoMessageListInner.md) | Contains a descriptive message for this property in all supported languages. | 
**category_list** | **[float]** | A list of code of the property class types that apply to the property. | 
**language_list** | **[str]** | The codes of languages the staff of this property can speak. Please note that these codes partially differ from the two character ISO language codes widely used throughout the API as they partially include country specific language code.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#languagecountry-code\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**accepted_payment_list** | [**[PropertiesPropertyIdGet200ResponsePropertyPropertyInfoAcceptedPaymentListInner]**](PropertiesPropertyIdGet200ResponsePropertyPropertyInfoAcceptedPaymentListInner.md) | A list of the accepted payment methods. Payment methods might subject to frequent change as payment providers come and go. You should always implement a way to handle new, unexpected payment methods.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#paymenttypes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**unit_count** | **float** | The amount of units the property has. | [optional] 
**location** | [**AvailablePropertiesInner1GeoLocation**](AvailablePropertiesInner1GeoLocation.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


