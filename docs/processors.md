# Processors

Data processing is one of features deform.io provides. Processors are entities in a schema. They can have access to multiple properties.

Processors can be chained. 

There is also a processor dependency recursion check.

Feel free to send us a feedback about processors you are missing.

## Limitations

As for now processor cannot process array fields. In future we will implement this feature.

## Current processors implemented

Name                     | Description
-------------------------|------------
apiai                    | Process natural language
google\_detect\_language | Detect the language of a text string
google\_translate        | Translate text from one language to another language
html\_to\_text           | Remove html tags from text
markdown                 | Render a html from a markdown
md5                      | Calculate a message-digest fingerprint (checksum)
random                   | Make a random value
readability              | Makes a text readable
readability\_com         | Use readability.com to turn any web page into a clean view for reading
resize                   | Resize an image
sentiment                | Sentiment analysis aims to determine the attitude of a speaker or a writer with respect to some topic or the overall contextual polarity of a text
template                 | Make a string from template
text\_to\_speech         | Text to speech processor
watermark                | Watermark an image
yandex\_detect\_language | Detect the language of a text string
yandex\_translate        | Translate text from one language to another language

    
## Examples

### apiai

Process natural language

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"human_text": {
        		"type": "string",
        		"required": true
        	},
            "ai_obj": {
            	"type": ["object", "null"],
            	"additionalProperties": true,
            	"processors": [
            		{
            			"name": "apiai",
            			"in": {
							"text": {
								"source": "property",
								"property": "human_text"
							},
							"language": {
								"source": "value",
								"value": "EN"
							},
							"language_token": {
								"source": "value",
								"value": "<YOUR_LANGUAGE_TOKEN>"
							},
							"subscription_key": {
								"source": "value",
								"value": "<YOUR_SUBSCTIPTION_KEY>"	
							},
							"timezone": {
								"source":"value",
								"value": "Europe/Moscow"
							},
							"contexts": {
								"source": "value",
								"value": ["calendar"]
							}
						}
            		}
            	]
            }
	    }
	}


Request payload::

	{
		"human_text": "schedule lunch at 1 pm tomorrow.",
	}

Response:

	{
	    "result": {
	        "_id": "572b676a32d2c61886cda77b",
	        "ai_obj": {
	            "action": "calendar.add",
	            "metadata": {
	                "contexts": [],
	                "inputContexts": [],
	                "outputContexts": []
	            },
	            "parameters": {
	                "endDate": "2016-05-06T13:00:00+03:00",
	                "startDate": "2016-05-06T13:00:00+03:00",
	                "summary_predefined": "lunch"
	            },
	            "resolvedQuery": "schedule lunch at 1 pm tomorrow.",
	            "score": 0,
	            "source": "domains",
	            "speech": ""
	        },
	        "human_text": "schedule lunch at 1 pm tomorrow."
	    }
	}



### google\_detect\_language

Detect the language of a text string

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"text": {
        		"type": "string"
        	},
        	"detected": {
        		"type": "string",
        		"processors": [
        			{
        				"name": "google_detect_language",
        				"in": {
                            "text": {
                                "source": "property",
                                "property": "text"
                            },
                            "api_key": {
                                "source": "value",
                                "value": "<YOUR_API_KEY>"
                            }
                        }
        			}
        		]
        	}
	    }
	}

Request payload:
	
	{
		"text": "Привет"
	}

Response:

	{
	    "result": {
	        "_id": "572a45ed32d2c602098508e0",
	        "text": "Привет",
	        "detected": "ru"
	    }
	}


### google\_translate

Translate text from one language to another language

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"text": {
        		"type": "string"
        	},
        	"translated": {
        		"type": "string",
        		"processors": [
        			{
        				"name": "google_translate",
        				"in": {
                            "text": {
                                "source": "property",
                                "property": "text"
                            },
                            "from": {
                                "source": "value",
                                "value": "ru"
                            },
							"to": {
                                "source": "value",
                                "value": "en"
                            },
							"api_key": {
                                "source": "value",
                                "value": "<YOUR_API_KEY>"
                            }
                        }
        			}
        		]
        	}
	    }
	}

Request payload:
	
	{
		"text": "Привет"
	}

