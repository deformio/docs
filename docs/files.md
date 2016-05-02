# Files

Your files info stores in a `_files` system collection.

Total size of all files could be found in a [project's status](/projects/#status) `files_size` property

## Document and Content

Every file can be retrieved as a document and as a raw bytes.

  * `/collections/_files/documents/<file_id>/` - as a json document
  * `/collections/_files/documents/<file_id>/content/` - as raw bytes
  * `/collections/<collection_with_a_document>/documents/<document_id>/my/file/path/` - as a json document
  * `/collections/<collection_with_a_document>/documents/<document_id>/my/file/path/content/` - as raw bytes
