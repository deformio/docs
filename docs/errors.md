# Errors

Deform uses standard HTTP status codes when returning errors. We provide additional info about error in a response body.

It can contain `message`

    {
    	"result": {
    		"message": "Not authorized"
    	}
    }

or `errors`

    {
    	"result": {
	    	"errors": [
	    		{
	    			"property": "File",
	    			"message": "is required"
	    		}
	    	]
	    }
    }

## HTTP Status codes

Code |  Description
---- | ------------
200  | Request ok
201  | Resource created
204  | No Content
400  | Bad Request
401  | Unauthorized request
402  | Payment required
403  | Forbidden
409  | Conflict
422  | Unprocessable entity
50x  | Server error

### 200

Request OK.

### 201

Resource created.

### 204

No content.

In case of successful `DELETE`.

### 400

Bad request.

### 401

Unauthorized request.

### 402

Payment required.

When your project's `status` exceeds it's `settings` limits [for database or files total size](/projects/#settings).

### 403

Forbidden.

In case if [token permission](/tokens/#permission) does not allow this operation.

### 409

Conflict.

In case when the entity with same unique identifier exists

### 422

Unprocessable entity.See response body for details.

### 50x

Server error.