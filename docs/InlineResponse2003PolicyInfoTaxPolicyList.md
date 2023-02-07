# InlineResponse2003PolicyInfoTaxPolicyList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **float** | The code that represents the type of tax.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#taxtype-codes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**charge_type** | **str** | The type of charge. | 
**charge_frequency_code** | **float** | The code that represents the frequency of charge.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#chargetype-codes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**currency_code** | **str** | The currency code of the currency in that the charge is applied.&lt;p&gt;See also &lt;a href&#x3D;\&quot;#currencycodes\&quot;&gt;in the appendix&lt;/a&gt;.&lt;/p&gt; | 
**condition_list** | **[str]** | A list of conditions for the tax. Is empty if &lt;code&gt;chargeType&lt;/code&gt; is not &lt;code&gt;conditional&lt;/code&gt;. | 
**percent** | **float** | The charged percentage if applicable. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


