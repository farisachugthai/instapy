#!/usr/bin/env python

# Well I feel like a fucking moron
from instapy_00 import username, password
from instapy import InstaPy

session = InstaPy(username="Chugthai", password="pyQV7GcQVjBsU93mFy48")

session.login()

session.like_by_tags(["bmw", "mercedes"], amount=5)
