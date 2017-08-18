from copy import deepcopy
import unittest

from jsonxs import (
    jsonxs,
    ACTION_SET,
    ACTION_DEL,
    ACTION_APPEND,
    ACTION_INSERT,
    ACTION_MKDICT,
    ACTION_MKLIST,
)


example_d = {
  'feed': {
    'id': 'my_feed',
    'url': 'http://example.com/feed.rss',
    'tags': ['devel', 'example', 'python'],
    'short.desc': 'A feed',
    'list': [
      {
        'uuid': 'e9b48a2'
      }
    ]
  }
}


class TestJsonxsGetAction(unittest.TestCase):

    def setUp(self):
        self.d = deepcopy(example_d)

    def test_get_path(self):
        """Get the value for a path expression"""

        self.assertEqual(
            jsonxs(self.d, 'feed.tags[-1]'),
            'python'
        )

    def test_get_path_with_special_chars(self):
        """Access paths with special chars in them"""

        self.assertEqual(
            jsonxs(self.d, 'feed.short\.desc'),
            'A feed'
        )

    def test_get_default_for_missing_path(self):
        """Return default value if path not found"""

        self.assertEqual(
            jsonxs(self.d, 'feed.long\.desc', default='N/A'),
            'N/A'
        )


class TestJsonxsSetAction(unittest.TestCase):

    def setUp(self):
        self.d = deepcopy(example_d)

    def test_set_value_of_path(self):
        """Set the value for a path expression"""
        jsonxs(self.d, 'feed.id', ACTION_SET, 'your_feed')
        self.assertEqual(
            self.d['feed']['id'],
            'your_feed'
        )

    def test_set_replaces_value_of_path(self):
        """Replace a value in a list"""

        jsonxs(self.d, 'feed.tags[-1]', ACTION_SET, 'javascript')
        self.assertEqual(
            self.d['feed']['tags'],
            ['devel', 'example', 'javascript']
        )

    def test_set_replaces_value_of_path(self):
        """Create a new key in a dict"""

        jsonxs(self.d, 'feed.author', ACTION_SET, 'Ferry Boender')
        self.assertEqual(
            self.d['feed']['author'],
            'Ferry Boender'
        )


class TestJsonxsDeleteAction(unittest.TestCase):

    def setUp(self):
        self.d = deepcopy(example_d)

    def test_deletes_value_from_path(self):
        """Delete a value from a list"""

        jsonxs(self.d, 'feed.tags[0]', ACTION_DEL)
        self.assertEqual(
            self.d['feed']['tags'],
            ['example', 'python']
        )

    def test_deletes_key_value_pair(self):
        """Delete a key/value pair from a dictionary"""

        jsonxs(self.d, 'feed.url', ACTION_DEL)
        self.assertFalse('url' in self.d['feed'])


class TestJsonxsAppendAction(unittest.TestCase):

    def setUp(self):
        self.d = deepcopy(example_d)

    def test_appends_value_to_list(self):
        """Append a value to a list"""

        jsonxs(self.d, 'feed.tags', ACTION_APPEND, 'programming')
        self.assertEqual(
            self.d['feed']['tags'],
            ['devel', 'example', 'python', 'programming']
        )


class TestJsonxsInsertAction(unittest.TestCase):

    def setUp(self):
        self.d = deepcopy(example_d)

    def test_insert_value_to_list(self):
        """Insert a value to a list"""

        jsonxs(self.d, 'feed.tags[1]', ACTION_INSERT, 'tech')
        self.assertEqual(
            self.d['feed']['tags'],
            ['devel', 'tech', 'example', 'python'],
        )


class TestJsonxsMkDictAction(unittest.TestCase):

    def setUp(self):
        self.d = deepcopy(example_d)

    def test_create_a_dict_value(self):
        """Create a dict value"""
        jsonxs(self.d, 'feed.details', ACTION_MKDICT)
        self.assertTrue(self.d['feed']['details'] == {})


class TestJsonxsMkDictAction(unittest.TestCase):

    def setUp(self):
        self.d = deepcopy(example_d)

    def test_create_a_list_value(self):
        """Create a list value"""
        jsonxs(self.d, 'feed.users', ACTION_MKLIST)
        self.assertTrue(self.d['feed']['users'] == [])