Response:

	{
	    "result": {
	        "_id": "572a45ec32d2c602098508d5",
	        "text": "Привет",
	        "translated": "Hi"
	    }
	}


### html\_to\_text

Remove html tags from text

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"html": {
        		"type": "string"
        	},
        	"text": {
        		"type": "string",
        		"processors": [
        			{
        				"name": "html_to_text",
        				"in": {
                            "html": {
                                "source": "property",
                                "property": "html"
                            }
                        }
        			}
        		]
        	}
	    }
	}

Request payload:
	
	{
		"html": "<html><head><title>Hello</title></head><body>World</body></html>"
	}

Response:

	{
	    "result": {
	        "_id": "572b75f632d2c620e67a8908",
	        "html": "<html><head><title>Hello</title></head><body>World</body></html>",
	        "text": "World"
	    }
	}


### markdown

Render a html from a markdown

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"markdown": {
				"type": "string",
				"required": true
			},
			"html": {
				"type": "string",
				"description": "rendered markdown",
				"processors": [
					{
						"name": "markdown",
						"in": {
							"text": {
								"source": "property",
								"property": "markdown"
							}
						}
					}
				]
			}
	    }
	}

Request payload:

	{
		"markdown": "**hello** __world__"
	}

Response:
	
	{
	    "result": {
	        "_id": "572b746a32d2c61f0a366d87",
	        "html": "<p><strong>hello</strong> <strong>world</strong></p>\n",
	        "markdown": "**hello** __world__"
	    }
	}


### md5

Calculate a message-digest fingerprint (checksum)

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"firstName": {
				"type": "string"
			},
			"lastName": {
				"type": "string"
			},
			"password_md5ed": {
				"type": "string",
				"description": "user password",
				"processors": [
					{
						"name": "md5"
					}
				],
				"required": true
			}
	    }
	}

Request payload:
	
	{
		"firstName": "Andrey",
		"lastName": "Chibisov",
		"password": "1234567890"
	}

Response:

	{
	    "result": {
	        "_id": "jKmLOGOunnNrLe",
	        "firstName": "Andrey",
	        "lastName": "Chibisov",
	        "password_md5ed": "e807f1fcf82d132f9bb018ca6738a19f"
	    }
	}


### random

Make a random value

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    "firstName": {
				"type": "string"
			},
			"lastName": {
				"type": "string"
			},
			"password": {
				"type": "string",
				"description": "random user password",
				"processors": [
					{
						"name": "random",
						"in": {
							"random_type": {
								"source": "value",
								"value": "string"
							},
							"length": {
								"source": "value",
								"value": 20
							}
						}
					},
					{
						"name": "md5"
					}
				]
			}
		},
		"required": ["firstName", "lastName"]
	}


Request payload:
	
	{
		"firstName": "Gennady",
		"lastName":  "Chibisov"
	}

Response:
	

	{
	    "result": {
	        "_id": "572b722a32d2c61d34331ef0",
	        "firstName": "Gennady",
	        "lastName": "Chibisov",
	        "password": "1591bbef3c4792bf9e102b10cad32b1c"
	    }
	}

### readability

Makes a text readable
	
	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	{
		"type": "object",
		"properties": {
			"html_content": {
				"type": "string"
			},
			"readable": {
				"type": "object",
				"properties": {
					"content": {
						"type": "string"
					},
					"short_title": {
						"type": "string"
					},
					"title": {
						"type": "string"
					}
				},
				"processors": [
					{
						"name": "readability",
						"in": {
							"text": {
								"source": "property",
								"property": "html_content"
							}
						}
					}
				]
			}
	    }
	}

Request payload:

	{
		"html_content": "<html><head><title>Hello</title></head><body>World</body></html>",
	}

Response:

	{
	    "result": {
	        "_id": "572b70b932d2c61c27a112bb",
	        "html_content": "<html><head><title>Hello</title></head><body>World</body></html>",
	        "plaintext": "World",
	        "readable": {
	            "content": "<body id=\"readabilityBody\">World</body>",
	            "short_title": "Hello",
	            "title": "Hello"
	        }
	    }
	}



### readability\_com

