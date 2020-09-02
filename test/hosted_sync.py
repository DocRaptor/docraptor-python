import docraptor
import time
import datetime
import urllib.request

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'
# doc_api.api_client.configuration.debug = True

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow_s = tomorrow.strftime('%Y-%m-%dT%H:%M:%S%z')

doc_status = doc_api.create_hosted_doc({
  "test":             True,
  "document_content": "<html><body>Hello from Python</body></html>",
  "name":             "python-sync.pdf",
  "document_type":    "pdf",
  "hosted_expires_at": tomorrow_s,
})

download_response = urllib.request.urlopen(doc_status.download_url)
decoded_response = download_response.read().decode('cp437')

if not decoded_response.startswith("%PDF-1.5"):
  raise ValueError(f"Invalid PDF expected: %PDF-1.5 recieved: {decoded_response[0:8]}")
