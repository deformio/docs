# Processors

One of key features of deform.io is data processing. Processors are entities in a schema. They can have access to multiple properties.

Processors can be chained. 

There is also a processor dependency recursion check.

Feel free to send us a feedback about processors you are missing.

## Limitations

As for now processor cannot process array fields. In future we will implement this feature.

## Current processors implemented

Name                   | Description
-----------------------|------------
bcrypt                 | A key derivation function for passwords designed by Niels Provos and David Mazières, based on the Blowfish cipher
google_detect_language | Detect the language of a text string
google_translate       | Translate text from one language to another language
html_to_text           | Remove html tags from a text
markdown               | Render a html from a markdown
md5                    | Calculate a message-digest fingerprint (checksum)
random                 | Make a random value
readability_com        | Use readability.com to turn any web page into a clean view for reading
resize                 | Resize an image
sentiment              | Sentiment analysis aims to determine the attitude of a speaker or a writer with respect to some topic or the overall contextual polarity of a text
template               | Make a string from template.
text_to_speech         | Text to speech processor
watermark              | Watermark an image
yandex_detect_language | Detect the language of a text string
yandex_translate       | Translate text from one language to another language