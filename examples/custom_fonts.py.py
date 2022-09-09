import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

document_content = r"""
    <h2>Custom Fonts</h2>
    <p>Hi, my name is Arial.</p>
    <p class='custom-font'>I wish to walk on the beach... On warm, Open Sans.</p>

    <style>
      @font-face {
        font-family: 'Open Sans';
        font-style: normal;
        font-weight: 300;
        src: local('Open Sans Light'), local('OpenSans-Light'), url(http://themes.googleusercontent.com/static/fonts/opensans/v8/DXI1ORHCpsQm3Vp6mXoaTaRDOzjiPcYnFooOUGCOsRk.woff) format('woff');
      }
      p {
        font-family: Arial, Helvetica, sans-serif;
      }
      p.custom-font {
        font-family: 'Open Sans', sans-serif;
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
    with open('custom-fonts.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created custom-fonts.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
