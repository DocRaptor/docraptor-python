# coding: utf-8

"""
    DocRaptor

    A native client library for the DocRaptor HTML to PDF/XLS service.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from docraptor.configuration import Configuration


class Doc(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'document_type': 'str',
        'document_content': 'str',
        'document_url': 'str',
        'test': 'bool',
        'pipeline': 'str',
        'strict': 'str',
        'ignore_resource_errors': 'bool',
        'ignore_console_messages': 'bool',
        'tag': 'str',
        'help': 'bool',
        'javascript': 'bool',
        'referrer': 'str',
        'callback_url': 'str',
        'hosted_download_limit': 'int',
        'hosted_expires_at': 'str',
        'prince_options': 'PrinceOptions'
    }

    attribute_map = {
        'name': 'name',
        'document_type': 'document_type',
        'document_content': 'document_content',
        'document_url': 'document_url',
        'test': 'test',
        'pipeline': 'pipeline',
        'strict': 'strict',
        'ignore_resource_errors': 'ignore_resource_errors',
        'ignore_console_messages': 'ignore_console_messages',
        'tag': 'tag',
        'help': 'help',
        'javascript': 'javascript',
        'referrer': 'referrer',
        'callback_url': 'callback_url',
        'hosted_download_limit': 'hosted_download_limit',
        'hosted_expires_at': 'hosted_expires_at',
        'prince_options': 'prince_options'
    }

    def __init__(self, name=None, document_type=None, document_content=None, document_url=None, test=True, pipeline=None, strict=None, ignore_resource_errors=True, ignore_console_messages=False, tag=None, help=False, javascript=False, referrer=None, callback_url=None, hosted_download_limit=None, hosted_expires_at=None, prince_options=None, local_vars_configuration=None):  # noqa: E501
        """Doc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._document_type = None
        self._document_content = None
        self._document_url = None
        self._test = None
        self._pipeline = None
        self._strict = None
        self._ignore_resource_errors = None
        self._ignore_console_messages = None
        self._tag = None
        self._help = None
        self._javascript = None
        self._referrer = None
        self._callback_url = None
        self._hosted_download_limit = None
        self._hosted_expires_at = None
        self._prince_options = None
        self.discriminator = None

        self.name = name
        self.document_type = document_type
        if document_content is not None:
            self.document_content = document_content
        if document_url is not None:
            self.document_url = document_url
        if test is not None:
            self.test = test
        if pipeline is not None:
            self.pipeline = pipeline
        if strict is not None:
            self.strict = strict
        if ignore_resource_errors is not None:
            self.ignore_resource_errors = ignore_resource_errors
        if ignore_console_messages is not None:
            self.ignore_console_messages = ignore_console_messages
        if tag is not None:
            self.tag = tag
        if help is not None:
            self.help = help
        if javascript is not None:
            self.javascript = javascript
        if referrer is not None:
            self.referrer = referrer
        if callback_url is not None:
            self.callback_url = callback_url
        if hosted_download_limit is not None:
            self.hosted_download_limit = hosted_download_limit
        if hosted_expires_at is not None:
            self.hosted_expires_at = hosted_expires_at
        if prince_options is not None:
            self.prince_options = prince_options

    @property
    def name(self):
        """Gets the name of this Doc.  # noqa: E501

        A name for identifying your document.  # noqa: E501

        :return: The name of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Doc.

        A name for identifying your document.  # noqa: E501

        :param name: The name of this Doc.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def document_type(self):
        """Gets the document_type of this Doc.  # noqa: E501

        The type of document being created.  # noqa: E501

        :return: The document_type of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this Doc.

        The type of document being created.  # noqa: E501

        :param document_type: The document_type of this Doc.  # noqa: E501
        :type document_type: str
        """
        if self.local_vars_configuration.client_side_validation and document_type is None:  # noqa: E501
            raise ValueError("Invalid value for `document_type`, must not be `None`")  # noqa: E501
        allowed_values = ["pdf", "xls", "xlsx"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and document_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `document_type` ({0}), must be one of {1}"  # noqa: E501
                .format(document_type, allowed_values)
            )

        self._document_type = document_type

    @property
    def document_content(self):
        """Gets the document_content of this Doc.  # noqa: E501

        The HTML data to be transformed into a document. You must supply content using document_content or document_url.   # noqa: E501

        :return: The document_content of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._document_content

    @document_content.setter
    def document_content(self, document_content):
        """Sets the document_content of this Doc.

        The HTML data to be transformed into a document. You must supply content using document_content or document_url.   # noqa: E501

        :param document_content: The document_content of this Doc.  # noqa: E501
        :type document_content: str
        """

        self._document_content = document_content

    @property
    def document_url(self):
        """Gets the document_url of this Doc.  # noqa: E501

        The URL to fetch the HTML data to be transformed into a document. You must supply content using document_content or document_url.   # noqa: E501

        :return: The document_url of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._document_url

    @document_url.setter
    def document_url(self, document_url):
        """Sets the document_url of this Doc.

        The URL to fetch the HTML data to be transformed into a document. You must supply content using document_content or document_url.   # noqa: E501

        :param document_url: The document_url of this Doc.  # noqa: E501
        :type document_url: str
        """

        self._document_url = document_url

    @property
    def test(self):
        """Gets the test of this Doc.  # noqa: E501

        Enable test mode for this document. Test documents are not charged for but include a watermark.  # noqa: E501

        :return: The test of this Doc.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this Doc.

        Enable test mode for this document. Test documents are not charged for but include a watermark.  # noqa: E501

        :param test: The test of this Doc.  # noqa: E501
        :type test: bool
        """

        self._test = test

    @property
    def pipeline(self):
        """Gets the pipeline of this Doc.  # noqa: E501

        Specify a specific verison of the DocRaptor Pipeline to use.  # noqa: E501

        :return: The pipeline of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this Doc.

        Specify a specific verison of the DocRaptor Pipeline to use.  # noqa: E501

        :param pipeline: The pipeline of this Doc.  # noqa: E501
        :type pipeline: str
        """

        self._pipeline = pipeline

    @property
    def strict(self):
        """Gets the strict of this Doc.  # noqa: E501

        Force strict HTML validation.  # noqa: E501

        :return: The strict of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._strict

    @strict.setter
    def strict(self, strict):
        """Sets the strict of this Doc.

        Force strict HTML validation.  # noqa: E501

        :param strict: The strict of this Doc.  # noqa: E501
        :type strict: str
        """
        allowed_values = ["none", "html"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and strict not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `strict` ({0}), must be one of {1}"  # noqa: E501
                .format(strict, allowed_values)
            )

        self._strict = strict

    @property
    def ignore_resource_errors(self):
        """Gets the ignore_resource_errors of this Doc.  # noqa: E501

        Failed loading of images/javascripts/stylesheets/etc. will not cause the rendering to stop.  # noqa: E501

        :return: The ignore_resource_errors of this Doc.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_resource_errors

    @ignore_resource_errors.setter
    def ignore_resource_errors(self, ignore_resource_errors):
        """Sets the ignore_resource_errors of this Doc.

        Failed loading of images/javascripts/stylesheets/etc. will not cause the rendering to stop.  # noqa: E501

        :param ignore_resource_errors: The ignore_resource_errors of this Doc.  # noqa: E501
        :type ignore_resource_errors: bool
        """

        self._ignore_resource_errors = ignore_resource_errors

    @property
    def ignore_console_messages(self):
        """Gets the ignore_console_messages of this Doc.  # noqa: E501

        Prevent console.log from stopping document rendering during JavaScript execution.  # noqa: E501

        :return: The ignore_console_messages of this Doc.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_console_messages

    @ignore_console_messages.setter
    def ignore_console_messages(self, ignore_console_messages):
        """Sets the ignore_console_messages of this Doc.

        Prevent console.log from stopping document rendering during JavaScript execution.  # noqa: E501

        :param ignore_console_messages: The ignore_console_messages of this Doc.  # noqa: E501
        :type ignore_console_messages: bool
        """

        self._ignore_console_messages = ignore_console_messages

    @property
    def tag(self):
        """Gets the tag of this Doc.  # noqa: E501

        A field for storing a small amount of metadata with this document.  # noqa: E501

        :return: The tag of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Doc.

        A field for storing a small amount of metadata with this document.  # noqa: E501

        :param tag: The tag of this Doc.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def help(self):
        """Gets the help of this Doc.  # noqa: E501

        Request support help with this request if it succeeds.  # noqa: E501

        :return: The help of this Doc.  # noqa: E501
        :rtype: bool
        """
        return self._help

    @help.setter
    def help(self, help):
        """Sets the help of this Doc.

        Request support help with this request if it succeeds.  # noqa: E501

        :param help: The help of this Doc.  # noqa: E501
        :type help: bool
        """

        self._help = help

    @property
    def javascript(self):
        """Gets the javascript of this Doc.  # noqa: E501

        Enable DocRaptor JavaScript parsing. PrinceXML JavaScript parsing is also available elsewhere.  # noqa: E501

        :return: The javascript of this Doc.  # noqa: E501
        :rtype: bool
        """
        return self._javascript

    @javascript.setter
    def javascript(self, javascript):
        """Sets the javascript of this Doc.

        Enable DocRaptor JavaScript parsing. PrinceXML JavaScript parsing is also available elsewhere.  # noqa: E501

        :param javascript: The javascript of this Doc.  # noqa: E501
        :type javascript: bool
        """

        self._javascript = javascript

    @property
    def referrer(self):
        """Gets the referrer of this Doc.  # noqa: E501

        Set HTTP referrer when generating this document.  # noqa: E501

        :return: The referrer of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this Doc.

        Set HTTP referrer when generating this document.  # noqa: E501

        :param referrer: The referrer of this Doc.  # noqa: E501
        :type referrer: str
        """

        self._referrer = referrer

    @property
    def callback_url(self):
        """Gets the callback_url of this Doc.  # noqa: E501

        A URL that will receive a POST request after successfully completing an asynchronous document. The POST data will include download_url and download_id similar to status API responses. WARNING: this only works on asynchronous documents.   # noqa: E501

        :return: The callback_url of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this Doc.

        A URL that will receive a POST request after successfully completing an asynchronous document. The POST data will include download_url and download_id similar to status API responses. WARNING: this only works on asynchronous documents.   # noqa: E501

        :param callback_url: The callback_url of this Doc.  # noqa: E501
        :type callback_url: str
        """

        self._callback_url = callback_url

    @property
    def hosted_download_limit(self):
        """Gets the hosted_download_limit of this Doc.  # noqa: E501

        The number of times a hosted document can be downloaded.  If no limit is specified, the document will be available for an unlimited number of downloads.  # noqa: E501

        :return: The hosted_download_limit of this Doc.  # noqa: E501
        :rtype: int
        """
        return self._hosted_download_limit

    @hosted_download_limit.setter
    def hosted_download_limit(self, hosted_download_limit):
        """Sets the hosted_download_limit of this Doc.

        The number of times a hosted document can be downloaded.  If no limit is specified, the document will be available for an unlimited number of downloads.  # noqa: E501

        :param hosted_download_limit: The hosted_download_limit of this Doc.  # noqa: E501
        :type hosted_download_limit: int
        """

        self._hosted_download_limit = hosted_download_limit

    @property
    def hosted_expires_at(self):
        """Gets the hosted_expires_at of this Doc.  # noqa: E501

        The date and time at which a hosted document will be removed and no longer available. Must be a properly formatted ISO 8601 datetime, like 1981-01-23T08:02:30-05:00.  # noqa: E501

        :return: The hosted_expires_at of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._hosted_expires_at

    @hosted_expires_at.setter
    def hosted_expires_at(self, hosted_expires_at):
        """Sets the hosted_expires_at of this Doc.

        The date and time at which a hosted document will be removed and no longer available. Must be a properly formatted ISO 8601 datetime, like 1981-01-23T08:02:30-05:00.  # noqa: E501

        :param hosted_expires_at: The hosted_expires_at of this Doc.  # noqa: E501
        :type hosted_expires_at: str
        """

        self._hosted_expires_at = hosted_expires_at

    @property
    def prince_options(self):
        """Gets the prince_options of this Doc.  # noqa: E501


        :return: The prince_options of this Doc.  # noqa: E501
        :rtype: PrinceOptions
        """
        return self._prince_options

    @prince_options.setter
    def prince_options(self, prince_options):
        """Sets the prince_options of this Doc.


        :param prince_options: The prince_options of this Doc.  # noqa: E501
        :type prince_options: PrinceOptions
        """

        self._prince_options = prince_options

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Doc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Doc):
            return True

        return self.to_dict() != other.to_dict()
