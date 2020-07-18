#!/usr/bin/env python
"""
==============================
Additional Features in InstaPy
==============================

InstaPy is a sizable project that has a lot of
`thoroughly documented <https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md>`_
features. The good news is that if you’re feeling comfortable with the
features you used above, then the rest should feel pretty similar. This
section will outline some of the more useful features of InstaPy.

Headless Browser
================
This feature allows you to run your bot without the GUI of the browser. This
is super useful if you want to deploy your bot to a server where you may not
have or need the graphical interface. It’s also less CPU intensive, so it
improves performance. You can use it like so:

Quota Supervisor Intro
======================
You can’t scrape Instagram all day, every day. The service will quickly
notice that you’re running a bot and will ban some of its actions. That’s why
it’s a good idea to set quotas on some of your bot’s actions.

Using AI to Analyze Posts
=========================
Earlier you saw how to ignore posts that contain inappropriate words in their
descriptions. What if the description is good but the image itself is
inappropriate? You can integrate your InstaPy bot with ClarifAI, which offers
image and video recognition services:
Now your bot won’t like or comment on any image that ClarifAI considers NSFW.
You get 5,000 free API-calls per month.

Relationship Bounds
===================
It’s often a waste of time to interact with posts by people who have a lot of
followers. In such cases, it’s a good idea to set some relationship bounds so
that your bot doesn’t waste your precious computing resources:
With this, your bot won’t interact with posts by users who have more than
8,500 followers.

"""
from instapy_00 import username, password
from instapy import InstaPy


def extras():
    session = InstaPy(username="Chugthai",
                      password="pyQV7GcQVjBsU93mFy48", headless_browser=True)

    session.set_quota_supervisor(
        enabled=True, peak_comments_daily=240, peak_comments_hourly=21
    )

    session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
    session.clarifai_check_img_for(['nsfw'])

    session.set_relationship_bounds(enabled=True, max_followers=8500)


if __name__ == "__main__":
    extras()
