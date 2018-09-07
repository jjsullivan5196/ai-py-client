# swagger_client.DefaultApi

All URIs are relative to *https://api.applicationinsights.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](DefaultApi.md#get_event) | **GET** /apps/{app-id}/events/{event-type}/{event-id} | Get an event
[**get_events**](DefaultApi.md#get_events) | **GET** /apps/{app-id}/events/{event-type} | Execute OData query
[**get_events_metadata_o_data**](DefaultApi.md#get_events_metadata_o_data) | **GET** /apps/{app-id}/events/$metadata | Get OData metadata
[**get_metric**](DefaultApi.md#get_metric) | **GET** /apps/{app-id}/metrics/{metric-id} | Retrieve metric data
[**get_metrics**](DefaultApi.md#get_metrics) | **POST** /apps/{app-id}/metrics | Retrieve metric data
[**get_metrics_metadata**](DefaultApi.md#get_metrics_metadata) | **GET** /apps/{app-id}/metrics/metadata | Retrieve metric metatadata
[**get_query**](DefaultApi.md#get_query) | **GET** /apps/{app-id}/query | Execute an Analytics query
[**get_query_schema**](DefaultApi.md#get_query_schema) | **GET** /apps/{app-id}/query/schema | Get Analytics query metadata
[**query**](DefaultApi.md#query) | **POST** /apps/{app-id}/query | Execute an Analytics query


# **get_event**
> EventsResults get_event(app_id, event_type, event_id, timespan=timespan)

Get an event

Gets the data for a single event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.
event_type = 'event_type_example' # str | The type of events to query; either a standard event type (`traces`, `customEvents`, `pageViews`, `requests`, `dependencies`, `exceptions`, `availabilityResults`) or `$all` to query across all event types.
event_id = 'event_id_example' # str | ID of event.
timespan = 'timespan_example' # str | Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression. (optional)

try:
    # Get an event
    api_response = api_instance.get_event(app_id, event_type, event_id, timespan=timespan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 
 **event_type** | **str**| The type of events to query; either a standard event type (&#x60;traces&#x60;, &#x60;customEvents&#x60;, &#x60;pageViews&#x60;, &#x60;requests&#x60;, &#x60;dependencies&#x60;, &#x60;exceptions&#x60;, &#x60;availabilityResults&#x60;) or &#x60;$all&#x60; to query across all event types. | 
 **event_id** | [**str**](.md)| ID of event. | 
 **timespan** | **str**| Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression. | [optional] 

### Return type

[**EventsResults**](EventsResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json;odata=none, application/json;odata=minimal, application/json;odata=full

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> EventsResults get_events(app_id, event_type, timespan=timespan, filter=filter, search=search, orderby=orderby, select=select, skip=skip, top=top, format=format, count=count, apply=apply)

Execute OData query

Executes an OData query for events

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.
event_type = 'event_type_example' # str | The type of events to query; either a standard event type (`traces`, `customEvents`, `pageViews`, `requests`, `dependencies`, `exceptions`, `availabilityResults`) or `$all` to query across all event types.
timespan = 'timespan_example' # str | Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression. (optional)
filter = 'filter_example' # str | An expression used to filter the returned events (optional)
search = 'search_example' # str | A free-text search expression to match for whether a particular event should be returned (optional)
orderby = 'orderby_example' # str | A comma-separated list of properties with \\\"asc\\\" (the default) or \\\"desc\\\" to control the order of returned events (optional)
select = 'select_example' # str | Limits the properties to just those requested on each returned event (optional)
skip = 56 # int | The number of items to skip over before returning events (optional)
top = 56 # int | The number of events to return (optional)
format = 'format_example' # str | Format for the returned events (optional)
count = true # bool | Request a count of matching items included with the returned events (optional)
apply = 'apply_example' # str | An expression used for aggregation over returned events (optional)

try:
    # Execute OData query
    api_response = api_instance.get_events(app_id, event_type, timespan=timespan, filter=filter, search=search, orderby=orderby, select=select, skip=skip, top=top, format=format, count=count, apply=apply)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 
 **event_type** | **str**| The type of events to query; either a standard event type (&#x60;traces&#x60;, &#x60;customEvents&#x60;, &#x60;pageViews&#x60;, &#x60;requests&#x60;, &#x60;dependencies&#x60;, &#x60;exceptions&#x60;, &#x60;availabilityResults&#x60;) or &#x60;$all&#x60; to query across all event types. | 
 **timespan** | **str**| Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression. | [optional] 
 **filter** | **str**| An expression used to filter the returned events | [optional] 
 **search** | **str**| A free-text search expression to match for whether a particular event should be returned | [optional] 
 **orderby** | **str**| A comma-separated list of properties with \\\&quot;asc\\\&quot; (the default) or \\\&quot;desc\\\&quot; to control the order of returned events | [optional] 
 **select** | **str**| Limits the properties to just those requested on each returned event | [optional] 
 **skip** | **int**| The number of items to skip over before returning events | [optional] 
 **top** | **int**| The number of events to return | [optional] 
 **format** | **str**| Format for the returned events | [optional] 
 **count** | **bool**| Request a count of matching items included with the returned events | [optional] 
 **apply** | **str**| An expression used for aggregation over returned events | [optional] 

### Return type

[**EventsResults**](EventsResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;odata=none, application/json;odata=minimal, application/json;odata=full

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_metadata_o_data**
> object get_events_metadata_o_data(app_id)

Get OData metadata

Gets OData EDMX metadata describing the event data model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.

try:
    # Get OData metadata
    api_response = api_instance.get_events_metadata_o_data(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_events_metadata_o_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 

### Return type

**object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/xml;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metric**
> MetricsResult get_metric(app_id, metric_id, timespan=timespan, interval=interval, aggregation=aggregation, segment=segment, top=top, orderby=orderby, filter=filter)

Retrieve metric data

Gets metric values for a single metric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.
metric_id = 'metric_id_example' # str | ID of the metric. This is either a standard AI metric, or an application-specific custom metric.
timespan = 'PT12H' # str | The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of `PT12H` (\"last 12 hours\") is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response. (optional) (default to PT12H)
interval = 'interval_example' # str | The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response. (optional)
aggregation = 'PT12H' # str | The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of `PT12H` (\"last 12 hours\") is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response. (optional) (default to PT12H)
segment = ['segment_example'] # list[str] | The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter. (optional)
top = 56 # int | The number of segments to return.  This value is only valid when segment is specified. (optional)
orderby = 'orderby_example' # str | The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified. (optional)
filter = 'filter_example' # str | An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving. (optional)

try:
    # Retrieve metric data
    api_response = api_instance.get_metric(app_id, metric_id, timespan=timespan, interval=interval, aggregation=aggregation, segment=segment, top=top, orderby=orderby, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 
 **metric_id** | **str**| ID of the metric. This is either a standard AI metric, or an application-specific custom metric. | 
 **timespan** | **str**| The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of &#x60;PT12H&#x60; (\&quot;last 12 hours\&quot;) is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response. | [optional] [default to PT12H]
 **interval** | **str**| The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response. | [optional] 
 **aggregation** | **str**| The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of &#x60;PT12H&#x60; (\&quot;last 12 hours\&quot;) is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response. | [optional] [default to PT12H]
 **segment** | [**list[str]**](str.md)| The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter. | [optional] 
 **top** | **int**| The number of segments to return.  This value is only valid when segment is specified. | [optional] 
 **orderby** | **str**| The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified. | [optional] 
 **filter** | **str**| An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving. | [optional] 

### Return type

[**MetricsResult**](MetricsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics**
> MetricsResults get_metrics(app_id, body)

Retrieve metric data

Gets metric values for multiple metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.
body = swagger_client.MetricsPostBody() # MetricsPostBody | The batched metrics query.

try:
    # Retrieve metric data
    api_response = api_instance.get_metrics(app_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 
 **body** | [**MetricsPostBody**](MetricsPostBody.md)| The batched metrics query. | 

### Return type

[**MetricsResults**](MetricsResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_metadata**
> object get_metrics_metadata(app_id)

Retrieve metric metatadata

Gets metadata describing the available metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.

try:
    # Retrieve metric metatadata
    api_response = api_instance.get_metrics_metadata(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_metrics_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 

### Return type

**object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query**
> QueryResults get_query(app_id, query=query, timespan=timespan, applications=applications)

Execute an Analytics query

Executes an Analytics query for data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.
query = 'query_example' # str | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) (optional)
timespan = 'timespan_example' # str | Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression. (optional)
applications = ['applications_example'] # list[str] | Application IDs to include in cross-application queries. (optional)

try:
    # Execute an Analytics query
    api_response = api_instance.get_query(app_id, query=query, timespan=timespan, applications=applications)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 
 **query** | **str**| The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) | [optional] 
 **timespan** | **str**| Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression. | [optional] 
 **applications** | [**list[str]**](str.md)| Application IDs to include in cross-application queries. | [optional] 

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_schema**
> object get_query_schema(app_id)

Get Analytics query metadata

Gets Analytics query schema describing the data model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.

try:
    # Get Analytics query metadata
    api_response = api_instance.get_query_schema(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_query_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 

### Return type

**object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> QueryResults query(app_id, body=body, timespan=timespan)

Execute an Analytics query

Executes an Analytics query for data. [Here](/documentation/2-Using-the-API/Query) is an example for using POST with an Analytics query.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: azure_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the application. This is Application ID from the API Access settings blade in the Azure portal.
body = swagger_client.QueryBody() # QueryBody | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) (optional)
timespan = 'timespan_example' # str | Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression. (optional)

try:
    # Execute an Analytics query
    api_response = api_instance.query(app_id, body=body, timespan=timespan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the application. This is Application ID from the API Access settings blade in the Azure portal. | 
 **body** | [**QueryBody**](QueryBody.md)| The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) | [optional] 
 **timespan** | **str**| Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression. | [optional] 

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

