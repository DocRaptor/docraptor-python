import docraptor
import shutil

docraptor.configuration.username = "YOUR_API_KEY_HERE"
# docraptor.configuration.debug = True
doc_api = docraptor.DocApi()

create_response = doc_api.create_doc({
  "test": True,
  "document_content": "<html><body>Hello World</body></html>",
  "name": "docraptor-python.pdf",
  "document_type": "pdf",
})
file = open("/tmp/docraptor-python.pdf", "wb")
file.write(create_response)
file.close
