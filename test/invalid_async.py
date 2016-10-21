import docraptor
import time

docraptor.configuration.username = "YOUR_API_KEY_HERE"
# docraptor.configuration.debug = True

doc_api = docraptor.DocApi()

create_response= doc_api.create_async_doc({
  "test":             True,
  "document_content": "<html><body>Hello from Python</body></html>",
  "name":             "s" * 201, # limit is 200 characters
  "type":             "pdf",
})

status_response = None
for x in range(0, 30):
  status_response = doc_api.get_async_doc_status(create_response.status_id)
  if status_response.status == "failed":
    exit(0)
  time.sleep(1)

print("Exception expected, but not raised")
exit(1)
