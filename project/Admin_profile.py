from project.Profile import Profile


class AdminProfile(Profile):
    def __init__(self, username, age, gender, email, password, bio, contact_information, location, education, hobbies):
        super().__init__(username, age, gender, email, password, bio, contact_information, location, education, hobbies,
                         False, False, False, False)

    def profile_permissions(self):
        pass