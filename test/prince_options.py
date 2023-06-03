import docraptor
import os
import platform

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

# Verify the test works as expected by confirming that this url will fail
# without prince_options[insecure]=true.
try:
  doc_api.create_doc({
    "test":             True,
    "document_url": "https://expired.badssl.com/",
    "name":             "python-sync.pdf",
    "document_type":    "pdf",
  })
except docraptor.exceptions.ApiException as ex:
  expected_message = "SSL Error downloading document content from supplied url."
  if expected_message not in str(ex):
    raise ValueError("Wrong exception, expected: " + expected_message + ", got: " + str(ex))

# Verify prince_options works by testing a url that will fail without
# prince_options[insecure]=true.
pdf_data = doc_api.create_doc({
  "test":             True,
  "document_url": "https://expired.badssl.com/",
  "name":             "python-sync.pdf",
  "document_type":    "pdf",
  "prince_options": {
    "insecure": True,
  },
})

file_path = "/app/tmp/test_output/" + os.path.basename(__file__) + "_python_" + platform.python_version() + ".pdf"

with open(file_path, "wb") as f:
  f.write(pdf_data)

stream = os.popen("qpdf --check " + file_path + " 2>&1")
output = stream.read()
close_value = stream.close()
if close_value is not None:
  with open(file_path, "rb") as f:
    decoded_response = f.read().decode('cp437')
    message = "Invalid PDF expected: %PDF-1.5 recieved:\n"
    message += decoded_response[0:8]
    message += "\n\nqpdf --check:\n" + output
    raise ValueError(message)

