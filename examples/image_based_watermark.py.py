import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

document_content = r"""
    <div id="watermark"><img src="https://docraptor-production-cdn.s3.amazonaws.com/tutorials/raptor.png" /></div>
    <div style="page-break-after: always;">Page 1</div>
    <div style="page-break-after: always;">Page 2</div>
    <div style="page-break-after: always;">Page 3</div>

    <style>
      #watermark {
        flow: static(watermarkflow);
        opacity: 0.7;
        text-align: center;
      }

      @page {
         @prince-overlay {
            content: flow(watermarkflow);
         }
      }
    </style>
"""

try:
    response = doc_api.create_doc({
        'test': False,  # test documents are free but watermarked
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
    with open('image-based-watermark.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created image-based-watermark.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
