# Collections

Collections are used to group, validate and process documents.

You can also create a document without collection.

## Collection advantages 

A collection is used to gain features like validation/processing.

Full list of features is located [here](/documents/#features).

## Collection properties

    {
        "_id": "example-collection",
        "documents_permissions": {
            "createable": true,
            "removeable": true,
            "updateable": true
        },
        "indexes": [],
        "is_system": false,
        "name": "Example Collection",
        "repr_property": "",
        "schema": {
            "type": "object",
            "additionalProperties": true
        }
    }


Property               | Type          | Description
---------------------- | ------------- | ------------
\_id                   | string        | Unique identity of the collection
documents\_permissions | object        | Documents access permissions
indexes                | array         | A list of indexes
is\_system             | bool          | If is true then this is a [system collection](/collections/#system-collections)
name                   | string        | Name of a collection
repr_property          | string        | Reproducive property of a collection
schema                 | object        | Is a [JSON Schema](/schemas/) a documents should match
description            | string        | Description of a collection
documents_count        | interger      | Number of documents containing in a collection


## indexes

General indexes:

    "indexes": [
        {
            "type":     "text",
            "property": "property",
            "language": "en"
        },
        {
            "type": "simple",
            "property": "simple_property"
            "unique": false
        },
        {
            "type": "compound",
            "properties": ["b", "c", "d"],
            "unique": true
        }
    ]

Index can be **simple**, **text** and **compound**

**Simple** index properties

Property  | Type       | Description
--------- | ---------- | ------------
property  | string     | Property to index
unique    | bool       | Unique index

**Text** index properties

Property  | Type       | Description
--------- | ---------- | ------------
property  | string     | Property to index for fulltext search
language  | string     | Language used for this index


Currently supported languages are:

Code   | Name
:-----:|------
da     | danish
nl     | dutch
en     | english
fi     | finnish
fr     | french
de     | german
hu     | hungarian
it     | italian
nb     | norwegian
pt     | portuguese
ro     | romanian
ru     | russian
es     | spanish
sv     | swedish
tr     | turkish
ara    | arabic
prs    | dari
pes    | iranian persian
urd    | urdu
zhs    | hans
zht    | hant

**Compound** index properties

Property  | Type       | Description
--------- | ---------- | ------------
properties| array      | Properties included to index
unique    | bool       | Unique index


## System collections

Every project has a set of system collections. Their names start with `_` prefix

You cannot **create**, **delete**, **update** system collections.

Name                      | Description
------------------------- | ------------
[\_debug](/debug)         | Writes all requests and responses. If `project.settings.debug` is enabled.
[\_files](/files)         | Uploaded and generated files
[\_hooks](/hooks)         | Hooks
[\_hooks_history](/hooks) | Hook history with responses and status codes
[\_notifications](/notifications) | System notifications will be saved here
[\_tokens](/tokens)        | Access tokens to your project
[\_usage](/usage)         | Project usage
[\_users](/users)         | Users allowed to your project. Project's Owner removal has no effect.

### \_notifications

All notifications from a system.

### \_debug

Writes all requests and responses. Toggle via `project.settings.debug`

### \_files

Uploaded and generated files.

### \_tokens

Manage access tokens in this collection.

### \_hooks

List of hooks and their conditions.

### \_hooks_history

History of hook triggers.. Documents inside this collection **are not affected by hooks**

### \_usage

Project usage. Documents inside this collection **are not affected by hooks**

### \_users

List of users allowed to access to the project. If you delete yourself you will still have an access to the project.