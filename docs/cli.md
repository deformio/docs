# CLI Reference

Deform command line client (CLI) allows you talk to and operate Deform using the command line interface. It talks to the Deform using the public API.

## Installation

### Mac OS X

    $ brew install deform-cli

### Ubuntu

    $ apt-get install deform-cli

### From binaries

todo: like [docker](https://docs.docker.com/engine/installation/binaries/)

## Configuration

## Use mode

Sometimes it's annoying to repeat your project name or path you're navigating.
For example let's get the document with `_id` equals `starbucks`:

    $ deform get mysquare.collections.venues.documents.starbucks

You can shorten this line by remembering the base path for the navigation:

    $ deform use mysquare
    $ deform get .collections.venues.documents.starbucks

Going deeper:

    $ deform use .collections.venues
    $ deform get .documents

With the command above you will get all the documents from the `venues` collection.
Let's get the exact document:

    $ deform get .documents.starbucks

In "use" mode there is no limitation for working with absolute paths:

    $ deform get mysquare.collections.venues.documents.starbucks

## Verbosity

By default CLI returns as simple response as possible. For example:

    $ deform get mysquare.collections.venues.documents --per-page 3

```json
[
  {
    "id": "starbucks",
    "name": "Starbucks"
  },
  {
    "id": "",
    "name": "Starbucks"
  },
  {
    "id": "starbucks",
    "name": "Starbucks"
  }
]
```

We've limited response by 3 documents. With `-v` flag we can see how many pages
left:

    $ deform get mysquare.collections.venues.documents --per-page 3 -v

```json
[
  {
    "id": "starbucks",
    "name": "Starbucks"
  },
  {
    "id": "",
    "name": "Starbucks"
  },
  {
    "id": "starbucks",
    "name": "Starbucks"
  }
]

Page: 1
Pages: 2
Per page: 3
Total: 6
Time: 1.0 sec
```

## Raw HTTP requests

If you want to see raw data used by CLI to communicate with API and raw response
just provide `--http` flag:

    $ deform get mysqaure.collections --http

# todo: use real example

```json
PUT /put HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Content-Type: application/json
Host: httpbin.org
User-Agent: HTTPie/0.2.7dev

{
    "hello": "world"
}


HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 477
Content-Type: application/json
Date: Sun, 05 Aug 2012 00:25:23 GMT
Server: gunicorn/0.13.4

{
    […]
}

```

## Account

* `deform account`
* `deform account create`

## Authentication

## Creating project
