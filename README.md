# DocRaptor Python Native Client Library

**WARNING: This code is not production ready, you should use https://docraptor.com/documentation/python **

This is a Python package for using [DocRaptor API](http://docraptor.com/documentation) to convert HTML to PDF and XLSX.

## Installation

Add the following to your `Gemfile`.

```sh
pip install --upgrade docraptor
```

or

```sh
easy_install --upgrade docraptor
```

See http://www.pip-installer.org/en/latest/index.html for instructions on installing pip. If you are on a system with easy_install but not pip, you can use easy_install instead. If you're not using virtualenv, you may have to prefix those commands with sudo. You can learn more about virtualenv at http://www.virtualenv.org/

## Usage

```python
import docraptor

docraptor.configuration.username = "YOUR_API_KEY_HERE"
# docraptor.configuration.debug = True

global docraptor = docraptor.ClientApi()

response = docraptor.create_doc({
  "test": True,                                                   # test documents are free but watermarked
  "document_content": "<html><body>Python</body></html>",         # supply content directly
  # "document_url": "http://docraptor.com/examples/invoice.html", # or use a url
  "name": "swagger-python.pdf",                                   # help you find a document later
  "document_type": "pdf",                                         # pdf or xls or xlsx
  # "javascript": True,                                           # enable JavaScript processing
  # "prince_options": {
  #   "media": "screen",                                          # use screen styles instead of print styles
  #   "baseurl": "http://hello.com",                              # pretend URL when using document_content
  # },
})
```

If your document will take longer than 60 seconds to render to PDF you will need to use our async api which allows up to 10 minutes, check out the [example](example/async.py).


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

1. Merge code
2. `script/test`
3. Increment version in code
4. Update [CHANGELOG.md](CHANGELOG.md)
5. Push to GitHub
6. Release TODO

## Version Policy

This library follows [Semantic Versioning 2.0.0](http://semver.org).
