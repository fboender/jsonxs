JSONxs
======

JSONxs is a Python library that uses a path expression string to get and set
values in JSON and Python datastructures. It's slightly similar to JSONPath,
but supports only simpler expressions and allows modifications.

Examples
--------

Given the folowing datastructure:

    d = {
      'feed': {
        'id': 'my_feed',
        'url': 'http://example.com/feed.rss',
        'tags': ['devel', 'example', 'python']
      }
    }

We can get, set and delete values from the stucture.

    jsonxs(d, 'feed.id')                                  # Get the 'id' field: 'my_feed'
    jsonxs(d, 'feed.tags')                                # Get the list of tags.
    jsonxs(d, 'feed.tags[-1]')                            # Get the last item in the 'tags' list: 'python'
    jsonxs(d, 'feed.id', ACTION_SET, 'your_feed')         # Set feed id to 'your_feed'
    jsonxs(d, 'feed.tags[-1]', ACTION_SET, 'javascript')  # Replace 'python' with 'javascript'
    jsonxs(d, 'feed.tags[0]', ACTION_DEL)                 # Delete the first tag
    jsonxs(d, 'feed.url', ACTION_DEL)                     # Delete the 'url' key from a dict
    jsonxs(d, 'feed.tags', ACTION_APPEND, 'programming')  # Append 'programming' to tags
    jsonxs(d, 'feed.author', ACTION_SET, 'Ferry Boender') # Create new key/string value in dict 
    jsonxs(d, 'feed.details', ACTION_MKDICT)              # Create new key/dict value in dict
    jsonxs(d, 'feed.details', ACTION_MKLIST)              # Create new key/list value in dict

Installation
------------

To install:

    pip install jsonxs

License
-------

JSONxs is licensed under the MIT license:

Copyright (c) 2015 Ferry Boender (ferry.boender@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
