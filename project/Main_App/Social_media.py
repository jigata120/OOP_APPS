from project.Main_App.Events import SocialMediaFunctionalities


class SocialMedia(SocialMediaFunctionalities):

    def __init__(self):
        super().__init__()
        self.user = super().login()

    def login(self):
        pass
