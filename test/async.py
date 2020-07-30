import docraptor
import time

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

create_response = doc_api.create_async_doc({
  "test":             True,
  "document_content": "<html><body>Hello from Python</body></html>",
  "name":             "python-async.pdf",
  "document_type":    "pdf",
})

status_response = None
while True:
  status_response = doc_api.get_async_doc_status(create_response.status_id)
  if status_response.status == "completed":
    break
  time.sleep(1)

doc_api.get_async_doc(status_response.download_id)
