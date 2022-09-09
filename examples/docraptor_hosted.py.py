import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

try:
    # different method than the non-hosted documents
    response = doc_api.create_hosted_doc({
        'test': True,  # test documents are free but watermarked
        'document_type': 'pdf',
        'document_content': '<html><body>Hello World!</body></html>',
        # 'document_url': 'https://docraptor.com/examples/invoice.html',
        # 'javascript': False,
        # 'prince_options': # {
        #    'media': 'print', # @media 'screen' or 'print' CSS
        #    'baseurl': 'https://yoursite.com', # the base URL for any relative URLs
        # },
    })

    print(f"The PDF is hosted at {response.download_url}")
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
