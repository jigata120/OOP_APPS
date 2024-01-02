from project.Main_functions.Data_validator import Validator
from project.Main_functions.Profile import Profile
from project.Main_functions.Admin_profile import AdminProfile
from project.Main_functions.Default_profile import DefaultProfile
from project.Main_functions.Chat import Chat
from project.Main_functions.Post import Post
from unittest import TestCase, main


class TestProfiles(TestCase):

    def setUp(self):
        self.user1 = DefaultProfile('JohnDoe', 25, 'john@example.com', 'secure_password')
        self.user2 = AdminProfile('kony', 20, 'kony@example.com', 'secure_password2')
        self.user3 = DefaultProfile('Lucy', 30, 'lucy@example.com', 'secure_password3')

    def test_initial_DefaultProfile(self):
        assert self.user1.username == 'JohnDoe'
        assert self.user1.age == 25
        assert self.user1.email == 'john@example.com'
        assert self.user1.password == 'secure_password'
        assert self.user1.is_admin == False

    def test_profile_quick_view(self):
        print(self.user1.quick_view())
    def test_profile_profile_view(self):
        print(self.user1.profile_view())

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
        result = chat.add_message(self.user1, 'Hello!')
        assert result == 'JohnDoe: Hello!'
        chat.add_message(self.user2, 'Hi!')
        assert chat.messages == ['JohnDoe: Hello!', 'kony: Hi!']
        result = chat.add_member(self.user3)
        assert result == 'Successfully added member(Lucy) to the chat.'
        assert chat.members == [self.user1, self.user2, self.user3]
        print(chat)

    def test_validator(self):
        result = Validator.is_valid_type(13, int)
        assert result
        result = Validator.is_valid_type('test_str', int)
        assert not result
        result = Validator.is_valid_type('test_str', str)
        assert result
        result = Validator.is_valid_type(12, str)
        assert not result
        result = Validator.is_valid_type(['test_str'], list)
        assert result
        result = Validator.is_min_length(['test_str'], 1)
        assert result
        result = Validator.is_min_length(['test_str'], 2)
        assert not result
        result = Validator.is_min_length('test_str', 8)
        assert result
        result = Validator.is_min_length('test_str', 9)
        assert not result
        result = Validator.is_min_length(12, 12)
        assert result
        result = Validator.is_min_length(12, 13)
        assert not result
        result = Validator.is_max_length('test_str', 8)
        assert result
        result = Validator.is_max_length('test_str', 7)
        assert not result
        result = Validator.is_max_length(12, 12)
        assert result
        result = Validator.is_max_length(12, 11)
        assert not result
        result = Validator.is_max_length(['test_str'], 1)
        assert result
        result = Validator.is_max_length(['test_str', 'test_int'], 1)
        assert not result


if __name__ == '__main__':
    main()
