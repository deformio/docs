# Collections

Collection is an entity which contains documents. 

## System collections

By default projects has collections which names starts with `_`:

  * `_notifications` - System notifications will be saved here;
  * `_files` - Uploaded and generated ( resized, watermarked and etc ) files;
  * `_tokens` - Access tokens to your project;
  * `_hooks` - Hooks;
  * `_hooks_history` - Hook history with responses and status codes;
  * `_users` - List of users allowed to your project. If you delete yourself you will have access to a project.

You cannot commit following operations to a system collections:
  
  * **create**
  * **delete**
  * **change** 

Document permissions in a collection can be found in a `documents_permissions` property. Possible values are:
  
  * `removeable` [:boolean] - you can **remove** documents inside of a collection;
  * `createable` [:boolean] - you can **create** documents inside of a collection;
  * `updateable` [:boolean] - you can **update** documents inside of a collection.