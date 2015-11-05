# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Doc(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Doc - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'document_type': 'str',
            'document_content': 'str',
            'document_url': 'str',
            'test': 'bool',
            'strict': 'str',
            'tag': 'str',
            'help': 'bool',
            'javascript': 'bool',
            'referrer': 'str',
            'callback_url': 'str',
            'prince_options': 'PrinceOptions'
        }

        self.attribute_map = {
            'name': 'name',
            'document_type': 'document_type',
            'document_content': 'document_content',
            'document_url': 'document_url',
            'test': 'test',
            'strict': 'strict',
            'tag': 'tag',
            'help': 'help',
            'javascript': 'javascript',
            'referrer': 'referrer',
            'callback_url': 'callback_url',
            'prince_options': 'prince_options'
        }

        self._name = None
        self._document_type = None
        self._document_content = None
        self._document_url = None
        self._test = None
        self._strict = None
        self._tag = None
        self._help = None
        self._javascript = None
        self._referrer = None
        self._callback_url = None
        self._prince_options = None

    @property
    def name(self):
        """
        Gets the name of this Doc.
        A name for identifying your document.

        :return: The name of this Doc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Doc.
        A name for identifying your document.

        :param name: The name of this Doc.
        :type: str
        """
        self._name = name

    @property
    def document_type(self):
        """
        Gets the document_type of this Doc.
        The type of document being created.

        :return: The document_type of this Doc.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """
        Sets the document_type of this Doc.
        The type of document being created.

        :param document_type: The document_type of this Doc.
        :type: str
        """
        allowed_values = ["pdf", "xls", "xlsx"]
        if document_type not in allowed_values:
            raise ValueError(
                "Invalid value for `document_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._document_type = document_type

    @property
    def document_content(self):
        """
        Gets the document_content of this Doc.
        The HTML data to be transformed into a document.\nYou must supply content using document_content or document_url.

        :return: The document_content of this Doc.
        :rtype: str
        """
        return self._document_content

    @document_content.setter
    def document_content(self, document_content):
        """
        Sets the document_content of this Doc.
        The HTML data to be transformed into a document.\nYou must supply content using document_content or document_url.

        :param document_content: The document_content of this Doc.
        :type: str
        """
        self._document_content = document_content

    @property
    def document_url(self):
        """
        Gets the document_url of this Doc.
        The URL to fetch the HTML data to be transformed into a document.\nYou must supply content using document_content or document_url.

        :return: The document_url of this Doc.
        :rtype: str
        """
        return self._document_url

    @document_url.setter
    def document_url(self, document_url):
        """
        Sets the document_url of this Doc.
        The URL to fetch the HTML data to be transformed into a document.\nYou must supply content using document_content or document_url.

        :param document_url: The document_url of this Doc.
        :type: str
        """
        self._document_url = document_url

    @property
    def test(self):
        """
        Gets the test of this Doc.
        Enable test mode for this document. Test documents are not charged for but include a watermark.

        :return: The test of this Doc.
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """
        Sets the test of this Doc.
        Enable test mode for this document. Test documents are not charged for but include a watermark.

        :param test: The test of this Doc.
        :type: bool
        """
        self._test = test

    @property
    def strict(self):
        """
        Gets the strict of this Doc.
        Force strict HTML validation.

        :return: The strict of this Doc.
        :rtype: str
        """
        return self._strict

    @strict.setter
    def strict(self, strict):
        """
        Sets the strict of this Doc.
        Force strict HTML validation.

        :param strict: The strict of this Doc.
        :type: str
        """
        allowed_values = ["none"]
        if strict not in allowed_values:
            raise ValueError(
                "Invalid value for `strict`, must be one of {0}"
                .format(allowed_values)
            )
        self._strict = strict

    @property
    def tag(self):
        """
        Gets the tag of this Doc.
        A field for storing a small amount of metadata with this document.

        :return: The tag of this Doc.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this Doc.
        A field for storing a small amount of metadata with this document.

        :param tag: The tag of this Doc.
        :type: str
        """
        self._tag = tag

    @property
    def help(self):
        """
        Gets the help of this Doc.
        Request support help with this request if it succeeds.

        :return: The help of this Doc.
        :rtype: bool
        """
        return self._help

    @help.setter
    def help(self, help):
        """
        Sets the help of this Doc.
        Request support help with this request if it succeeds.

        :param help: The help of this Doc.
        :type: bool
        """
        self._help = help

    @property
    def javascript(self):
        """
        Gets the javascript of this Doc.
        Enable DocRaptor JavaScript parsing. PrinceXML JavaScript parsing is also available elsewhere.

        :return: The javascript of this Doc.
        :rtype: bool
        """
        return self._javascript

    @javascript.setter
    def javascript(self, javascript):
        """
        Sets the javascript of this Doc.
        Enable DocRaptor JavaScript parsing. PrinceXML JavaScript parsing is also available elsewhere.

        :param javascript: The javascript of this Doc.
        :type: bool
        """
        self._javascript = javascript

    @property
    def referrer(self):
        """
        Gets the referrer of this Doc.
        Set HTTP referrer when generating this document.

        :return: The referrer of this Doc.
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """
        Sets the referrer of this Doc.
        Set HTTP referrer when generating this document.

        :param referrer: The referrer of this Doc.
        :type: str
        """
        self._referrer = referrer

    @property
    def callback_url(self):
        """
        Gets the callback_url of this Doc.
        A URL that will receive a POST request after successfully completing an asynchronous document.\nThe POST data will include download_url and download_id similar to status api responses.\nWARNING: this only works on asynchronous documents.

        :return: The callback_url of this Doc.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """
        Sets the callback_url of this Doc.
        A URL that will receive a POST request after successfully completing an asynchronous document.\nThe POST data will include download_url and download_id similar to status api responses.\nWARNING: this only works on asynchronous documents.

        :param callback_url: The callback_url of this Doc.
        :type: str
        """
        self._callback_url = callback_url

    @property
    def prince_options(self):
        """
        Gets the prince_options of this Doc.


        :return: The prince_options of this Doc.
        :rtype: PrinceOptions
        """
        return self._prince_options

    @prince_options.setter
    def prince_options(self, prince_options):
        """
        Sets the prince_options of this Doc.


        :param prince_options: The prince_options of this Doc.
        :type: PrinceOptions
        """
        self._prince_options = prince_options

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
