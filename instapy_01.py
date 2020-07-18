#!/usr/bin/env python
"""Script that functionally uses the basic API for InstaPy."""

from instapy_00 import username, password
from instapy import InstaPy

def start_session():
    session = InstaPy(username="Chugthai", password="pyQV7GcQVjBsU93mFy48")

    session.login()

    session.like_by_tags(["bmw", "mercedes"], amount=5)
    session.set_dont_like(["naked", "nsfw"])

    # Next, you can tell the bot to not only like the posts but also to follow some
    # of the authors of those posts. You can do that with set_do_follow():
    session.set_do_follow(True, percentage=50)

    # You can also leave some comments on the posts. There are two things that you
    # need to do. First, enable commenting with set_do_comment():
    session.set_do_comment(True, percentage=50)

    # now let's set what comments to leave with this
    # session.set_comments()  # type: List
    session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])

    session.end()


if __name__ == "__main__":
    start_session()