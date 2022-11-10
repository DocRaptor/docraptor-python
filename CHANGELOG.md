### 3.0.0 [TBD]
* Switch API host to more secure api.docraptor.com (dropping old TLS)
* Switch from swagger to openapi-generator v6.0.1 (better maintained)
* Remove support for python <3.4

### 2.0.0 [July 31, 2020]
* Drop Support for Python 2
  _(We will now only develop and test against Python 3)_
* Add support for hosted documents
* Upgrade to latest swagger 2.4.14
* **BREAKING CHANGE**: DocApi configuration must now be configured per instance

### 1.2.0 [November 3, 2016]
* Added support for the pipeline API parameter

### 1.1.0 [September 27, 2016]
* Added support for prince_options[no_parallel_downloads]

### 1.0.0 [May 13, 2016]
* No significant code changes

### 0.3.0 [March 12, 2016]
* Added support for prince_options[debug]

### 0.2.1 [March 3, 2016]
* Python 3 support

### 0.2.0 [January 29, 2016]
* **BREAKING CHANGE**: Rename ClientApi to DocApi

### 0.1.0 [January 27, 2016]
* **BREAKING CHANGE**: create_doc and get_async_doc responses are now binary strings instead of temp files

### 0.0.1 [January 16, 2016]
* Initial release
