import docraptor
import time

docraptor.configuration.username = "YOUR_API_KEY_HERE"
docraptor.configuration.debug = True

doc_api = docraptor.ClientApi()

response = doc_api.docs_post({"test": True, "document_content": "<html><body>Swagger Python</body></html>", "name": "swagger-python.pdf", "document_type": "pdf"})
