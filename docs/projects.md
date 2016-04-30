# Projects

Project is an entity which contains collections. 

You can request your project's entities by adding it's `_id` to our domain. 

For example your project has `_id` equal to `hello`. Request it's collections as easy as:

    curl -H "Authorization: Token <ACCESS_TOKEN>" https://hello.deform.io/api/collections/


## Limitations

By default user can have maximum `5` projects.

Project default settings:

  * `database` size: **5 Mb**
  * `files` size: **10 Mb**


## Status and Usage

Current usage can be found in `status` property of a requested project.

You can modify `settings`:
  
  * `settings.delete_files` - files should be deleted in the moment when related documents/collections are deleted ( **default false** )
  * `settings.orphan_files_ttl` - time orphan files to live if `settings.delete_files:false` since `last_access` of a file.