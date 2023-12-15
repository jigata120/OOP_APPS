from project.Profile import Profile


class AdminProfile(Profile):
    NOT_FILLED = 'Not filed'

    def __init__(self, username, age, email, password, gender=NOT_FILLED, bio=NOT_FILLED,
                 contact_information=NOT_FILLED, location=NOT_FILLED, education=NOT_FILLED, hobbies=NOT_FILLED):
        super().__init__(username, age, email, password, gender, bio, contact_information, location, education, hobbies,
                         False, True, False, False)

    def profile_permissions(self):
        pass
