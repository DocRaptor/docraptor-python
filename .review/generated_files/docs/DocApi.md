# docraptor.DocApi

All URIs are relative to *https://api.docraptor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_async_doc**](DocApi.md#create_async_doc) | **POST** /async_docs | 
[**create_doc**](DocApi.md#create_doc) | **POST** /docs | 
[**create_hosted_async_doc**](DocApi.md#create_hosted_async_doc) | **POST** /hosted_async_docs | 
[**create_hosted_doc**](DocApi.md#create_hosted_doc) | **POST** /hosted_docs | 
[**expire**](DocApi.md#expire) | **PATCH** /expire/{id} | 
[**get_async_doc**](DocApi.md#get_async_doc) | **GET** /download/{id} | 
[**get_async_doc_status**](DocApi.md#get_async_doc_status) | **GET** /status/{id} | 


# **create_async_doc**
> AsyncDoc create_async_doc(doc)



Creates a document asynchronously. You must use a callback url or the returned status id and the status API to find out when it completes. Then use the download API to get the document. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import docraptor
from docraptor.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docraptor.com
# See configuration.py for a list of all supported configuration parameters.
configuration = docraptor.Configuration(
    host = "https://api.docraptor.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = docraptor.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with docraptor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docraptor.DocApi(api_client)
    doc = docraptor.Doc() # Doc | The document to be created.

    try:
        api_response = api_instance.create_async_doc(doc)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocApi->create_async_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc** | [**Doc**](Doc.md)| The document to be created. | 

### Return type

[**AsyncDoc**](AsyncDoc.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/pdf, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_doc**
> str create_doc(doc)



Creates a document synchronously. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import docraptor
from docraptor.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docraptor.com
# See configuration.py for a list of all supported configuration parameters.
configuration = docraptor.Configuration(
    host = "https://api.docraptor.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = docraptor.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with docraptor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docraptor.DocApi(api_client)
    doc = docraptor.Doc() # Doc | The document to be created.

    try:
        api_response = api_instance.create_doc(doc)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocApi->create_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc** | [**Doc**](Doc.md)| The document to be created. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/pdf, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hosted_async_doc**
> AsyncDoc create_hosted_async_doc(doc)



Creates a hosted document asynchronously. You must use a callback url or the returned status id and the status API to find out when it completes. Then use the download API to get the document. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import docraptor
from docraptor.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docraptor.com
# See configuration.py for a list of all supported configuration parameters.
configuration = docraptor.Configuration(
    host = "https://api.docraptor.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = docraptor.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with docraptor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docraptor.DocApi(api_client)
    doc = docraptor.Doc() # Doc | The document to be created.

    try:
        api_response = api_instance.create_hosted_async_doc(doc)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocApi->create_hosted_async_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc** | [**Doc**](Doc.md)| The document to be created. | 

### Return type

[**AsyncDoc**](AsyncDoc.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/pdf, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hosted_doc**
> DocStatus create_hosted_doc(doc)



Creates a hosted document synchronously. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import docraptor
from docraptor.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docraptor.com
# See configuration.py for a list of all supported configuration parameters.
configuration = docraptor.Configuration(
    host = "https://api.docraptor.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = docraptor.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with docraptor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docraptor.DocApi(api_client)
    doc = docraptor.Doc() # Doc | The document to be created.

    try:
        api_response = api_instance.create_hosted_doc(doc)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocApi->create_hosted_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc** | [**Doc**](Doc.md)| The document to be created. | 

### Return type

[**DocStatus**](DocStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/pdf, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire**
> expire(id)



Expires a previously created hosted doc. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import docraptor
from docraptor.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docraptor.com
# See configuration.py for a list of all supported configuration parameters.
configuration = docraptor.Configuration(
    host = "https://api.docraptor.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = docraptor.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with docraptor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docraptor.DocApi(api_client)
    id = 'id_example' # str | The download_id returned from status request or hosted document response.

    try:
        api_instance.expire(id)
    except ApiException as e:
        print("Exception when calling DocApi->expire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The download_id returned from status request or hosted document response. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_doc**
> str get_async_doc(id)



Downloads a finished document. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import docraptor
from docraptor.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docraptor.com
# See configuration.py for a list of all supported configuration parameters.
configuration = docraptor.Configuration(
    host = "https://api.docraptor.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = docraptor.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with docraptor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docraptor.DocApi(api_client)
    id = 'id_example' # str | The download_id returned from an async status request or callback.

    try:
        api_response = api_instance.get_async_doc(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocApi->get_async_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The download_id returned from an async status request or callback. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/pdf, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_doc_status**
> DocStatus get_async_doc_status(id)



Check on the status of an asynchronously created document. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import docraptor
from docraptor.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docraptor.com
# See configuration.py for a list of all supported configuration parameters.
configuration = docraptor.Configuration(
    host = "https://api.docraptor.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = docraptor.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with docraptor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docraptor.DocApi(api_client)
    id = 'id_example' # str | The status_id returned when creating an asynchronous document.

    try:
        api_response = api_instance.get_async_doc_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocApi->get_async_doc_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The status_id returned when creating an asynchronous document. | 

### Return type

[**DocStatus**](DocStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/pdf, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

