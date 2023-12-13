from typing import List
import time
from project.Data_validator import Validator
from project.Profile import Profile


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

    def __repr__(self):
        return f"{self.user.username.capitalize()}'s post"

    def __str__(self):
        result = [f"Post by: {self.user.username.capitalize()}",
                  f"Picture: {self.picture}",
                  f"Text: {self.text}",
                  f"Likes: {self.likes}",
                  f"Comments: {self.comments}"
                  ]
        return '\n'.join(result)
