import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

document_content = r"""
    <h1>This document has printer's marks!</h1>
    <style>
      @page {
        -prince-mark-length: 1cm;
        -prince-mark-offset: 0.25cm; /* offset between marks and page area, defaults to bleed */
        -prince-mark-width: 1px;
        marks: crop cross;
        size: 8cm 8cm;
        -prince-trim: 0.25cm;
        bleed: 0.75cm;
        margin: 0;
        background-color: #489bcf;
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
    with open('printers-marks.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created printers-marks.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
