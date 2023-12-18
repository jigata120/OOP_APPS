from typing import List
import time
from project.Main_functions.Data_validator import Validator
from project.Main_functions.Profile import Profile


class Post(Validator):
    def __init__(self, picture, text: str, user: Profile):
        self.picture = picture
        self.text = text
        self.user = user
        self.likes: List[Profile] = []
        self.comments = []

    @classmethod
    def create(cls, picture, text: str, user: Profile):
        post = cls(picture, text, user)
        user.posts.append(post)
        return post

    def like_post(self, user: Profile):
        if user in self.likes:
            self.likes.remove(user)
        self.likes.append(user)

    def comment_post(self, user, comment):
        self.comments.append(f"{user}: {comment}")

    def __repr__(self):
        return f"{self.user.username.capitalize()}'s post"

    def __str__(self):
        result = ['===============================',
                  f"Post by: {self.user.username.capitalize()}",
                  f"-------------------------------",
                  f"{self.picture}",
                  f"-------------------------------",
                  f"Text: {self.text}",
                  f"Likes: {len(self.likes)} Comments: {len(self.comments)}",
                  '===============================',
                  ]
        return '\n'.join(result)
