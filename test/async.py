import docraptor
import time

docraptor.configuration.username = "YOUR_API_KEY_HERE"
# docraptor.configuration.debug = True

doc_api = docraptor.ClientApi()

response = doc_api.create_async_doc({"test": True, "document_content": "<html><body>Swagger Python</body></html>", "name": "swagger-python.pdf", "document_type": "pdf"})

status_response = None
while True:
  status_response = doc_api.get_async_status(response.status_id)
  if status_response.status == "completed":
    break
  time.sleep(1)

print doc_api.get_async_doc(status_response.download_id)
