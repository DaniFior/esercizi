class User:
    def __init__(self, first_name, last_name, email, telephone, login_attempts=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telephone = telephone
        self.login_attempts = login_attempts

class Privileges:
    def __init__(self, privileges=None) -> None:
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def get_privileges(self):
        return self.privileges

    def set_privileges(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin2(User):
    def __init__(self, first_name, last_name, email, telephone, privileges=None, login_attempts=0) -> None:
        super().__init__(first_name, last_name, email, telephone, login_attempts)
        if privileges is None:
            privileges = []
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()
