from project.Main_functions.Chat import Chat
from project.Main_functions.Post import Post
from project.Main_functions.Admin_profile import AdminProfile
from project.Main_functions.Default_profile import DefaultProfile
from project.Main_functions.Data_validator import Validator
from project.Main_functions.Profile import Profile
from typing import List

user1 = DefaultProfile("user1", 21, ".com", "123a")
user2 = DefaultProfile("user2", 22, ".com", "123")
user3 = DefaultProfile("user3", 23, ".com", "123")
user4 = DefaultProfile("user4", 23, ".com", "123")
user5 = AdminProfile("user5", 25, ".com", "123")


class SocialMediaFunctionalities(Validator):
    PROFILE_TYPES = {
        "default": DefaultProfile,
        "admin": AdminProfile
    }

    def __init__(self):
        self.users: List[Profile] = [user1, user2, user3, user4, user5]

    def login(self):
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
        required_data = ["type", "username", "age", "email", "password"]
        type_of_profile = Validator.get_validated_data(
            'type of profile (default / admin)', data_type=str, required_data=required_data,
            required_choise=self.PROFILE_TYPES.keys())

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
        print("You have no admin permissions to crate a chat.")

    def main_content(self):
        all_content = [user]
    def personal_content(self):
        pass
    def recomended_content(self):
sm = SocialMediaFunctionalities()

print(sm.create_post(user1))
