import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

document_content = r"""
    <div class="flex-column">
      <div class="flex-item red">1</div>
      <div class="flex-item green">2</div>
      <div class="flex-item blue">3</div>
    </div>
    <div class="flex-row">
      <div class="flex-item green">1</div>
      <div class="flex-item blue">2</div>
      <div class="flex-item red">3</div>
    </div>

    <style>
      .flex-column {
        display: flex;
        flex-direction: column;
      }

      .flex-row {
        display: flex;
        flex-direction: row;
      }

      .flex-item {
        flex: 1;
      }

      .flex-row .flex-item {
        /* simulate long content forcing a page break  */
        height: 1000px;
      }

      .red { background-color: red; }
      .green { background-color: green; }
      .blue { background-color: blue; }
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
    with open('css-flexbox.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created css-flexbox.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
