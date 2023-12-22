from project.Main_App.Social_media import SocialMedia
from project.Main_App.Events import SocialMediaFunctionalities
from unittest import TestCase, main
from project.Main_functions.Chat import Chat
from project.Main_functions.Post import Post
from project.Main_functions.Admin_profile import AdminProfile
from project.Main_functions.Default_profile import DefaultProfile
from project.Main_functions.Data_validator import Validator
from project.Main_functions.Profile import Profile
from typing import List


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
    def test_content(self):
        user1 = DefaultProfile("user1", 21, ".com", "123a")
        user2 = DefaultProfile("user2", 22, ".com", "123")
        user3 = DefaultProfile("user3", 23, ".com", "123")
        user4 = DefaultProfile("user4", 23, ".com", "123")
        user5 = AdminProfile("user5", 25, ".com", "123")
        post1 = Post.create(':0', 'post1', user1)
        post2 = Post.create(':)', 'post1', user1)
        post3 = Post.create(':(', 'post1', user1)
        post4 = Post.create(':0{','post1',  user2)
        post5 = Post.create(':>', 'post1', user2)
        post6 = Post.create(':?', 'post1', user3)
        post7 = Post.create(':/', 'post1', user4)
        post1.like_post(user1)
        post1.like_post(user2)
        post1.like_post(user3)
        post1.like_post(user4)
        post2.like_post(user1)
        post3.like_post(user1)
        post4.like_post(user2)
        post5.like_post(user3)
        post6.like_post(user4)
        post7.like_post(user5)
        post7.comment_post(user1,'nice!')
        print([str(post) for post in self.sm.main_content()])
if __name__ == '__main__':
    main()
