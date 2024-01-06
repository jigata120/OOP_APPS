from project.Main_App.Events import SocialMediaFunctionalities, user1, user5, user2, user3, user4


class SocialMedia(SocialMediaFunctionalities):

    def __init__(self):
        super().__init__()
        self.user = user5
        # super().login()

        self.main_events = {
            "content": self.content,
            "chats": self.chats,
            "create_post": self.create_post,
            "create_chat": self.create_chat,
            "search_user": self.search_name,
            "search_post": self.search_post,
            "profile": self.profile_options,
            "logout": self.logout
        }
        self.main_options()

    def logout(self):
        self.user = super().login()

    def content(self):
        content = super().personal_content(self.user)
        return content

    def chats(self):
        return self.user.chats_view()

    def create_post(self):
        post = super().create_post(self.user)
        return post

    def create_chat(self):
        chat = super().create_chat(self.user)
        return chat

    def main_options_redirect(self, *arg):
        return self.main_options()

    def search_name(self, user=None):

        if not user:
            # ask for post name
            username = input("Search by username: ")
            user = super().find_user(username)
            print(user.profile_view())

        def follow_user(_user):
            return self.user.will_follow(_user)

        def user_info(_user):
            return str(_user)

        def followers_list_view(_user):
            return _user.followers_view()

        def posts_list_view(_user):
            return _user.posts_view()

        def save_post_view(_user):
            return _user.saves_view()

        user_events = {
            "follow_user": follow_user,
            "info": user_info,
            "followers_list": followers_list_view,
            "posts_list": posts_list_view,
            "saves_list": save_post_view,
            "menu": self.main_options_redirect,
        }
        print(user_events[super().options(user_events)](user))
        return self.search_name(user)

    def search_post(self, post=None):
        if not post:
            # ask for post name
            post_text = input("Search by post text: ")
            post = super().find_post(post_text)
            print(post)

        def follow_user_by_post(_post):
            return self.user.will_follow(_post.user)

        def like_post(_post):
            _post.like_post(self.user)
            return _post.display_likes()

        def comment_post(_post):
            comment = input("Type here: ")
            _post.comment_post(self.user, comment)
            return _post.display_comments()

        def save_post(_post):
            return self.user.save_post(_post)

        post_events = {
            "follow_user": follow_user_by_post,
            "like": like_post,
            "comment": comment_post,
            "save": save_post,
            "menu": self.main_options_redirect,
        }
        print(post_events[super().options(post_events)](post))
        return self.search_post(post)

    def profile_options(self):
        profile = self.user.profile_view()
        print(profile)

        def info():
            return str(self.user)

        profile_events = {
            "info": info,
            "followers_list": self.user.followers_view,
            "posts_list": self.user.posts_view,
            "saves_list": self.user.saves_view,
            "requests_list": self.user.requests_view,
            "change_privacy": self.user.change_privacy_status,
            "menu": self.main_options_redirect()
        }
        print(profile_events[super().options(profile_events)]())
        return self.profile_options()

    def main_options(self):
        print(self.main_events[super().options(self.main_events)]())
        return self.main_options()


dm = SocialMedia()
