# DocRaptor Python Native Client Library

This is a Python package for using [DocRaptor API](https://docraptor.com/documentation) to convert [HTML to PDF and XLSX](https://docraptor.com).


## Installation

```bash
pip install --upgrade docraptor
```

or

```bash
easy_install --upgrade docraptor
```

If you are on a system with `easy_install` but not [`pip`](http://www.pip-installer.org/en/latest/index.html), you can use `easy_install` instead. If you're not using [`virtualenv`](http://www.virtualenv.org/), you may have to prefix those commands with `sudo`.


## Usage

See [examples](examples/) for runnable examples with file output, error handling, etc.

```python
import docraptor

docraptor.configuration.username = "YOUR_API_KEY_HERE" # this key works for test documents
# docraptor.configuration.debug = True

doc_api = docraptor.DocApi()

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

Docs created like this are limited to 60 seconds to render, check out the [async example](examples/async.py) which allows 10 minutes.

We have guides for doing some of the common things:

* [Headers and Footers](https://docraptor.com/documentation/style#pdf-headers-footers) including page skipping
* [CSS Media Selector](https://docraptor.com/documentation/api#api_basic_pdf) to make the page look exactly as it does in your browser
* Protect content with [HTTP authentication](https://docraptor.com/documentation/api#api_http_user) or [proxies](https://docraptor.com/documentation/api#api_http_proxy) so only DocRaptor can access them


## More Help

DocRaptor has a lot of more [styling](https://docraptor.com/documentation/style) and [implementation options](https://docraptor.com/documentation/api).

Stuck? We're experts at using DocRaptor so please [email us](mailto:support@docraptor.com) if you run into trouble.


## Development

The majority of the code in this repo is generated using swagger-codegen on [docraptor.yaml](docraptor.yaml). You can modify this file and regenerate the client using `script/generate_language python`.

The generated client needed a few fixes
- Python3 was forcing all encoding to utf8 on binary data


## Release Process

1. `script/test`
2. Increment version in code
  - `swagger-config.json`
  - `setup.py`
  - `docraptor/api_client.py`
  - `docraptor/configuration.py`
3. Update [CHANGELOG.md](CHANGELOG.md)
4. Tag version: `git tag 'v0.0.x' && git push --tags`
5. Push to GitHub
6. Build packages `python setup.py sdist bdist_wheel`
7. Upload packages `twine upload dist/*`
8. Update documentation on docraptor.com


## Version Policy

This library follows [Semantic Versioning 2.0.0](http://semver.org).
