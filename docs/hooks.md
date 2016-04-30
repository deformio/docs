# Hooks

Webhooks are meant to commit a request somewhere when some event is being started.

They **works only for documents**.

We have implemented webhooks as our needs were, but fill free to send us a feedback if you see something we missed.

## Features

### Headers

Hook has a property `headers`. 

Every webhook will these headers in a request:
  
  * `X-Hook-ID` - `_id` of a hook
  * `X-Hook-Trigger` - `event` of a document which caused hook to trigger
  * `X-Hook-Operation-ID` - operation `_id` of a hook. Can be found in a `_hooks_history`

In case of method equals `PUT`, `PATCH` or `POST`:

  * Header `Content-Type` will always be `application/json`
  * Header `Content-Length` will be passed with length of a payload

In some cases you may need a webhook to pass a custom header with a request it commits.

### Methods

This Method is being used to commit a HTTP Request.

Hook has a property `method`. Possible values are `["GET", "POST", "DELETE", "PUT"]`. 

Methods `PUT`, `PATCH`, `POST` will contain a body. 

Methods `GET`, `DELETE` will not contain a body.

In some cases you may need a webhook to `PUT` a processed document to your cache or database with REST.

### Events

Hook has a property `triggers`. When a document event matches `["created", "updated", "deleted"]` the webhook triggers.

### Wrapper

Hook has a property `request_payload_wrapper`. By default a payload of a webhook is wrapped to `payload` property. 

Sometimes you may need it to be a different root property.

### Condition

Hook has a property `condition`. This is a schema. If a document which triggered this hook matches this `condition` schema - this hook will commit an operation, otherwise it won't.

If you want all documents to trigger a hook - make it's value equal a

    {
        "type": "object",
        "additionalProperties": true
    }

All documents will match this schema and a hook will trigger