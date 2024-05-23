#!/usr/bin/env python3

"""Unitest for utils"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Access Nested Map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """
        Test accessing a value in a nested map with a key path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test accessing a value in a nested map with a key path.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test Get Json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://example.com/1", {"payload": False}),
    ])
    def test_get_json(self, url: str, expected: str) -> None:
        """
        Test get_json
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = expected
            self.assertEqual(get_json(url), expected)


class TestMemoize(unittest.TestCase):
    """
    Test Memoize
    """
    def test_memoize(self) -> None:
        """
        Test memoize
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()
