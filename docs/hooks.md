# Hooks

Webhooks are meant to commit a request somewhere when some event is being started.

They **works only for documents**.

We have implemented webhooks as our needs were, but fill free to send us a feedback if you see something we missed.

## Hook properties

	{
	    "_id": "57114ee832d2c668de756b5d",
	    "collection": "_files",
	    "condition": {
	        "additionalProperties": true,
	        "properties": {
	            "name": {
	                "enum": [
	                    "small.jpg"
	                ],
	                "type": "string"
	            }
	        },
	        "type": "object"
	    },
	    "headers": {
	        "Authorization": "Bearer <secret-value>",
	        "Content-Type": "application/json"
	    },
	    "method": "GET",
	    "name": "files_hook",
	    "triggers": [
	        "created"
	    ],
	    "url": "https://example.com/url-to-post-to"
	}


Property                | Type          | Description
------------------------|---------------|-------------
_id                     | string        | id of a project
name                    | string        | name of a project
collection              | string        | collection which contains a documents called hook to trigger
condition               | object        | condition of a successful hook trigger
headers                 | object        | http request headers
method                  | string        | http method to commit a request
triggers                | array         | document event to trigger a hook
request_payload_wrapper | string        | name of `payload` property
url                     | string        | url to commit a http request


### collection

All documents from this collection will be used to be a hook trigger

### condition

This is a schema. If a document which triggered this hook matches this `condition` schema - this hook will commit an operation, otherwise it won't.

If you want all documents to trigger a hook - make it's value equal a

    {
        "type": "object",
        "additionalProperties": true
    }

All documents will match this schema and a hook will trigger

### headers

Hook will contain these headers in a request:

Header              | Description
------------------- | ------------
X-Hook-ID           | `_id`  of a hook
X-Hook-Trigger      | event` of a document which caused hook to trigger
X-Hook-Operation-ID | operation `_id` of a hook. Can be found in a `_hooks_history`

If `method` is `PUT`, `PATCH` or `POST`:

Header         | Value              | Description
-------------- | ------------------ | ------------
Content-Type   | `application/json` | Body will contain document's JSON
Content-Length |                    | Length of document's JSON

In some cases you may need a webhook to pass a custom header with a request it commits.

### method

A **method** is being used to commit a HTTP Request. Valud values are `GET`, `POST`, `DELETE` or `PUT`.

Method |  Body | Content-Type
-------|:-----:|------------------
PUT    | *     | `application/json`
PATCH  | *     | `application/json`
POST   | *     | `application/json`
GET    |       |
DELETE |       |


In some cases you may need a webhook to `PUT` a processed document to your cache or database.

### triggers

When a document event matches `created`, `updated`, `deleted` the webhook triggers.

### request_payload_wrapper

By default a payload of a webhook is wrapped to `payload` property. 

Sometimes you may need it to be a different root property.
