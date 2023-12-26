from project.Main_App.Events import SocialMediaFunctionalities


class SocialMedia(SocialMediaFunctionalities):

    def __init__(self):
        super().__init__()
        self.user = super().login()
        self.main_events = {
            "content": self.content,
            "create post": self.create_post,
            "create chat": self.create_chat,
            "search user": self.search_name,
            "search post": self.search_post,
            "logout": self.logout
        }
        self.main_options()

    def logout(self):
        self.user = super().login()

    def create_post(self):
        post = super().create_post(self.user)
        return post

    def create_chat(self, *args):
        chat = super().create_chat(self.user, *args)
        return chat

    def content(self):
        content = super().personal_content(self.user)
        return str(content)

    def search_name(self):
        # ask for username
        username = input("Search by username: ")
        user = super().find_user(username)

    def search_post(self):
        # ask for post name
        post_text = input("Search by post text: ")
        user = super().find_user(post_text)

    def main_options(self):
        print(self.main_events[super().options(self.main_events)]())
        return self.main_options()

dm = SocialMedia()
