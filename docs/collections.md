# Collections

Collection is an entity which contains documents.

## Collection properties

General collection looks like:

    {
        "_id": "example-collection",
        "documents_permissions": {
            "createable": true,
            "removeable": true,
            "updateable": true
        },
        "indexes": [],
        "is_system": false,
        "name": "Example Collection",
        "repr_property": "",
        "schema": {
            "type": "object",
            "additionalProperties": true
        }
    }


Property     | Type          | Description
------------ | ------------- | ------------
_id                   | string | id of a collection
documents_permissions | object | object which contains documents access permissions
indexes               | array  | a list of indexes which can be created
is_system             | bool   | if is true then this is a [system collection](/collections/#system-collections)
name                  | string | name of a collection
repr_property         | string | reproducive property of a collection
schema                | object | is a [JSON Schema](/schemas/) a documents should match

## System collections

By default projects has collections which names starts with `_`.

You cannot **create**, **delete**, **update** system collections.

Name           | Description
-------------- | ------------
_notifications | System notifications will be saved here
_files         | Uploaded and generated ( resized, watermarked and etc ) files
_tokens        | Access tokens to your project
_hooks         | Hooks
_hooks_history | Hook history with responses and status codes
_users         | List of users allowed to your project. If you delete yourself you will have access to a project

