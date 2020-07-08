import docraptor

configuration = docraptor.Configuration()
configuration.username = 'YOUR_API_KEY_HERE'
# configuration.debug = True

doc_api = docraptor.DocApi(docraptor.ApiClient(configuration))

doc_api.create_doc({
  "test":             True,
  "document_content": "<html><body>Hello from Python</body></html>",
  "name":             "python-sync.pdf",
  "document_type":    "pdf",
})
