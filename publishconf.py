#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
from pelicanconf import *
sys.path.append(os.curdir)

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "liungoahc"
GOOGLE_ANALYTICS = "UA-54228593-1"
