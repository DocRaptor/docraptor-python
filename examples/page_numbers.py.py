import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

document_content = r"""
    <div style="page-break-after: always;">Page 1</div>
    <div style="page-break-after: always;">Page 2</div>
    <div style="page-break-after: always;">Page 3</div>
    <div id="page4" style="page-break-after: always;">Page 4, with reset page counter</div>

    <style>
      @page {
        @bottom {
          content: "Page " counter(page, upper-alpha) " of " counter(pages, decimal);
        }
      }

      #page4 {
        counter-reset: page 1
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
        # 'prince_options': # {
        #    'media': 'print', # @media 'screen' or 'print' CSS
        #    'baseurl': 'https://yoursite.com', # the base URL for any relative URLs
        # },
    })

    # create_doc() returns a binary string
    with open('page-numbers.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created page-numbers.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
