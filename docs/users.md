# Users

To manage access to your [project](/projects/) you can use a `_users` system collection.

You can add a user using his email. He won't receive any invintation ( currently )

If this user is registered at [deform.io](https://deform.io) he will be allowed to work with your project.

If someone of your mates accidentally removes you from a collection nothing will happen. You are the master of a project :D

## Users properties

	{
	    "_id": "andrey-55042645@ya.ru",
	    "is_active": true
	}


Property      | Type          | Description
--------------|---------------|-------------
\_id          | string        | email of the user
is\_active    | bool          | is the user allowed to access the project
