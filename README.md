# DocRaptor Python Native Client Library

**WARNING: This code is not production ready, you should use [this](https://docraptor.com/documentation/python).**

This is a Python package for using [DocRaptor API](http://docraptor.com/documentation) to convert HTML to PDF and XLSX.

## Installation

```sh
pip install --upgrade docraptor
```

or

```sh
easy_install --upgrade docraptor
```

See http://www.pip-installer.org/en/latest/index.html for instructions on installing pip. If you are on a system with easy_install but not pip, you can use easy_install instead. If you're not using virtualenv, you may have to prefix those commands with sudo. You can learn more about virtualenv at http://www.virtualenv.org/

## Usage

See [examples](examples/) for runnable examples with file output, error handling, etc.

```python
import docraptor

docraptor.configuration.username = "YOUR_API_KEY_HERE" # this key works for test documents
# docraptor.configuration.debug = True

doc_api = docraptor.ClientApi()

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
* [Protected Content](https://docraptor.com/documentation/api#api_advanced_pdf) to secure your URLs so only DocRaptor can access them

## More Help

DocRaptor has a lot of more [styling](https://docraptor.com/documentation/style) and [implementation options](https://docraptor.com/documentation/api).

Stuck? We're experts at using DocRaptor so please [email us](mailto:support@docraptor.com) if you run into trouble.


## Development

The majority of the code in this repo is generated using swagger-codegen on [docraptor.yaml](docraptor.yaml). You can modify this file and regenerate the client using `script/generate_language python`.

## Release Process

1. `script/test`
2. Increment version in code
  - `swagger-config.json`
  - `setup.py`
3. Update [CHANGELOG.md](CHANGELOG.md)
4. Tag version: `git tag 'v0.0.x' && git push --tags`
5. Push to GitHub
6. Build packages `python setup.py sdist bdist_wheel`
7. Upload packages `twine upload dist/*`

## Version Policy

This library follows [Semantic Versioning 2.0.0](http://semver.org).
