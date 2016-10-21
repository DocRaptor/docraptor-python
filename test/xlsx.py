import docraptor

docraptor.configuration.username = "YOUR_API_KEY_HERE"
# docraptor.configuration.debug = True

doc_api = docraptor.DocApi()

doc_api.create_doc({
  "test":             True,
  "document_content": "<html><body><table><tr><td>Hello from Python</td></tr></table></body></html>",
  "name":             "python-xlsx.xlsx",
  "type":             "xlsx",
})
