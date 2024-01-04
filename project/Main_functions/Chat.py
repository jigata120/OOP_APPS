from project.Main_functions.Data_validator import Validator
from project.Main_functions.Profile import Profile
from typing import List


class Chat(Validator):
    def __init__(self, *args, **kwargs):
        self.messages = []
        self.members: List[Profile] = list(args)

    def add_message(self, member, message):
        if member in self.members:
            full_message = f"{member.username}: {message}"
            self.messages.append(full_message)
            return full_message
        raise KeyError(f"{member.username} is not a member of the chat")

    def add_member(self, member: Profile):
        self.members.append(member)
        return f'Successfully added member({member.username}) to the chat.'

    @classmethod
    def create(cls, user, *args):
        chat = cls([user] + list(args))
        user.chats.append(chat)
        return chat

    def __str__(self):
        return f"{self.members}"+'\n----------------\n'.join(self.messages)
