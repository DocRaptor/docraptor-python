import docraptor
import time

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

create_response= doc_api.create_async_doc({
  "test":             True,
  "document_content": "<html><body>Hello from Python</body></html>",
  "name":             "s" * 201, # limit is 200 characters
  "document_type":    "pdf",
})

status_response = None
for x in range(0, 30):
  status_response = doc_api.get_async_doc_status(create_response.status_id)
  if status_response.status == "failed":
    exit(0)
  time.sleep(1)

print("Exception expected, but not raised")
exit(1)
