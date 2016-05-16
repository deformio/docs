# Projects

Project is an entrypoint to your DeformIO world.

## Project properties

`/api/user/project/<project_id>/`

	{
	    "_id": "project-35567587-35567587",
	    "name": "post-created-project-name",
	    "settings": {
	        "check_limits_period": "24h0m0s",
	        "data_size_limit": 5242880,
	        "delete_files": false,
	        "files_size_limit": 10485760,
	        "orphan_files_ttl": "168h0m0s",
	        "rate_limit": 30
	    },
	    "status": {
	        "data_size": 7584,
	        "files_size": 0,
	        "rate": 0
	    }
	}


Property      | Type          | Description
--------------|---------------|-------------
\_id          | string        | Unique identity of the project
name          | string        | Name of a project
settings      | object        | Project settings
status        | object        | Project status

### settings

Property              | Type   | Editable | Description
----------------------|--------|:--------:|-----------
check\_limits\_period | string |          | How often limits of a project will be checked
data\_size\_limit     | int    | *        | Database size limit
delete\_files         | bool   | *        | Delete files after related documents and collections were deleted
files\_size\_limit    | int    | *        | Files total size limit
orphan\_files\_ttl    | string | *        | TTL of a file without document since `last_access`
rate\_limit           | int    |          | NIY. Requests per second limit

#### settings.data\_size\_limit

Units: Bytes. 

Change this to control your project DB size.

Set to `0` to make unlimited.

#### settings.files\_size\_limit

Units: Bytes. 

Change this to control your project Files total size.

Set to `0` to make unlimited.


### status

Property     | Type          | Description
-------------|---------------|-------------
data_size    | int           | Database size
files_size   | int           | Files size
is_active    | bool          | Project is active
rate         | int           | NYI. Requests per second


## Notifications

When your project `status.data_size` or `status.files_size` reaching limits ( in case if these limits are greater than `0` ) of `20%` or less you will get a [notification](/collections/#system-collections) and email message with details.

For example:

You have a project with `settings.data_size_limit` equal `100`.

In case when `status.data_size` equal or greater than `80` you will notification.


## Current limitations

By default user can have up to `5` projects.

Project initial settings:

  * `database` size: **5 Mb**
  * `files` size: **10 Mb**
