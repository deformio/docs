# Tokens

Tokens are entities which can modify access levels to your documents and collections. 

Tokens **cannot** be used to operate with:
  
  * user
  * project

Tokens **can** be used to operate with:
  
  * collections
  * documents

Every entity in a project is a [document](/documents/) contained in a [collection](/collections/). 

This means you can create a token **able only to create other tokens**:

    {
	    "_id": "57114edc32d2c668de756b0c",
	    "is_active": true,
	    "name": "token_to_create_token",
	    "permission": {
	        "allow": {
	            "create": [
	                {
	                    "what": "document",
	                    "where": "_tokens"
	                }
	            ]
	        }
	    }
	}


Or you can create a token **able to read only one `document` in a collection `vacations` with id `september`**:

    {
	    "_id": "57114edc32d2c668de756b0c",
	    "is_active": true,
	    "name": "token-35567587",
	    "permission": {
	        "allow": {
	            "read": [
	                {
	                    "what": "document",
	                    "where": "vacations",
	                    "what_id": "september"
	                }
	            ]
	        }
	    }
	}


## Token in a Request

You can pass a token in request header as:

  * `"Authorization": "Token TokenId"`

Also you can pass it in URL:
  
  * `https://myproject.deform.io/api/collections/_files/documents/vacation/content/?token=TokenId`



## Token properties

	{
	    "_id": "57114edc32d2c668de756b0c",
	    "is_active": true,
	    "name": "token-35567587",
	    "permission": {
	        "allow": {
	            "create": [
	                {
	                    "what": "document",
	                    "where": "venues"
	                },
	                {
	                    "what": "collection"
	                }
	            ],
	            "delete": [
	                {
	                    "what": "document",
	                    "where": "venues",
	                    "what_id": "removeable-cafe"
	                },
	                {
	                    "what": "collection",
	                    "what_id": "removable-collection"
	                }
	            ],
	            "read": [
	                {
	                    "what": "document",
	                    "where": "read-only-collection"
	                },
	                {
	                    "what": "collection"
	                }
	            ],
	            "update": [
	                {
	                    "what": "document"
	                },
	                {
	                    "what": "collection",
	                    "what_id": "update-only-collection"
	                }
	            ]
	        }
	    }
	}


Property      | Type          | Description
--------------|---------------|-------------
\_id          | string        | Unique identity of the token
name          | string        | Name of a token
is\_active    | bool          | Is token active or not
permission    | object        | Token access levels


### permission

Property     | Type          | Description
-------------|---------------|-------------
allow        | object        | Token allow access levels


#### allow

Property     | Type          | Description
-------------|---------------|-------------
all          | bool          | Allow all
create       | array         | List of [entities](/tokens/#access-entity) which can be created
update       | array         | List of [entities](/tokens/#access-entity) which can be updated
read         | array         | List of [entities](/tokens/#access-entity) which can be read
delete       | array         | List of [entities](/tokens/#access-entity) which can be deleted


##### access entity

Property      | Type          | Description
--------------|---------------|-------------
what          | string        | Values: `collection`, `document`
what\_id      | string        | Unique identifier of a `what` entity to perate with
where         | string        | If `what:document` this will be the `_id` of a collection