Use [readability.com](https://readability.com/) to turn any web page into a clean view for reading

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"url_to_make_readable": {
        		"type": "string"
        	},
        	"readable": {
        		"type": "object",
        		"additionalProperties": true,
        		"processors": [
        			{
        				"name": "readability_com",
        				"in": {
                            "url": {
                                "source": "property",
                                "property": "url_to_make_readable"
                            },
							"api_key": {
                                "source": "value",
                                "value": "<YOUR_API_KEY>"
                            }
                        }
        			}
        		]
        	}
	    }
	}

Request payload:
	
	{
		"url_to_make_readable": "https://blog.chib.me/how-to-convert-databases-with-one-line-of-code/",
	}


Response:

	{
	    "result": {
	        "_id": "572b7cb032d2c628585e1fa9",
	        "readable": {
	            "author": null,
	            "content": "............",
	            "date_published": "2016-02-07 13:03:06",
	            "dek": null,
	            "direction": "ltr",
	            "domain": "blog.chib.me",
	            "excerpt": "07 February 2016 Have you ever wanted to convert mysql database to sqlite? Or postgres to mysql? Or mysql to postgres? Recently I've been migrating my django project from MySQL to SQLite. I tried to&hellip;",
	            "lead_image_url": null,
	            "next_page_id": null,
	            "rendered_pages": 1,
	            "short_url": "http://rdd.me/7gou967w",
	            "title": "How to convert databases with one line of code",
	            "total_pages": 0,
	            "url": "https://blog.chib.me/how-to-convert-databases-with-one-line-of-code/",
	            "word_count": 421
	        },
	        "url_to_make_readable": "https://blog.chib.me/how-to-convert-databases-with-one-line-of-code/"
	    }
	}

### resize

Resize an image

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"original": {
				"type": "file"
			},
			"resized": {
				"type": "file",
				"processors": [
					{
						"name": "resize",
						"in": {
					        "original_image": {
					            "source": "property",
					            "property": "original"
					       	},
							"size": {
								"source": "value",
								"value": [200,200]
							}
						}
					}
				]
			}
	    }
	}

Commit a `PUT`/`POST`/`PATCH` with `Content-Type: multipart/form-data` and file assigned to `original` property

Response:

	{
	    "result": {
	        "_id": "572b6e7732d2c61b066cee6e",
	        "original": {
	            "_id": "572b6e7732d2c61b066cee6f",
	            "collection_id": "QSMHdGfXIQIXOv",
	            "content_type": "image/gif",
	            "date_created": "2016-05-05T16:01:59.614410146Z",
	            "document_id": "572b6e7732d2c61b066cee6e",
	            "last_access": "2016-05-05T16:01:59.614410146Z",
	            "md5": "8c4c6953f0b9003eb9ceb7a923cc208e",
	            "name": "test_helpers/data/animated.gif",
	            "size": 991109
	        },
	        "resized": {
	            "_id": "572b6e7832d2c61b066cee71",
	            "collection_id": "QSMHdGfXIQIXOv",
	            "content_type": "image/gif",
	            "date_created": "2016-05-05T16:02:00.475956835Z",
	            "document_id": "572b6e7732d2c61b066cee6e",
	            "last_access": "2016-05-05T16:02:00.475956835Z",
	            "md5": "d741fa8da603842a0dd0aec9ec2330df",
	            "name": "resized_resize_OLYi.gif",
	            "size": 366404
	        }
	    }
	}


### sentiment

Sentiment analysis aims to determine the attitude of a speaker or a writer with respect to some topic or the overall contextual polarity of a text

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"text": {
				"type": "string"
			},
			"sentiment": {
				"type": "number",
				"description": "text to sentiment",
				"processors": [
					{
						"name": "sentiment",
						"in": {
							"text": {
								"source": "property",
								"property": "text"
							}
						}
					}
				]
			}
	    }
	}

Request payload:

	{
		"text": "this restaurant is great",
	}

Response:

	{
	    "result": {
	        "_id": "572b6d4132d2c61a78927e5d",
	        "sentiment": 0.8,
	        "text": "this restaurant is great"
	    }
	}


### template

