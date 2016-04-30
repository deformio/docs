# Schemas

We use JSON Schema as a core feature for data description.

[Here](http://json-schema.org/) you can find docs and examples. 

## Changed behaviour

We had to change some property behaviours to fit our goals:

  * **additionalProperties** by default was **true**
    * **changed** to be **false**

## Attributes

We also added some new attributes:

Attribute  | Description
-----------|------------
processors | add a list of processors to the field
required   | marks a field as required. By default the field is **not required**. See the example below.
immutable  | marks a field as an immutable. This means - you cannot change a field after it was created.
position   | decorative helper attribute to assign a position in UI

## Data types

Default data types:

Name    | Description
--------|------------
array   | array
boolean | boolean
integer | number without a fraction or exponent part
number  | number
null    | null value
object  | object
string  | string


We added some custom types to extend default schema:

Name     | Type   | Description
---------|--------|------------
file     | object | accepts a file uploaded using `multipart/form-data`
datetime | string | format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
embed    | object | makes possible to set a data source


### Datetime

These two are valid datetimes:
 
 * `2009-11-10T23:00:00Z`
 * `2015-06-03T15:55:59.073Z`

### Embed

Property     | Type   | Required | Description
-------------|--------|:--------:|-----------
collection   | string | *        | points to collection for data to fetch from
field        | string |          | `_id`  or a collection schema's field

All datetime without a timezone will be assumed to be a UTC.

You can set a date to `2015-06-03T18:55:59.073+03:00` this will be converted to UTC and properly saved to database.

