# As a paid add-on, DocRaptor can provide long-term, publicly-accessible hosting for your documents.
# This allows you to provide a URL to your end users, third party tools like Zapier and Salesforce,
# or anyone else. We'll host the document on your behalf at a completely unbranded URL for as long
# as you want, or within the limits you specify.
#
# This example demonstrates creating a PDF using common options that DocRaptor will host for you.
# By default, hosted documents do not have limits on downloads or hosting time, though you may
# pass additional parameters to the document generation call to set your own limits. Learn more
# about the specific options in the hosted API documentation.
# https://docraptor.com/documentation/api#api_hosted
#
# The document is created asynchronously, which means DocRaptor will allow it to generate for up to
# 10 minutes. This is useful when creating many documents in parallel, or very large documents with
# lots of assets.
#
# DocRaptor supports many CSS and API options for output customization. Visit
# https://docraptor.com/documentation/ for full details.
#
# You can run this example with: python hosted_async.py

import docraptor
import time

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

try:
    # different method than synchronous or non-hosted documents
    response = doc_api.create_hosted_async_doc({
        'test': True,  # test documents are free but watermarked
        'document_type': 'pdf',
        'document_content': '<html><body>Hello World!</body></html>',
        # 'document_url': 'https://docraptor.com/examples/invoice.html',
        # 'javascript': True,
        # 'prince_options': # {
        #    'media': 'print', # @media 'screen' or 'print' CSS
        #    'baseurl': 'https://yoursite.com', # the base URL for any relative URLs
        # },
    })

    while True:
        status_response = doc_api.get_async_doc_status(response.status_id)
        if status_response.status == "completed":
            print(
                f"The asynchronously-generated PDF is hosted at {status_response.download_url}")
            break
        elif status_response.status == "failed":
            print("FAILED")
            print(status_response)
            break
        else:
            time.sleep(1)
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
