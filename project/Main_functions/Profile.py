from abc import ABC, abstractmethod


class Profile(ABC):
    REQUIRED_DATA = {'username': str, 'age': int, 'email': str, 'password': str, }

    def __init__(self, username: str, age: int, email: str, password: str,
                 gender: str, bio: str, contact_information: str, location: str,
                 education: str, hobbies: str, is_active: bool, is_admin: bool,
                 is_staff: bool, is_profile_private: bool,
                 ):
        self.username = username
        self.age = age
        self.gender = gender
        self.email = email
        self.password = password
        self.bio = bio
        self.contact_information = contact_information
        self.location = location
        self.education = education
        self.hobbies = hobbies
        self.is_active = is_active
        self.is_admin = is_admin
        self.is_staff = is_staff
        self.is_profile_private = is_profile_private
        self.posts = []
        self.chats = []
        self.saves = []
        self._followers_list = []

    @property
    def followers(self):
        return len(self._followers_list)

    @followers.setter
    def followers(self, value):
        self._followers_list = value

    @property
    def status(self):
        return 'PRIVATE' if self.is_profile_private else 'PUBLIC'

    def change_password(self, new_password):
        self.password = new_password

    def change_email(self, new_email):
        self.email = new_email

    def change_privacy_status(self):
        self.is_profile_private = not self.is_profile_private

    def follow(self, user):
        if not user.is_profile_private:
            if user in self._followers_list:
                self._followers_list.remove(user)
                return f'You unfollowed {user.username}'
            self._followers_list.append(user)
            return f'You now Follow {user.username}'
        # sidecase private

    def save_post(self, post):
        if post in self.saves:
            self.saves.remove(post)
            return "Post removed successfully"
        self.saves.append(post)
        return "Post saved successfully"

    @abstractmethod
    def profile_permissions(self):
        pass

    def __repr__(self):
        return f"{self.username.capitalize()}'s profile"

    def quick_for_list_view(self):
        result = [f"{self.username}",
                  f"Followers: {self.followers}",
                  f"Posts: {len(self.posts)}",
                  ]
        return " ".join(result)

    def followers_view(self):
        result = [user.quick_for_list_view() for user in self._followers_list]
        return "\n".join(result)

    def posts_view(self):
        result = [str(post) for post in self.posts]
        return "\n:::::::::::::::::::::::::::::::::::".join(result)

    def saves_view(self):
        result = [str(post) for post in self.saves]
        return "\n:::::::::::::::::::::::::::::::::::".join(result)

    def own_profile_view(self):
        pass

    def profile_view(self):

        result = [f"╔══════════════════════════════════════════╗",
                  f"                  {self.status} ",
                  f"          !_-'-_| {self.username} |_-'-_!",
                  f"          followers    Posts   Saves",
                  f"             |{self.followers}|       |{len(self.posts)}|     |{len(self.saves)}|",
                  f"╚══════════════════════════════════════════╝"
                  ]
        return "\n".join(result)

    def __str__(self):
        if self.is_profile_private:
            return f"{self.username.capitalize()}'s private profile:\nSend a request to get a public profile"

        result = [f"{self.username.capitalize()}'s Profile:\n",
                  f"username: {self.username}\n",
                  f"age: {self.age}\n",
                  f"gender: {self.gender}\n" if self.gender else "",
                  f"email: {self.email}\n" if self.email else "",
                  f"bio: {self.bio}\n" if self.bio else "",
                  f"Contact information: {self.contact_information}\n" if self.contact_information else "",
                  f"Location: {self.location}\n" if self.location else "",
                  f"Education: {self.education}\n" if self.education else "",
                  f"Hobbies: {self.hobbies}\n" if self.hobbies else "",
                  f"This user is active" if self.is_active else "Not active",
                  ]
        return "".join(result)


''''
user = Profile(
    username="JohnDoe", age=25, gender="Male", email="john@example.com",
    password="secure_password", bio="A software developer", contact_information="123-456-7890",
    location="Cityville", education="Computer Science", hobbies=' ',
    is_active=True, is_admin=False, is_staff=True, is_profile_private=True
)

print(user)
'''
