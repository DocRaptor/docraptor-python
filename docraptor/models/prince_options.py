# coding: utf-8

"""
Copyright 2016 SmartBear Software

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


class PrinceOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PrinceOptions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'baseurl': 'str',
            'no_xinclude': 'bool',
            'no_network': 'bool',
            'http_user': 'str',
            'http_password': 'str',
            'http_proxy': 'str',
            'http_timeout': 'int',
            'insecure': 'bool',
            'media': 'str',
            'no_author_style': 'bool',
            'no_default_style': 'bool',
            'no_embed_fonts': 'bool',
            'no_subset_fonts': 'bool',
            'no_compress': 'bool',
            'encrypt': 'bool',
            'key_bits': 'int',
            'user_password': 'str',
            'owner_password': 'str',
            'disallow_print': 'bool',
            'disallow_copy': 'bool',
            'disallow_annotate': 'bool',
            'disallow_modify': 'bool',
            'input': 'str',
            'version': 'str',
            'javascript': 'bool',
            'css_dpi': 'int',
            'profile': 'str'
        }

        self.attribute_map = {
            'baseurl': 'baseurl',
            'no_xinclude': 'no_xinclude',
            'no_network': 'no_network',
            'http_user': 'http_user',
            'http_password': 'http_password',
            'http_proxy': 'http_proxy',
            'http_timeout': 'http_timeout',
            'insecure': 'insecure',
            'media': 'media',
            'no_author_style': 'no_author_style',
            'no_default_style': 'no_default_style',
            'no_embed_fonts': 'no_embed_fonts',
            'no_subset_fonts': 'no_subset_fonts',
            'no_compress': 'no_compress',
            'encrypt': 'encrypt',
            'key_bits': 'key_bits',
            'user_password': 'user_password',
            'owner_password': 'owner_password',
            'disallow_print': 'disallow_print',
            'disallow_copy': 'disallow_copy',
            'disallow_annotate': 'disallow_annotate',
            'disallow_modify': 'disallow_modify',
            'input': 'input',
            'version': 'version',
            'javascript': 'javascript',
            'css_dpi': 'css_dpi',
            'profile': 'profile'
        }

        self._baseurl = None
        self._no_xinclude = None
        self._no_network = None
        self._http_user = None
        self._http_password = None
        self._http_proxy = None
        self._http_timeout = None
        self._insecure = None
        self._media = 'print'
        self._no_author_style = None
        self._no_default_style = None
        self._no_embed_fonts = None
        self._no_subset_fonts = None
        self._no_compress = None
        self._encrypt = None
        self._key_bits = None
        self._user_password = None
        self._owner_password = None
        self._disallow_print = None
        self._disallow_copy = None
        self._disallow_annotate = None
        self._disallow_modify = None
        self._input = 'html'
        self._version = None
        self._javascript = None
        self._css_dpi = None
        self._profile = None

    @property
    def baseurl(self):
        """
        Gets the baseurl of this PrinceOptions.
        Set the baseurl for assets.

        :return: The baseurl of this PrinceOptions.
        :rtype: str
        """
        return self._baseurl

    @baseurl.setter
    def baseurl(self, baseurl):
        """
        Sets the baseurl of this PrinceOptions.
        Set the baseurl for assets.

        :param baseurl: The baseurl of this PrinceOptions.
        :type: str
        """
        self._baseurl = baseurl

    @property
    def no_xinclude(self):
        """
        Gets the no_xinclude of this PrinceOptions.
        Disable XML inclusion.

        :return: The no_xinclude of this PrinceOptions.
        :rtype: bool
        """
        return self._no_xinclude

    @no_xinclude.setter
    def no_xinclude(self, no_xinclude):
        """
        Sets the no_xinclude of this PrinceOptions.
        Disable XML inclusion.

        :param no_xinclude: The no_xinclude of this PrinceOptions.
        :type: bool
        """
        self._no_xinclude = no_xinclude

    @property
    def no_network(self):
        """
        Gets the no_network of this PrinceOptions.
        Disable network access.

        :return: The no_network of this PrinceOptions.
        :rtype: bool
        """
        return self._no_network

    @no_network.setter
    def no_network(self, no_network):
        """
        Sets the no_network of this PrinceOptions.
        Disable network access.

        :param no_network: The no_network of this PrinceOptions.
        :type: bool
        """
        self._no_network = no_network

    @property
    def http_user(self):
        """
        Gets the http_user of this PrinceOptions.
        Set the user for HTTP authentication.

        :return: The http_user of this PrinceOptions.
        :rtype: str
        """
        return self._http_user

    @http_user.setter
    def http_user(self, http_user):
        """
        Sets the http_user of this PrinceOptions.
        Set the user for HTTP authentication.

        :param http_user: The http_user of this PrinceOptions.
        :type: str
        """
        self._http_user = http_user

    @property
    def http_password(self):
        """
        Gets the http_password of this PrinceOptions.
        Set the password for HTTP authentication.

        :return: The http_password of this PrinceOptions.
        :rtype: str
        """
        return self._http_password

    @http_password.setter
    def http_password(self, http_password):
        """
        Sets the http_password of this PrinceOptions.
        Set the password for HTTP authentication.

        :param http_password: The http_password of this PrinceOptions.
        :type: str
        """
        self._http_password = http_password

    @property
    def http_proxy(self):
        """
        Gets the http_proxy of this PrinceOptions.
        Set the HTTP proxy server.

        :return: The http_proxy of this PrinceOptions.
        :rtype: str
        """
        return self._http_proxy

    @http_proxy.setter
    def http_proxy(self, http_proxy):
        """
        Sets the http_proxy of this PrinceOptions.
        Set the HTTP proxy server.

        :param http_proxy: The http_proxy of this PrinceOptions.
        :type: str
        """
        self._http_proxy = http_proxy

    @property
    def http_timeout(self):
        """
        Gets the http_timeout of this PrinceOptions.
        Set the HTTP request timeout.

        :return: The http_timeout of this PrinceOptions.
        :rtype: int
        """
        return self._http_timeout

    @http_timeout.setter
    def http_timeout(self, http_timeout):
        """
        Sets the http_timeout of this PrinceOptions.
        Set the HTTP request timeout.

        :param http_timeout: The http_timeout of this PrinceOptions.
        :type: int
        """
        self._http_timeout = http_timeout

    @property
    def insecure(self):
        """
        Gets the insecure of this PrinceOptions.
        Disable SSL verification.

        :return: The insecure of this PrinceOptions.
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """
        Sets the insecure of this PrinceOptions.
        Disable SSL verification.

        :param insecure: The insecure of this PrinceOptions.
        :type: bool
        """
        self._insecure = insecure

    @property
    def media(self):
        """
        Gets the media of this PrinceOptions.
        Specify the CSS media type. Defaults to \"print\" but you may want to use \"screen\" for web styles.

        :return: The media of this PrinceOptions.
        :rtype: str
        """
        return self._media

    @media.setter
    def media(self, media):
        """
        Sets the media of this PrinceOptions.
        Specify the CSS media type. Defaults to \"print\" but you may want to use \"screen\" for web styles.

        :param media: The media of this PrinceOptions.
        :type: str
        """
        self._media = media

    @property
    def no_author_style(self):
        """
        Gets the no_author_style of this PrinceOptions.
        Ignore author stylesheets.

        :return: The no_author_style of this PrinceOptions.
        :rtype: bool
        """
        return self._no_author_style

    @no_author_style.setter
    def no_author_style(self, no_author_style):
        """
        Sets the no_author_style of this PrinceOptions.
        Ignore author stylesheets.

        :param no_author_style: The no_author_style of this PrinceOptions.
        :type: bool
        """
        self._no_author_style = no_author_style

    @property
    def no_default_style(self):
        """
        Gets the no_default_style of this PrinceOptions.
        Ignore default stylesheets.

        :return: The no_default_style of this PrinceOptions.
        :rtype: bool
        """
        return self._no_default_style

    @no_default_style.setter
    def no_default_style(self, no_default_style):
        """
        Sets the no_default_style of this PrinceOptions.
        Ignore default stylesheets.

        :param no_default_style: The no_default_style of this PrinceOptions.
        :type: bool
        """
        self._no_default_style = no_default_style

    @property
    def no_embed_fonts(self):
        """
        Gets the no_embed_fonts of this PrinceOptions.
        Disable font embedding in PDFs.

        :return: The no_embed_fonts of this PrinceOptions.
        :rtype: bool
        """
        return self._no_embed_fonts

    @no_embed_fonts.setter
    def no_embed_fonts(self, no_embed_fonts):
        """
        Sets the no_embed_fonts of this PrinceOptions.
        Disable font embedding in PDFs.

        :param no_embed_fonts: The no_embed_fonts of this PrinceOptions.
        :type: bool
        """
        self._no_embed_fonts = no_embed_fonts

    @property
    def no_subset_fonts(self):
        """
        Gets the no_subset_fonts of this PrinceOptions.
        Disable font subsetting in PDFs.

        :return: The no_subset_fonts of this PrinceOptions.
        :rtype: bool
        """
        return self._no_subset_fonts

    @no_subset_fonts.setter
    def no_subset_fonts(self, no_subset_fonts):
        """
        Sets the no_subset_fonts of this PrinceOptions.
        Disable font subsetting in PDFs.

        :param no_subset_fonts: The no_subset_fonts of this PrinceOptions.
        :type: bool
        """
        self._no_subset_fonts = no_subset_fonts

    @property
    def no_compress(self):
        """
        Gets the no_compress of this PrinceOptions.
        Disable PDF compression.

        :return: The no_compress of this PrinceOptions.
        :rtype: bool
        """
        return self._no_compress

    @no_compress.setter
    def no_compress(self, no_compress):
        """
        Sets the no_compress of this PrinceOptions.
        Disable PDF compression.

        :param no_compress: The no_compress of this PrinceOptions.
        :type: bool
        """
        self._no_compress = no_compress

    @property
    def encrypt(self):
        """
        Gets the encrypt of this PrinceOptions.
        Encrypt PDF output.

        :return: The encrypt of this PrinceOptions.
        :rtype: bool
        """
        return self._encrypt

    @encrypt.setter
    def encrypt(self, encrypt):
        """
        Sets the encrypt of this PrinceOptions.
        Encrypt PDF output.

        :param encrypt: The encrypt of this PrinceOptions.
        :type: bool
        """
        self._encrypt = encrypt

    @property
    def key_bits(self):
        """
        Gets the key_bits of this PrinceOptions.
        Set encryption key size.

        :return: The key_bits of this PrinceOptions.
        :rtype: int
        """
        return self._key_bits

    @key_bits.setter
    def key_bits(self, key_bits):
        """
        Sets the key_bits of this PrinceOptions.
        Set encryption key size.

        :param key_bits: The key_bits of this PrinceOptions.
        :type: int
        """
        self._key_bits = key_bits

    @property
    def user_password(self):
        """
        Gets the user_password of this PrinceOptions.
        Set the PDF user password.

        :return: The user_password of this PrinceOptions.
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """
        Sets the user_password of this PrinceOptions.
        Set the PDF user password.

        :param user_password: The user_password of this PrinceOptions.
        :type: str
        """
        self._user_password = user_password

    @property
    def owner_password(self):
        """
        Gets the owner_password of this PrinceOptions.
        Set the PDF owner password.

        :return: The owner_password of this PrinceOptions.
        :rtype: str
        """
        return self._owner_password

    @owner_password.setter
    def owner_password(self, owner_password):
        """
        Sets the owner_password of this PrinceOptions.
        Set the PDF owner password.

        :param owner_password: The owner_password of this PrinceOptions.
        :type: str
        """
        self._owner_password = owner_password

    @property
    def disallow_print(self):
        """
        Gets the disallow_print of this PrinceOptions.
        Disallow printing of this PDF.

        :return: The disallow_print of this PrinceOptions.
        :rtype: bool
        """
        return self._disallow_print

    @disallow_print.setter
    def disallow_print(self, disallow_print):
        """
        Sets the disallow_print of this PrinceOptions.
        Disallow printing of this PDF.

        :param disallow_print: The disallow_print of this PrinceOptions.
        :type: bool
        """
        self._disallow_print = disallow_print

    @property
    def disallow_copy(self):
        """
        Gets the disallow_copy of this PrinceOptions.
        Disallow copying of this PDF.

        :return: The disallow_copy of this PrinceOptions.
        :rtype: bool
        """
        return self._disallow_copy

    @disallow_copy.setter
    def disallow_copy(self, disallow_copy):
        """
        Sets the disallow_copy of this PrinceOptions.
        Disallow copying of this PDF.

        :param disallow_copy: The disallow_copy of this PrinceOptions.
        :type: bool
        """
        self._disallow_copy = disallow_copy

    @property
    def disallow_annotate(self):
        """
        Gets the disallow_annotate of this PrinceOptions.
        Disallow annotation of this PDF.

        :return: The disallow_annotate of this PrinceOptions.
        :rtype: bool
        """
        return self._disallow_annotate

    @disallow_annotate.setter
    def disallow_annotate(self, disallow_annotate):
        """
        Sets the disallow_annotate of this PrinceOptions.
        Disallow annotation of this PDF.

        :param disallow_annotate: The disallow_annotate of this PrinceOptions.
        :type: bool
        """
        self._disallow_annotate = disallow_annotate

    @property
    def disallow_modify(self):
        """
        Gets the disallow_modify of this PrinceOptions.
        Disallow modification of this PDF.

        :return: The disallow_modify of this PrinceOptions.
        :rtype: bool
        """
        return self._disallow_modify

    @disallow_modify.setter
    def disallow_modify(self, disallow_modify):
        """
        Sets the disallow_modify of this PrinceOptions.
        Disallow modification of this PDF.

        :param disallow_modify: The disallow_modify of this PrinceOptions.
        :type: bool
        """
        self._disallow_modify = disallow_modify

    @property
    def input(self):
        """
        Gets the input of this PrinceOptions.
        Specify the input format.

        :return: The input of this PrinceOptions.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this PrinceOptions.
        Specify the input format.

        :param input: The input of this PrinceOptions.
        :type: str
        """
        allowed_values = ["html", "xml", "auto"]
        if input not in allowed_values:
            raise ValueError(
                "Invalid value for `input`, must be one of {0}"
                .format(allowed_values)
            )
        self._input = input

    @property
    def version(self):
        """
        Gets the version of this PrinceOptions.
        Specify a specific verison of PrinceXML to use.

        :return: The version of this PrinceOptions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PrinceOptions.
        Specify a specific verison of PrinceXML to use.

        :param version: The version of this PrinceOptions.
        :type: str
        """
        self._version = version

    @property
    def javascript(self):
        """
        Gets the javascript of this PrinceOptions.
        Enable PrinceXML JavaScript. DocRaptor JavaScript parsing is also available elsewhere.

        :return: The javascript of this PrinceOptions.
        :rtype: bool
        """
        return self._javascript

    @javascript.setter
    def javascript(self, javascript):
        """
        Sets the javascript of this PrinceOptions.
        Enable PrinceXML JavaScript. DocRaptor JavaScript parsing is also available elsewhere.

        :param javascript: The javascript of this PrinceOptions.
        :type: bool
        """
        self._javascript = javascript

    @property
    def css_dpi(self):
        """
        Gets the css_dpi of this PrinceOptions.
        Set the DPI when rendering CSS. Defaults to 96 but can be set with Prince 9.0 and up.

        :return: The css_dpi of this PrinceOptions.
        :rtype: int
        """
        return self._css_dpi

    @css_dpi.setter
    def css_dpi(self, css_dpi):
        """
        Sets the css_dpi of this PrinceOptions.
        Set the DPI when rendering CSS. Defaults to 96 but can be set with Prince 9.0 and up.

        :param css_dpi: The css_dpi of this PrinceOptions.
        :type: int
        """
        self._css_dpi = css_dpi

    @property
    def profile(self):
        """
        Gets the profile of this PrinceOptions.
        In Prince 9.0 and up you can set the PDF profile.

        :return: The profile of this PrinceOptions.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this PrinceOptions.
        In Prince 9.0 and up you can set the PDF profile.

        :param profile: The profile of this PrinceOptions.
        :type: str
        """
        self._profile = profile

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

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

