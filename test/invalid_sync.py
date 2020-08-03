import docraptor

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

try:
  doc_api.create_doc({
    "test":             True,
    "document_content": "<html><body>Hello from Python</body></html>",
    "name":             "s" * 201,
    "document_type":    "pdf",
  })
except docraptor.rest.ApiException as e:
  exit(0)

print("Exception expected, but not raised")
exit(1)

