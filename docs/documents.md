# Documents

The `document` is a simple JSON entity. It is stored in a [collection](/collections/).

## Features

Feature        | Description
---------------|--------------------------
[storage](/documents/#storage)       | attach files to documents
[validation](/documents/#validation) | validate a document
[processing](/documents/#processing) | process a document according collection's schema
[hooks](/documents/#hooks)           | trigger a hook after document event


### storage

You can upload files with data to your document in a single request.

It will create a document with a file reference. File will be saved as a document to [_files](/files/) collection.

Create a document using [cli-deform](https://github.com/deformio/cli-deform):

```bash
deform document create -c users -d '{
	"name": "Andrey",
	"avatar": @"/home/andrey/files/avatar.jpg"
}'
```

```bash
deform documents find -c users -f '{"name": "Andrey"}' --pretty

{
	"_id": "574d48cf32d2c69274322585",
	"name": "andrey",
	"avatar": {
	    "_id": "574c9a266dff87000562eaf6",
	    "collection_id": "users",
	    "content_type": "image/png",
	    "date_created": "2016-05-31T19:53:10.43Z",
	    "document_id": "574d48cf32d2c69274322585",
	    "last_access": "2016-05-31T19:53:10.43Z",
	    "md5": "a6a859273c133cdf168295a3b7d83a0f",
	    "name": "avatar.png",
	    "size": 3421
	}
}
```

Also a `_files` collection will contain a file document.

```bash
deform documents find -c _files -f '{"_id": "574c9a266dff87000562eaf6"}' --pretty

{
    "_id": "574c9a266dff87000562eaf6",
    "collection_id": "users",
    "content_type": "image/png",
    "date_created": "2016-05-31T19:53:10.43Z",
    "document_id": "574d48cf32d2c69274322585",
    "last_access": "2016-05-31T19:53:10.43Z",
    "md5": "a6a859273c133cdf168295a3b7d83a0f",
    "name": "avatar.png",
    "size": 3421
}
```


### validation

We are using JSON Schema [customized](/schemas/) draft v4.

Schema validation:

	{
		"type": "object",
		"properties": {
			"integer_price": {
				"type": "integer"
			},
			"float_price": {
				"type": "number"
			}
		}
	}

Document              | Valid 
----------------------|--------
{"integer_price": 1.2}|
{"integer_price": 1}  | *
{"float_price": 1.2}  | *
{"float_price": 1}    | *


### processing

### hooks

Document can trigger a [hook](/hooks/).

Hooks has `triggers` property of type array. 

Every document operation via interfaces pushes this event to hook's queue.

HTTP Method     | Hook trigger
----------------|--------------
`POST`          | `created`
`PATCH`         | `updated`
`DELETE`        | `deleted`
`PUT`           | `updated`. If document exists
`PUT`           | `created`. If document does not exist

Cli-Deform method | Hook trigger
---------------------|-------------

Python-Deform method | Hook trigger
---------------------|-------------


## Example usage

We need to receive a slack notification every time new user registers in one of our services.

There are 4 steps to achieve the result:

  * create a collection for users. `users`
  * create a collection for slack notifications. `slack_notifications`
  * add a webhook for `user` document creation. Hook will send it `slack_notifications`
  * add a webhook for `slack_notifications` document creation. Hook will send it to [Slack](https://slack.com).

Let's use [cli-deform](https://github.com/deformio/cli-deform). 

### step 1

Create a collection for users.

```bash
deform collection create -d '{
	"_id": "users", 
	"name":"users", 
	"schema": {
		"type": "object",
		"properties": {
			"username": {
				"type": "string"
			},
			"email": {
				"type": "string"
			},
			"avatar": {
				"type": "string"
			}
		}
	}
}'
```

### step 2

Create a collection for slack notifications.

```bash
deform collection create -d '{
    "_id": "slack_notifications",
    "name": "Slack Notifications",
    "schema": {
        "title": "Slack specific hook wrapper",
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "processors": [
                    {
                        "name": "template",
                        "in": {
                            "context": {
                                "profile": {
                                    "property": "user"
                                }
                            },
                            "syntax": {
                                "value": "handlebars"
                            },
                            "template_string": {
                                "value": "{{#if profile}} Welcome <{{profile.username}}>{{/if}}"
                            }
                        }
                    }
                ]
            },
            "user": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string"
                    }
                },
                "additionalProperties": true
            }
        }
    }
}'
```

### step 3

Add a hook for new user registration. We must insert his data to `slack_notifications` collection. 

```bash
deform document save -c _hooks -d '{
	"_id": "user_registered",
    "name": "User joined",
    "url": "https://YOUR_PROJECT.deform.io/api/collections/slack_notifications/documents/",
    "request_payload_wrapper": "payload",
    "method": "PUT",
    "triggers": ["created"],
    "collection": "users",
    "headers": {
        "Authorization": "Token slack_notifications_creation_token"
    }
}'
```

Notes:

  * `method` set to `PUT`. This will create or update existing slack notification. 
  * `url` set to our collection `slack_notifications`
  * `triggers` set to `created`. Only new users will trigger this hook
  * `headers` has an item with `AUTHORIZATION` header. We recommend you to create a [token](/tokens/) allowed to `create` documents inside of `slack_notifications` collection.

        deform document save -c _tokens -d '{
            "_id": "slack_notifications_creation_token",
            "name": "Slack notification",
            "is_active": true,
            "permission": {
	            "allow": {
	                "create": [
	                    {
	                        "what": "document",
	                        "where": "slack_notifications"
	                    }
	                ]
	            }
	        }
        }'


### step 4


Now we need to create a hook for `slack_notifications` collection. 

It will send a document to a [Slack](https://slack.com).

```bash
deform document save -c _hooks -d '{
	"_id": "send_slack_notification",
    "name": "Slack notification",
    "url": "https://hooks.slack.com/services/YOUR_SLACK_DETAILS",
    "method": "POST",
    "triggers": ["created"],
    "collection": "slack_notifications"
}'
```

Notes:

  * `url` replace to a correct slack webhook url.


### How does it work.

New User registation in your service causes a document to be `created` inside `users` collection.

Collection `users` has a hook triggering by `create` event. This hook will commit a HTTP Request:
   
   * use a HTTP Method `PUT` to **create or update**
   * use a `Authorization` header
   * send a document to a `slack_notifications` collection

Collection `slack_notifications` has a hook triggering by `create` event. This hook will send a document directly to a [Slack](https://slack.com)

In a few moments you will get a Slack notification.
