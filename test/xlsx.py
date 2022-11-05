import docraptor
import os
import platform

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

pdf_data = doc_api.create_doc({
  "test":             True,
  "document_content": "<html><body><table><tr><td>Hello from Python</td></tr></table></body></html>",
  "name":             "python-xlsx.xlsx",
  "document_type":    "xlsx",
})

file_path = "/app/tmp/test_output/" + os.path.basename(__file__) + "_python_" + platform.python_version() + ".xlsx"

with open(file_path, "wb") as f:
  f.write(pdf_data)
