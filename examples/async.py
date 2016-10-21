# This example demonstrates creating a PDF using common options and saving it
# to a place on the filesystem.
#
# It is created asynchronously, which means DocRaptor will render it for up to
# 10 minutes. This is useful when creating many documents in parallel, or very
# large documents with lots of assets.
#
# DocRaptor supports many options for output customization, the full list is
# https://docraptor.com/documentation/api#api_general
#
# You can run this example with: python async.rb

import docraptor
import time
import shutil

docraptor.configuration.username = "YOUR_API_KEY_HERE" # this key works for test documents
# docraptor.configuration.debug = True
doc_api = docraptor.DocApi()

try:

  create_response = doc_api.create_async_doc({
    "test": True,                                                   # test documents are free but watermarked
    "document_content": "<html><body>Hello World</body></html>",    # supply content directly
    # "document_url": "http://docraptor.com/examples/invoice.html", # or use a url
    "type": "pdf",                                                  # pdf or xls or xlsx
    # "javascript": True,                                           # enable JavaScript processing
    # "prince_options": {
    #   "media": "screen",                                          # use screen styles instead of print styles
    #   "baseurl": "http://hello.com",                              # pretend URL when using document_content
    # },
  })

  while True:
    status_response = doc_api.get_async_doc_status(create_response.status_id)
    if status_response.status == "completed":
      doc_response = doc_api.get_async_doc(status_response.download_id)
      file = open("/tmp/docraptor-python.pdf", "wb")
      file.write(doc_response)
      file.close
      print("Wrote PDF to /tmp/docraptor-python.pdf")
      break
    elif status_response.status == "failed":
      print("FAILED")
      print(status_response)
      break
    else:
      time.sleep(1)

except docraptor.rest.ApiException as error:
  print(error)
  print(error.message)
  print(error.code)
  print(error.response_body)
