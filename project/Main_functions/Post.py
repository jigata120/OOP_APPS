from typing import List
import time
from project.Main_functions.Data_validator import Validator
from project.Main_functions.Profile import Profile


class Post(Validator):
    def __init__(self, picture, text: str, user: Profile):
        self.picture = picture
        self.text = text
        self.user = user
        self.likes_list: List[Profile] = []
        self.comments_list = []

    @property
    def likes_count(self):
        return len(self.likes_list)

    @property
    def comment_count(self):
        return len(self.comments_list)

    @classmethod
    def create(cls, picture, text: str, user: Profile):
        post = cls(picture, text, user)
        user.posts.append(post)
        return post

    def like_post(self, user: Profile):
        if user in self.likes_list:
            print("Unliked")
            return self.likes_list.remove(user)
        print("Liked")
        return self.likes_list.append(user)


    def comment_post(self, user, comment):
        self.comments_list.append(f"{user.username}: {comment}")


    def __repr__(self):
        return f"{self.user.username.capitalize()}'s post"

    def display_likes(self):
        info = ['===============================',
                  f"Post by: {self.user.username.capitalize()}",
                  f"-------------------------------",
                  f"{self.picture}",
                  f"-------------------------------",
                  f"Text: {self.text}",
                  f"Comments: {self.comment_count}",
                  f"VVV Likes:{self.likes_count} VVV"]
        list_of_users = [f"{user.username}" for user in self.likes_list]

        return '\n'.join(info+list_of_users)

    def display_comments(self):
        info = ['===============================',
                  f"Post by: {self.user.username.capitalize()}",
                  f"-------------------------------",
                  f"{self.picture}",
                  f"-------------------------------",
                  f"Text: {self.text}",
                  f"Likes:{self.likes_count}",
                  f"VVV Comments: {self.comment_count} VVV"]
        list_of_comments = [comment for comment in self.comments_list]

        return '\n'.join(info+list_of_comments)


    def __str__(self):
        result = ['===============================',
                  f"Post by: {self.user.username.capitalize()}",
                  f"-------------------------------",
                  f"{self.picture}",
                  f"-------------------------------",
                  f"Text: {self.text}",
                  f"Likes: {self.likes_count} Comments: {self.comment_count}",
                  '===============================',
                  ]
        return '\n'.join(result)
