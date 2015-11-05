import docraptor
import time

docraptor.configuration.username = "YOUR_API_KEY_HERE"
docraptor.configuration.debug = True

doc_api = docraptor.ClientApi()

response = doc_api.async_docs_post({"test": True, "document_content": "<html><body>Swagger Python</body></html>", "name": "swagger-python.pdf", "document_type": "pdf"})

status_response = None
while True:
  status_response = doc_api.status_id_get(response.status_id)
  if status_response.status == "completed":
    break
  time.sleep(1)

print doc_api.download_id_get(status_response.download_id)

print "SHITS DONE!"
