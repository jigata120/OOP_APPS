from typing import List
from project.Data_validator import Validator
from project.Profile import Profile
from typing import List


class Chat(Validator):
    def __init__(self, *args, **kwargs):
        self.messages = []
        self.members: List[Profile] = args

    def add_message(self, member, message):
        if member in self.members:
            full_message = f"{member.username}: {message}"
            self.messages.append(full_message)
        raise KeyError(f"{member.username} is not a member of the chat")

    def add_member(self, member: Profile):
        self.members.append(member)

    def __str__(self):
        return '\n'.join(self.messages)
