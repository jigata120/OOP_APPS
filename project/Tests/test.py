from project.Data_validator import Validator
from project.Profile import Profile
from project.Admin_profile import AdminProfile
from project.Default_profile import DefaultProfile
from project.Chat import Chat
from project.Post import Post
from unittest import TestCase, main


class TestProfiles(TestCase):

    def setUp(self):
        self.user1 = DefaultProfile('JohnDoe', 25, 'john@example.com', 'secure_password')
        self.user2 = AdminProfile('kony', 20, 'kony@example.com', 'secure_password2')

    def test_initial_DefaultProfile(self):
        assert self.user1.username == 'JohnDoe'
        assert self.user1.age == 25
        assert self.user1.email == 'john@example.com'
        assert self.user1.password == 'secure_password'
        assert self.user1.is_admin == False

    def test_initial_AdminProfile(self):
        assert self.user2.username == 'kony'
        assert self.user2.age == 20
        assert self.user2.email == 'kony@example.com'
        assert self.user2.password == 'secure_password2'
        assert self.user2.is_admin == True

    def test_initial_Post(self):
        post1 = Post('<3', 'Hello, world!', self.user1)

        assert post1.picture == '<3'
        assert post1.text == 'Hello, world!'
        assert post1.user == self.user1
        created_post = Post.create(' :(', 'Bye, world!', self.user2)
        expected_string = '''Post by: Kony
                            Picture:  :(
                            Text: Bye, world!
                            Likes: 0
                            Comments: 0'''

        def normalize_multiline_string(s):
            return '\n'.join(line.strip() for line in s.split('\n'))

        expected_result = normalize_multiline_string(expected_string)
        assert str(created_post) == expected_result

    def test_chat(self):
        chat = Chat(self.user1, self.user2)
        chat.add_message(self.user1, 'Hello!')
        chat.add_message(self.user2, 'Hi!')
        print(chat.messages)
        print(chat.members[0].username)
        print(chat)


if __name__ == '__main__':
    main()
