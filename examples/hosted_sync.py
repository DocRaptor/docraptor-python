# As a paid add-on, DocRaptor can provide long-term, publicly-accessible hosting for your documents.
# This allows you to provide a URL to your end users, third party tools like Zapier and Salesforce,
# or anyone else. We'll host the document on your behalf at a completely unbranded URL for as long
# as you want, or within the limits you specify.
#
# This example demonstrates creating a PDF that DocRaptor will host for you using common options.
# By default, hosted documents do not have limits on downloads or hosting time, though you may
# pass additional parameters to the document generation call to set your own limits. Learn more
# about the specific options in the hosted API documentation.
# https://docraptor.com/documentation/api#api_hosted
#
# It is created synchronously, which means DocRaptor will allow it to generate for up to 60 seconds.
# Since this document will be hosted by DocRaptor the response from this request will return a JSON
# formatted object containing public URL where the document can be downloaded from.
#
# DocRaptor supports many options for output customization, the full list is
# https://docraptor.com/documentation/api#api_general
#
# You can run this example with: python sync.rb

import docraptor
import shutil

configuration = docraptor.Configuration()
configuration.username = "YOUR_API_KEY_HERE" # you will need a real api key to test hosted documents
# docraptor.configuration.debug = True
doc_api = docraptor.DocApi(docraptor.ApiClient(configuration))

try:

  create_response = doc_api.create_hosted_doc({
    "test": True,                                                   # test documents are free but watermarked
    "document_content": "<html><body>Hello World</body></html>",    # supply content directly
    # "document_url": "http://docraptor.com/examples/invoice.html", # or use a url
    "name": "docraptor-python.pdf",                                 # help you find a document later
    "document_type": "pdf",                                         # pdf or xls or xlsx
    # "javascript": True,                                           # enable JavaScript processing
    # "prince_options": {
    #   "media": "screen",                                          # use screen styles instead of print styles
    #   "baseurl": "http://hello.com",                              # pretend URL when using document_content
    # },
  })
  print(f"The hosted PDF is now available for public download at {create_response.download_url}")
  doc_response = doc_api.get_async_doc(create_response.download_id)
  with open("/tmp/docraptor-python.pdf", "wb") as f:
    f.write(doc_response)
  print("Wrote PDF to /tmp/docraptor-python.pdf")

except docraptor.rest.ApiException as error:
  print(error)
  print(error.message)
  print(error.code)
  print(error.response_body)
