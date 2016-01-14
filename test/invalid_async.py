import docraptor
import time

docraptor.configuration.username = "YOUR_API_KEY_HERE"
docraptor.configuration.debug = True

doc_api = docraptor.ClientApi()

response = doc_api.async_docs_post({"test": True, "document_content": "<html><body>Swagger Python</body></html>", "name": "s" * 201, "document_type": "pdf"})

status_response = None
for x in range(0, 30):
  status_response = doc_api.status_id_get(response.status_id)
  if status_response.status == "failed":
    exit(0)
  time.sleep(1)

print "Exception expected, but not raised"
exit(1)
