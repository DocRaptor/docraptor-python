# coding: utf-8

"""
    DocRaptor

    A native client library for the DocRaptor HTML to PDF/XLS service.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import docraptor
from docraptor.models.async_doc import AsyncDoc  # noqa: E501
from docraptor.rest import ApiException

class TestAsyncDoc(unittest.TestCase):
    """AsyncDoc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AsyncDoc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = docraptor.models.async_doc.AsyncDoc()  # noqa: E501
        if include_optional :
            return AsyncDoc(
                status_id = ''
            )
        else :
            return AsyncDoc(
        )

    def testAsyncDoc(self):
        """Test AsyncDoc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
