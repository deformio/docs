# Api Backend

## v0.0.1

### 07.05.2016
  
  * System collection `_usage` added.
  * Project `status.is_active` property added.
  * 404 now has general error interface.

        {
            "result": {
                "message": "Page not found."
            }
        }

### 03.05.2016
  
  * Processors changed:
      * apiai - has customer settings now


### 30.04.2016
  
  * User can have **5** projects.

### 17.04.2016

  * Collection and Project support `fields` and `fields_exclude`.

### 30.03.2016

  * Watermark processor fix. No url required. Watermark file is required.
  
### 18.03.2016

  * Processor dependency recursion detection implemented.
  * ProcessOnly mechanism implemented.
  

### 12.03.2016

  * Http Api Response interface migrated from

        {
            "error": [
            ]
        }

    to 

        {
            "result": {
                "message": "",
                "errors": [
                ],
            }
        }

### 11.03.2016

  * Token permissions migrated from

        {
            "permission": {
                "all": true,
                "read": [],
                "write": [],
                "delete": [],
                "update": []
            }
        }

    to 

        {
            "permission": {
                "allow": {
                    "all": true,
                    "read": [],
                    "write": [],
                    "delete": [],
                    "update": []
                }
            }
        }


### 23.02.2016
  
  * Hooks has a timeout 10 seconds

### 21.02.2016
  
  * New system collection `_users`.
  * New system collection `_notification`.

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
  