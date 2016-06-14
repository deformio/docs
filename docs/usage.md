# Usage

To manage project usage check this collection. 

This is read-only collection.

Every request you do makes a dump of data/files size in a project. 

Every hour the most big number inserts into this collection.

## Usage properties

	{
	    "_id": "576044be32d2c60f3d0736ce",
	    "data_size": 69466,
	    "date": "2016-06-14T17:00:00Z",
	    "files_size": 319531
	}


Property      | Type          | Description
--------------|---------------|-------------
\_id          | string        | unique identity of the usage document
data\_size    | integer       | data size
date          | datetime      | date the stats were dumped
files\_size   | integer       | files size

