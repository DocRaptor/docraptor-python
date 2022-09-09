import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

try:
    response = doc_api.create_doc({
        'test': True,  # test documents are free but watermarked
        'document_type': 'pdf',
        'document_content': 'You cant print me!t print me!',
        # 'document_url': 'https://docraptor.com/examples/invoice.html',
        # 'javascript': False,
        'prince_options': {
            'encrypt': True,
            'disallow_print': True,
        },
    })

    # create_doc() returns a binary string
    with open('print-protection.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created print-protection.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
