# DocRaptor Python Native Client Library

This is a Python package for using [DocRaptor API](https://docraptor.com/documentation) to convert [HTML to PDF and XLSX](https://docraptor.com). It is compatible with Python 3.


## Installation

```bash
pip install --upgrade docraptor
```

or

```bash
easy_install --upgrade docraptor
```

If you are on a system with `easy_install` but not [`pip`](http://www.pip-installer.org/en/latest/index.html), you can use `easy_install` instead. If you're not using [`virtualenv`](http://www.virtualenv.org/), you may have to prefix those commands with `sudo`.


## Basic Usage

```python
import docraptor

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'   # this key works for test documents
# doc_api.api_client.configuration.debug = True

response = doc_api.create_doc({
  "test": True,                                                   # test documents are free but watermarked
  "document_content": "<html><body>Hello World</body></html>",    # supply content directly
  # "document_url": "http://docraptor.com/examples/invoice.html", # or use a url
  "name": "docraptor-python.pdf",                                 # help you find a document later
  "document_type": "pdf",                                         # pdf or xls or xlsx
  # "javascript": True,                                           # enable JavaScript processing
  # "prince_options": {
  #   "media": "screen",                                          # use screen styles instead of print styles
  #   "baseurl": "http://hello.com",                              # pretend URL when using document_content
  # },
})
```
## Next Steps

- Optionally store and get a URL for your converted document with [document hosting](https://docraptor.com/document-hosting)
- View more [code examples](examples) with error handling, asynchronous creation, file saving, and document hosting.
- Perfect your document styling with our [knowledge base](https://help.docraptor.com), [style and formatting reference](https://docraptor.com/documentation/style), and [API reference](https://docraptor.com/documentation/api). Easily add headers and footers, page breaks, page numbers, table of contents, and much more!

## More Help

Stuck? We're experts at turning HTML into PDFs so please [email us](mailto:support@docraptor.com) if you run into trouble.


## Development

The majority of the code in this repo is generated using swagger-codegen on [docraptor.yaml](docraptor.yaml). You can modify this file and regenerate the client using `script/generate_language python`.

The generated client needed a few fixes
- https://github.com/swagger-api/swagger-codegen/issues/2305


## Release Process

1. Pull latest master
2. Merge feature branch(es) into master
3. `script/test`
4. Increment version in code:
  - `swagger-config.json`
  - `setup.py`
  - `docraptor/api_client.py`
  - `docraptor/configuration.py`
5. Update [CHANGELOG.md](CHANGELOG.md)
6. Commit "Release version vX.Y.Z"
7. Push to GitHub
8. Tag version: `git tag 'vX.Y.Z' && git push --tags`
9. Clean out any old packages `rm dist/*`
10. Build packages `python setup.py sdist bdist_wheel`
11. Upload packages `twine upload dist/*`
12. Verify package release at https://pypi.python.org/pypi/docraptor
13. Update documentation on docraptor.com


## Version Policy

This library follows [Semantic Versioning 2.0.0](http://semver.org).
