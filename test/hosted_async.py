import docraptor
import time
import datetime
import urllib.request

with open("../.docraptor_key") as f:
  api_key = f.readline().strip()

if not api_key:
  raise ValueError("Please put a valid (paid plan) api key in the .docraptor_key file when testing this feature.")

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = api_key
# doc_api.api_client.configuration.debug = True

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow_s = tomorrow.strftime('%Y-%m-%dT%H:%M:%S%z')

create_response = doc_api.create_hosted_async_doc({
  "test":             True,
  "document_content": "<html><body>Hello from Python</body></html>",
  "name":             "python-async.pdf",
  "document_type":    "pdf",
  "hosted_expires_at": tomorrow_s,
})

status_response = None
while True:
  status_response = doc_api.get_async_doc_status(create_response.status_id)
  if status_response.status == "completed":
    break
  elif status_response.status == "failed":
    raise ValueError("Failed creating hosted async document")
  time.sleep(1)

download_response = urllib.request.urlopen(status_response.download_url)
decoded_response = download_response.read().decode('cp437')

if not decoded_response.startswith("%PDF-1.5"):
  raise ValueError(f"Invalid PDF expected: %PDF-1.5 recieved: {decoded_response[0:8]}")