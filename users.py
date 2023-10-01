class Users:
    def __init__(self,user_name: str, user_password: str):
        self.user_name = user_name
        self.user_password = user_password

    def __str__(self):
        return f"{self.user_name} {self.user_password}"

