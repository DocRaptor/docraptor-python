import docraptor
import time
import datetime
import urllib.request
import os
import platform

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow_s = tomorrow.strftime('%Y-%m-%dT%H:%M:%S%z')

status_response = doc_api.create_hosted_doc({
  "test":             True,
  "document_content": "<html><body>Hello from Python</body></html>",
  "name":             "python-sync.pdf",
  "document_type":    "pdf",
  "hosted_expires_at": tomorrow_s,
})

download_response = urllib.request.urlopen(status_response.download_url)
pdf_data = download_response.read()

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


doc_api.expire(status_response.download_id)
try:
  urllib.request.urlopen(status_response.download_url)
  raise ValueError("Document should not exist")
except urllib.error.HTTPError as error:
  success = "expected error"


