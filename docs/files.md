# Files

Your files info stores in a `_files` system collection.

Total size of all files could be found in a [project's status](/projects/#status) `files_size` property

## Document and Content

Every file can be retrieved as JSON document and raw bytes.

  * `/collections/_files/documents/<file_id>/` - JSON document
  * `/collections/_files/documents/<file_id>/content/` - raw bytes
  * `/collections/<collection_with_a_document>/documents/<document_id>/my/file/path/` - JSON document
  * `/collections/<collection_with_a_document>/documents/<document_id>/my/file/path/content/` - raw bytes
