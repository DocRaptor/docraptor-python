import docraptor
import time

docraptor.configuration.username = "YOUR_API_KEY_HERE"
docraptor.configuration.debug = True

doc_api = docraptor.ClientApi()

response = doc_api.docs_post({"test": True, "document_content": "<html><body><table><tr><td>Swagger Python</td></tr></table></body></html>", "name": "swagger-python.xlsx", "document_type": "xlsx"})
