from login import login, LoginInsta
from target import Target
from usuals import UsualFunctions


def run_bot(user, password, option):
    if option == 1:
        target = UsualFunctions().get_target()
        bot = login(user, password)
        bot.target = target
        bot.like_all()
    elif option == 2:
        target = UsualFunctions().get_target()
        num_posts = UsualFunctions().get_num_posts_to_like()
        bot = login(user, password)
        bot.target = target
        bot.like_some(num_posts)
    else:
        link = UsualFunctions().get_link()
        bot = login(user, password)
        bot.like_one(link)


# get option
option = UsualFunctions().show_options()

# get user credentials
user, password = UsualFunctions().get_cred()

# run the bot
run_bot(user, password, option)
