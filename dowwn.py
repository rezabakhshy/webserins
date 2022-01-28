from instapy import InstaPy
session=InstaPy(username="rbz8181",password="reza13811")
session.login()
session.set_do_comment(enabled=True,percentage=100)
session.set_comments(["naice","good","help"])
session.set_do_follow(enabled=True,percentage=100)
session.like_by_users(["bramastavrl","vindiesel"],amount=10)
session.like_by_tags(["siasefid","mehrab"])

