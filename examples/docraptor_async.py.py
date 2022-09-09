import docraptor
import time

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

try:
    # different method than the synchronous documents
    response = doc_api.create_async_doc({
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

    while True:
        status_response = doc_api.get_async_doc_status(response.status_id)
        if status_response.status == "completed":
            pdf = doc_api.get_async_doc(status_response.download_id)
            # get_async_doc() returns a binary string
            with open("docraptor-async.pdf", "wb") as f:
                f.write(pdf)
            print('Wrote PDF to docraptor-async.pdf')
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
