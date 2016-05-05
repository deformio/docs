# Embeds

We've implemented new type `embed`. 

This type has access to all **documents** in your **project**.

## Example: Countries & Cities

For example you have two collections `countries` and `cities`.

Schema of `countries`

    {
        "properties": {
            "name": {
                "type": "string",
                "required": true
            },
            "code": {
                "type": "string",
                "required": true
            },
            "representation": {
                "type": "string",
                "processors": [
                    {
                        "name": "template",
                        "in": {
                            "context": {
                                "code": {
                                    "source": "property",
                                    "property": "code"
                                },
                                "name": {
                                    "source": "property",
                                    "property": "name"
                                }
                            },
                            "syntax": {
                                "source": "value",
                                "value": "handlebars"
                            },
                            "template_string": {
                                "source": "value",
                                "value": "{{code}} - {{name}}"
                            }
                        }
                    }
                ]
            }
        }
    }


Schema of `cities`:

    {
        "properties": {
            "name": {
                "type": "string"
            },
            "country": {
                "type": "embed",
                "collection": "countries",
                "field": "code"
            },
            "population": {
                "type": "number"
            }
        }
    }


We have `field` property set pointing to `code`.

Valid payloads to match are:

* As a value:

    	{
    	    "payload": {
    	        "country": "US"
    	    }
    	}
	

* As an object

    	{
    	    "payload": {
    	        "country": {
    	            "code": "US"
    	        }
    	    }
    	}
	

If you are not setting a `field` property filtering will be performed using a `id` field of a `countries` collection.

The result **cities document** with an embedded `US` country code as **embed** will be:

    {
        "name": "Washington",
        "country": {
            "id": "united_states",
            "name": "United States",
            "code": "US",
            "representation": "US - United States"
        },
        "population": 321729000
    }
