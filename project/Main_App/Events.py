from project.Main_functions.Chat import Chat
from project.Main_functions.Post import Post
from project.Main_functions.Admin_profile import AdminProfile
from project.Main_functions.Default_profile import DefaultProfile
from project.Main_functions.Data_validator import Validator
from project.Main_functions.Profile import Profile
from typing import List


class SocialMediaFunctionalities(Validator):
    PROFILE_TYPES = {
        "default": DefaultProfile,
        "admin": AdminProfile
    }

    def __init__(self):
        self.users: List[Profile] = [user1, user2, user3, user4, user5]

    def login(self):
        print("LOGIN")
        username = Validator.get_validated_data(
            'username', data_type=str, required_data=["username"])
        password = Validator.get_validated_data(
            'password', data_type=str, required_data=["password"])
        logged_user = next((user for user in self.users if user.username == username
                            and user.password == password), None)
        if logged_user:
            return logged_user
        print("Invalid username or password")
        return self.register()

    def register(self):
        print("REGISTER")
        required_data = ["type", "username", "age", "email", "password"]
        type_of_profile = Validator.get_validated_data(
            'type of profile (default / admin)', data_type=str, required_data=required_data,
            required_choice=self.PROFILE_TYPES.keys())

        user = self.PROFILE_TYPES[type_of_profile](
            Validator.get_validated_data(
                'username', data_type=str, required_data=required_data, data_min_length=2, data_max_length=20),
            Validator.get_validated_data(
                'age', data_type=int, required_data=required_data, data_min_length=18, data_max_length=120),
            Validator.get_validated_data(
                'email', data_type=str, required_data=required_data, data_min_length=5, data_max_length=35),
            Validator.get_validated_data(
                'password', data_type=str, required_data=required_data, data_min_length=4, data_max_length=35),
            Validator.get_validated_data('gender', data_type=str),
            Validator.get_validated_data('bio', data_type=str),
            Validator.get_validated_data('contact_information', data_type=str),
            Validator.get_validated_data('location', data_type=str),
            Validator.get_validated_data('education', data_type=str),
            Validator.get_validated_data('hobbies', data_type=str)
        )
        return user

    def find_user(self, user_name):
        found_user = next((found_user for found_user in self.users if user_name == found_user.username), None)
        if not found_user:
            #    raise ValueError("This user do not exist.")
            username = Validator.get_validated_data('valid searchable username', data_type=str)
            return self.find_user(username)
        return found_user

    def find_post(self, post):
        found_post = next((found_post for found_post in self.all_posts() if post == found_post.text), None)
        if not found_post:
            #    raise ValueError("This post do not exist.")
            post = Validator.get_validated_data('valid searchable post text', data_type=str)
            return self.find_post(post)
        return found_post

    def logout(self):
        pass

    def create_post(self, user: Profile):
        required_data = ["picture", "text", ]
        post = Post.create(
            Validator.get_validated_data('picture', data_type=str, required_data=required_data),
            Validator.get_validated_data('text', data_type=str, required_data=required_data),
            user=user
        )
        print(f"Post was successfully created by {user.username.capitalize()}.")
        return post

    def create_chat(self, user: Profile, *args: Profile):
        if user.__class__.__name__ == self.PROFILE_TYPES['admin']:
            chat = Chat.create(user, args)
            return chat
        return "You have no admin permissions to crate a chat."

    def non_private(self):
        return [user for user in self.users if not user.is_profile_private]

    def all_posts(self, user=None):
        posts = []
        if not user:
            for user in self.non_private():
                posts += user.posts
        else:
            for user in user._followers_list:
                posts += user.posts
        return posts

    def main_content(self):
        sorted_users = Validator.sort_by_parameter(self.users, 'followers', 'username', reverse=True)
        sorted_posts = Validator.sort_by_parameter(self.all_posts(), 'likes_count', 'comments_count', reverse=True)
        return sorted_posts

    def personal_posts(self, user):
        sorted_posts = Validator.sort_by_parameter(self.all_posts(user=user), 'likes_count', 'comments_count',
                                                   reverse=True)
        return sorted_posts

    def personal_new_users(self, user):
        new_users = list(filter(lambda x: x not in user._followers_list, self.users))
        sorted_new_users = Validator.sort_by_parameter(new_users, 'followers', 'username', reverse=True)
        return sorted_new_users

    def personal_content(self, user):
        content_types = {
            "posts": [self.personal_posts, "Follow people to see more posts"],
            "new_users": [self.personal_new_users, "There are no other users"]
        }
        content_choice = Validator.get_validated_data('content type( posts / new_users)', data_type=str,
                                                      required_choice=content_types.keys())
        if content_choice:
            content = content_types[content_choice][0](user)
            list_of_content = [str(post) for post in content]
            return '\n+++++++++++++++++++++++++++++++\n'.join(list_of_content)
        return content_types[content_choice][1]

    def recommended_content(self):
        pass


    def options(self, events):
        events_str = 'event\n' + '\n'.join([f"{position + 1}: {event}" for position, event in enumerate(events.keys())])
        return Validator.get_validated_data(events_str, data_type=str, required_choice=events.keys())


user1 = DefaultProfile("user1", 21, ".com", "123a")
user2 = DefaultProfile("user2", 22, ".com", "123")
user3 = DefaultProfile("user3", 23, ".com", "123")
user4 = DefaultProfile("user4", 23, ".com", "123")
user5 = AdminProfile("user5", 25, ".com", "123")
sm = SocialMediaFunctionalities()

user1 = DefaultProfile("user1", 21, ".com", "123a")
user2 = DefaultProfile("user2", 22, ".com", "123")
user3 = DefaultProfile("user3", 23, ".com", "123")
user4 = DefaultProfile("user4", 23, ".com", "123")
user5 = AdminProfile("user5", 25, ".com", "123")
post1 = Post.create(':0', 'post1', user1)
post2 = Post.create(':)', 'post2', user1)
post3 = Post.create(':(', 'post3', user1)
post4 = Post.create(':0{', 'post4', user2)
post5 = Post.create(':>', 'post5', user2)
post6 = Post.create(':?', 'post6', user3)
post7 = Post.create(':/', 'post7', user4)
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
post7.comment_post(user1, 'nice!')

user1._followers_list = [user2, user3]
