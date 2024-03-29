# Doc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for identifying your document. | 
**document_type** | **str** | The type of document being created. | 
**document_content** | **str** | The HTML data to be transformed into a document. You must supply content using document_content or document_url.  | [optional] 
**document_url** | **str** | The URL to fetch the HTML data to be transformed into a document. You must supply content using document_content or document_url.  | [optional] 
**test** | **bool** | Enable test mode for this document. Test documents are not charged for but include a watermark. | [optional] [default to True]
**pipeline** | **str** | Specify a specific verison of the DocRaptor Pipeline to use. | [optional] 
**strict** | **str** | Force strict HTML validation. | [optional] 
**ignore_resource_errors** | **bool** | Failed loading of images/javascripts/stylesheets/etc. will not cause the rendering to stop. | [optional] [default to True]
**ignore_console_messages** | **bool** | Prevent console.log from stopping document rendering during JavaScript execution. | [optional] [default to False]
**tag** | **str** | A field for storing a small amount of metadata with this document. | [optional] 
**help** | **bool** | Request support help with this request if it succeeds. | [optional] [default to False]
**javascript** | **bool** | Enable DocRaptor JavaScript parsing. PrinceXML JavaScript parsing is also available elsewhere. | [optional] [default to False]
**referrer** | **str** | Set HTTP referrer when generating this document. | [optional] 
**callback_url** | **str** | A URL that will receive a POST request after successfully completing an asynchronous document. The POST data will include download_url and download_id similar to status API responses. WARNING: this only works on asynchronous documents.  | [optional] 
**hosted_download_limit** | **int** | The number of times a hosted document can be downloaded.  If no limit is specified, the document will be available for an unlimited number of downloads. | [optional] 
**hosted_expires_at** | **str** | The date and time at which a hosted document will be removed and no longer available. Must be a properly formatted ISO 8601 datetime, like 1981-01-23T08:02:30-05:00. | [optional] 
**prince_options** | [**PrinceOptions**](PrinceOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


