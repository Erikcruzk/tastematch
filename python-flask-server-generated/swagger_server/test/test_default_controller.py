# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.recipe import Recipe  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_getrecipe_get(self):
        """Test case for getrecipe_get

        Gets new recipe for user with last swipe
        """
        query_string = [('username', 'username_example'),
                        ('recipe_id', 'recipe_id_example'),
                        ('recipe_like', 'recipe_like_example')]
        response = self.client.open(
            '/getrecipe',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
