import docraptor

docraptor.configuration.username = "YOUR_API_KEY_HERE"
# docraptor.configuration.debug = True

doc_api = docraptor.ClientApi()

doc_api.create_doc({
  "test":             True,
  "document_content": "<html><body>Hello from Python</body></html>",
  "name":             "python-sync.pdf",
  "document_type":    "pdf",
})
