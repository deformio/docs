# Debug

Debug writes all requests and their's responses into `_debug` system collection.

All HTTP Requests except Files will be cached.

To turn toggle it - set your project's `settings.debug` to `true` or `false`

## Debug properties

    {
        "_id": "5760307d32d2c6ce9b2c5ff7",
        "date_created": "2016-06-14T16:27:41Z",
        "request": {
            "body": null,
            "headers": {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Token 5760305432d2c6ce9b2c5f91",
                "Connection": "keep-alive",
                "User-Agent": "python-requests/2.10.0"
            },
            "method": "GET",
            "url": "/collections/_notifications/documents/"
        },
        "response": {
            "body": {
                "items": [
                    {
                        "_id": "WxRfMtBQUwfZoKxn",
                        "author": "System",
                        "date_sent": "2016-06-14T17:14:33Z",
                        "message": "Debug is turned on",
                        "subject": "Debug mode changed"
                    }
                ],
                "links": {
                    "first": "https://CJJPKADFFO.deform.io/api/collections/_notifications/documents/?page=1",
                    "last": "",
                    "next": "",
                    "prev": ""
                },
                "message": "",
                "page": 1,
                "pages": 1,
                "perpage": 100,
                "total": 1
            },
            "headers": {
                "Content-Length": "300",
                "Content-Type": "application/json; charset=utf-8"
            },
            "status_code": 200,
            "time_took": 0.0057844640000000004
        }
    }


Property                  | Type          | Description
--------------------------|---------------|-------------
\_id                      | string        | unique identity of the debug document
date\_created             | datetime      | date the document was created
request                   | object        | request details
response                  | object        | response details


### request

Property                  | Type                    | Description
--------------------------|-------------------------|-------------
body                      | object, string, null    | body of a request
headers                   | object                  | request headers
method                    | string                  | request method
url                       | string                  | request url


#### request.body

Payload which was sent in a request body.

#### request.headers

Headers used in a request

#### request.method

Method used: "GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"

#### request.url

Url of a request.


### response

Property                  | Type                    | Description
--------------------------|-------------------------|-------------
body                      | object, string, null    | body of a response
headers                   | object                  | response headers
status_code               | integer                 | response status code
time_took                 | number                  | time took since request was accepted


#### response.body

Response body

#### response.headers

Response headers

#### response.status_code

Status code of a response

#### response.time_took

Time took since request was accepted. **Seconds**
