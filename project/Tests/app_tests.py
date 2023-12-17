from project.Main_App.Social_media import SocialMedia
from project.Main_App.Events import SocialMediaFunctionalities
from unittest import TestCase, main


class TestSocialMediaFunctionalities(TestCase):
    def setUp(self):
        self.sm = SocialMediaFunctionalities()

    def test_social_media_func(self):
        self.assertIsNotNone(SocialMedia())

    def test_login(self):
        # successful
        pass

    def test_register(self):
        # successful
        pass

    def test_logout(self):
        # successful
        pass

    def test_post(self):
        # successful
        pass


if __name__ == '__main__':
    main()
