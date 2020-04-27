# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
instagram_username = ''
instagram_password = ''

# change or add comments from this list, the more you add the less suspicious they become.
comments = ['Nice shot! @{}',
            'I love your profile! @{}',
            'Your feed is an inspiration :thumbsup:',
            'Just incredible :open_mouth:',
            'What camera did you use @{}?',
            'Love your posts @{}',
            'Looks awesome @{}',
            'Getting inspired by you @{}',
            ':raised_hands: Yes!',
            'I can feel your passion @{} :muscle:']

# initiate an InstaPy session
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=instagram_username,
                  password=instagram_password,
                  headless_browser=False)

# launches InstaPy
with smart_run(session):
    """ Activity flow """
    # people who you do not want bot to have interaction with
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # bot searches through posts with these tags
    session.like_by_tags(["natgeo", "soccer"], amount=10)

    # if enabled = true, percentage dictates how often bot comments on posts it is viewing
    session.set_do_comment(enabled=True, percentage=35)

    # uses list of comments define above as comments
    session.set_comments(comments)

    # checks posts under topic defined and engages in them in the way which is defined
    session.join_pods(topic='sports', engagement_mode='no_comments')
