# Adobe Analytics API
 This is a Python wrapper for Adobe Analytics APIs v 1.4. By default, it points to San Jose data center https://api.omniture.com/admin/1.4/rest/ but for the best API performance, you should update the configuration according to the data center your company is in.

##### From Adobe documentation:
_For the best API performance, it is important to use the correct endpoint. The correct endpoint can be obtained by calling Company.GetEndpoint. Our best practice is to call Company.GetEndpoint in your production applications and then use the returned endpoint in all your subsequent API requests. This is important if your company is migrated to another data center._

_For example, if your company was migrated from the San Jose data center to the Singapore data center, you need to replace api.omniture.com with api4.omniture.com as shown below. If you do not update this endpoint, your API requests will have unnecessary latency added due to the jumps between the San Jose and Singapore data centers._

- _api.omniture.com - San Jose_
- _api2.omniture.com - Dallas_
- _api3.omniture.com - London_
- _api4.omniture.com - Singapore_
- _api5.omniture.com - Pacific Northwest_


### Important links:
- [API explorer](
  https://marketing.adobe.com/developer/api-explorer)
- [API documentation](
https://marketing.adobe.com/developer/documentation)


 ### Supported APIs with example calls:
[Analytics Reporting](
https://marketing.adobe.com/developer/documentation/analytics-reporting-1-4/get-started)

```Python
params = {
    'reportSuiteID': REPORT_SUITE,
    'reportType': 'any'
}
report_elements = request_to_api(ADOBE_CREDENTIALS.get('user_name'), ADOBE_CREDENTIALS.get(
    'secret'), 'Report.GetElements', params)
```

[Analytics Administration](
https://marketing.adobe.com/developer/documentation/analytics-administration-1-4/admin-api)
```Python
props = request_to_api(ADOBE_CREDENTIALS.get('user_name'), ADOBE_CREDENTIALS.get(
    'secret'), 'ReportSuite.GetProps', {'rsid_list': [REPORT_SUITE]})
```
```Python
login_name = 'user.surname'
result = request_to_api(ADOBE_CREDENTIALS.get('user_name'), ADOBE_CREDENTIALS.get(
    'secret'), 'Permissions.DeleteLogin', {'login': login_name})
if result:
    print('User {} deleted'.format(login_name))
```

[Classifications](
https://marketing.adobe.com/developer/documentation/classifications-1-4-saint/classifications-api)
```Python
params = {
    'all_rows': 'true',
    'date_filter_end_date': 'Jun 2017',
    'date_filter_start_date': 'May 2017',
    'element': 'evar15',
    'email_address': 'your@email.com',
    'encoding': 'UTF-8',
    'rsid_list': [
        REPORT_SUITE
    ]
}

classification_export_job = request_to_api(ADOBE_CREDENTIALS.get('user_name'), ADOBE_CREDENTIALS.get(
    'secret'), 'Classifications.CreateExport', params)
```


[Data Feeds](
https://marketing.adobe.com/developer/documentation/data-feeds/overview)

```Python
params = {
    'rsid_list': [
        REPORT_SUITE
    ],
    'status': [
        'processing'
    ]
}

data_feeds = request_to_api(ADOBE_CREDENTIALS.get('user_name'), ADOBE_CREDENTIALS.get(
    'secret'), 'DataFeed.GetFeeds', params)
```

[Data Sources](
https://marketing.adobe.com/developer/documentation/data-sources/c-data-sources-api)
```Python
data_sources = request_to_api(ADOBE_CREDENTIALS.get('user_name'), ADOBE_CREDENTIALS.get(
    'secret'), 'DataSources.Get', {'reportSuiteID': REPORT_SUITE})
```

[Segments](
https://marketing.adobe.com/developer/documentation/segments-1-4/segments-api)
```Python
params = {
    'accessLevel': 'owned',
    'fields': [
        'reportSuiteID',
        'definition'
    ],
    'filters': {
        'reportSuiteID': REPORT_SUITE,
    },
    'sort': 'name'
}

my_segments = request_to_api(ADOBE_CREDENTIALS.get('user_name'), ADOBE_CREDENTIALS.get(
    'secret'), 'Segments.Get', params)
```
