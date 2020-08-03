import docraptor

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

doc_api.create_doc({
  "test":             True,
  "document_content": "<html><body><table><tr><td>Hello from Python</td></tr></table></body></html>",
  "name":             "python-xlsx.xlsx",
  "document_type":    "xlsx",
})
