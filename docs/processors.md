# Processors

Data processing is one of features deform.io provides. Processors are entities in a schema. They can have access to multiple properties.

Processors can be chained. 

There is also a processor dependency recursion check.

Feel free to send us a feedback about processors you are missing.

## Limitations

As for now processor cannot process array fields. In future we will implement this feature.

## Current processors implemented

Name                     | Description
-------------------------|------------
apiai                    | Process natural language
google\_detect\_language | Detect the language of a text string
google\_translate        | Translate text from one language to another language
html\_to\_text           | Remove html tags from a text
markdown                 | Render a html from a markdown
md5                      | Calculate a message-digest fingerprint (checksum)
random                   | Make a random value
readability\_com         | Use readability.com to turn any web page into a clean view for reading
resize                   | Resize an image
sentiment                | Sentiment analysis aims to determine the attitude of a speaker or a writer with respect to some topic or the overall contextual polarity of a text
template                 | Make a string from template.
text\_to\_speech         | Text to speech processor
watermark                | Watermark an image
yandex\_detect\_language | Detect the language of a text string
yandex\_translate        | Translate text from one language to another language