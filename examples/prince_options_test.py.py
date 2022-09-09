import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

document_content = r"""
    <html><body>
      <h1>Hello World!</h1>
    </body></html>

    <style>
      h1 {
        display: none;
      }
      @media screen {
        h1 {
          display: block;
        }
      }
    </style>
"""

try:
    response = doc_api.create_doc({
        'test': True,  # test documents are free but watermarked
        'document_type': 'pdf',
        'document_content': document_content,
        # 'document_url': 'https://docraptor.com/examples/invoice.html',
        # 'javascript': False,
        'prince_options': {
            'media': 'screen',
            'baseurl': 'https://yoursite.com',
        },
    })

    # create_doc() returns a binary string
    with open('prince-options-test.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created prince-options-test.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
