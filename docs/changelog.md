# Api Backend

## v0.0.1

### 20.02.2016
  
  * User email validation
  * User can invite another user ( already registered or send invintation email ) to project

### 19.02.2016
  
  * All queueing operations now commits in goroutines. This should significantly decrease response time.
  * Documents can be deleted by criteria. 

        curl -X POST -H "X-Action: Delete" -H "Content-Type: application/json" -d '{"payload": {"filter": {"_id": {"$in": ["document-8069947-8069947"]}}}}'

### 14.02.2016

  * System collections now have an underscore prefix. It's forbidden to create a collection with an underscore sign.
  * System fields `_id` now have an underscore prefix.
  * Response json interface `error` now is an array of objects. The schema is:

        {
            "property": {
                "type": ["string", "null"]
            },
            "message": {
            	"type": "string"
            }
        }
  