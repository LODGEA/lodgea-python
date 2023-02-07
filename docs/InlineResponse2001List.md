# InlineResponse2001List


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The properties unique code/ID. | 
**language_code** | **str** | The language code of the language in which the property description is written.&lt;p&gt;Please note that beside the general restrictions listed below only languages configured during system setup for your respective tenant are allowed.&lt;/p&gt;&lt;p&gt;See also &lt;a href&#x3D;\&quot;#isolanguage-codes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**currency_code** | **str** | The currency code for the currency in which prices are returned.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#currencycodes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**unit_system** | **str** | The unit system (either \&quot;metric\&quot; or \&quot;imperial\&quot;) used for measurements. | 
**name** | **str** | The name of the property. | 
**uri** | **str** | A URI for the property. | 
**service_list** | **[float]** | A list of service codes indicating the services and amenities the property has.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#servicecodes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**category_list** | **[float]** | A list of property class type codes indicating the types of the property.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#propertyclass-type-codes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**uri_path** | **str** | A URI path for the property. | 
**text** | **str** | A description of the property. | 
**media_list** | [**[InlineResponse2001MediaList]**](InlineResponse2001MediaList.md) | A list of media objects for the property. | 
**attraction_list** | [**[InlineResponse2001AttractionList]**](InlineResponse2001AttractionList.md) | A list of objects describing the attractions available at the property. | 
**lowest_price** | [**InlineResponse2001LowestPrice**](InlineResponse2001LowestPrice.md) |  | 
**geo** | [**InlineResponse2001Geo**](InlineResponse2001Geo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


