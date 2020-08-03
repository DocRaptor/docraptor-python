import docraptor
import shutil

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

create_response = doc_api.create_doc({
  "test": True,
  "document_content": "<html><body>Hello World</body></html>",
  "name": "docraptor-python.pdf",
  "document_type": "pdf",
})

with open("/tmp/docraptor-python.pdf", "wb") as f:
  f.write(create_response)

with open("/tmp/docraptor-python.pdf", "rb") as f:
  first_line = f.readline().decode('cp437')
  if "%PDF-1.5" not in first_line:
    raise ValueError("Invalid PDF")