Make a string from template

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
			"country": {
				"type": "object",
				"properties": {
					"name": {
						"type": "string",
						"required": true
					},
					"code": {
						"type": "string",
						"required": true
					}
				}
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
                        			"property": "country.code"
                        		},
                        		"name": {
                        			"source": "property",
                        			"property": "country.name"
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

Request payload:

    {
    	"country": {
    		"name": "Russian Federation",
    		"code": "RU"
    	}
    }

Response:

	{
		"_id": "562b6b7a32e3c118e83aa4fa",
		"country": {
    		"name": "Russian Federation",
    		"code": "RU"
    	},
    	"representation": "RU - Russian Federation"
	}


### text\_to\_speech

Text to speech processor

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
			"user_info": {
				"type": "object",
				"properties": {
					"firstName": {
						"type": "string"
					},
					"lastName": {
						"type": "string"
					},
					"age": {
						"description": "Age in years",
						"type": "integer",
						"minimum": 0
					}
				}
			},
			"message": {
				"type": "string",
				"processors": [
					{
						"name": "template",
						"in": {
							"context": {
                        		"firstName": {
                        			"source": "property",
                        			"property": "user_info.firstName"
                        		},
                        		"lastName": {
                        			"source": "property",
                        			"property": "user_info.lastName"
                        		},
                        		"age": {
                        			"source": "property",
                        			"property": "user_info.age"
                        		}
                        	},
							"syntax": {
								"source":"value",
								"value":"handlebars"
							},
                            "template_string": {
                            	"source": "value",
                            	"value":"{{lastName}} {{firstName}} is {{age}} years"
                            }
						}
					}
				]
			},
			"tts_field": {
				"type": "file",
				"processors": [
					{
						"name": "text_to_speech",
						"in": {
							"text": {
								"source": "property",
								"property": "message"
							},
							"language": {
								"source":"value",
								"value": "en-US"
							}
						}
					}
				]
			}
		}
	}


Request payload::

	{
        "user_info": {
            "lastName":  "Chibisov",
            "firstName": "Andrey",
            "age":       27
		}
	}

Response:

	{
	    "result": {
	        "_id": "572b6b7832d2c619e83aa4fd",
	        "message": "Chibisov Andrey is 27 years",
	        "tts_field": {
	            "_id": "572b6b7a32d2c619e83aa4fe",
	            "collection_id": "example_schema_tts-MuVVGXLnShseQO",
	            "content_type": "audio/x-wav",
	            "date_created": "2016-05-05T15:49:14.342821384Z",
	            "document_id": "572b6b7832d2c619e83aa4fd",
	            "last_access": "2016-05-05T15:49:14.342821384Z",
	            "md5": "8a2bab3a7b3752028e9dfbfa326d5e73",
	            "name": "tts_field_text_to_speech_trde.wav",
	            "size": 59206
	        },
	        "user_info": {
	            "age": 27,
	            "firstName": "Andrey",
	            "lastName": "Chibisov"
	        }
	    }
	}




### watermark

Watermark an image

TODO


### yandex\_detect\_language

Detect the language of a text string

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"text": {
        		"type": "string"
        	},
        	"detected": {
        		"type": "string",
        		"processors": [
        			{
        				"name": "yandex_detect_language",
        				"in": {
                            "text": {
                                "source": "property",
                                "property": "text"
                            },
							"api_key": {
                                "source": "value",
                                "value": "<YOUR_API_KEY>"
                            }
                        }
        			}
        		]
        	}
	    }
	}

Request payload::

	{
		"text": "Hello world",
	}

Response:

	{
	    "result": {
	        "_id": "572b7a9432d2c6241b8bbe22",
	        "text": "Hello world",
	        "detected": "en"
	    }
	}


### yandex\_translate

Translate text from one language to another language

	{
	    "description": "Collection schema",
	    "type": "object",
	    "properties": {
	    	"text": {
        		"type": "string"
        	},
        	"translated": {
        		"type": "string",
        		"processors": [
        			{
        				"name": "yandex_translate",
        				"in": {
                            "text": {
                                "source": "property",
                                "property": "text"
                            },
                            "lang": {
                                "source": "value",
                                "value": "ru-en"
                            },
							"api_key": {
                                "source": "value",
                                "value": "<YOUR_API_KEY>"
                            }
                        }
        			}
        		]
        	}
	    }
	}

Request payload:
	
	{
		"text": "Как дела?"
	}

Response:
	
	{
	    "result": {
	        "_id": "572b791532d2c6226354dd26",
	        "text": "Как дела?",
	        "translated": "How's it going?"
	    }
	}

