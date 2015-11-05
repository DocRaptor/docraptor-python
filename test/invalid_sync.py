import docraptor
import time

docraptor.configuration.username = "YOUR_API_KEY_HERE"
docraptor.configuration.debug = True

doc_api = docraptor.ClientApi()

try:
  response = doc_api.docs_post({"test": True, "document_content": "<html><body>Swagger Python</body></html>", "name": "s" * 201, "document_type": "pdf"})
except docraptor.rest.ApiException, e:
  exit(0)

print "Exception expected, but not raised"
exit(1)

