# Tokens

Tokens are entities which can modify access levels to your documents and collections. 

Tokens **cannot** be used to operate with:
  
  * user
  * project

## Token properties

`/api/collections/_tokens/documents/<token_id>/`

	{
	    "_id": "57114edc32d2c668de756b0c",
	    "is_active": true,
	    "name": "token-35567587",
	    "permission": {
	        "allow": {
	            "create": [
	                {
	                    "what": "document"
	                },
	                {
	                    "what": "collection"
	                }
	            ],
	            "delete": [
	                {
	                    "what": "document"
	                },
	                {
	                    "what": "collection"
	                }
	            ],
	            "read": [
	                {
	                    "what": "document"
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
	                    "what": "collection"
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
