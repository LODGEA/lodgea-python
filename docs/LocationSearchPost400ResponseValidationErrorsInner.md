# LocationSearchPost400ResponseValidationErrorsInner

A Zod issue. More fields can be present depending on the issue type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The ZodIssueCode describing the issue. | 
**message** | **str** | A message describing the error in a human readable way. | 
**path** | **[str]** | An array describing the position of the faulty property. The first segment will always be either \&quot;body\&quot;, \&quot;pathParameters\&quot; or \&quot;queryParameters\&quot; indicating on which part of your request the error occurred. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


