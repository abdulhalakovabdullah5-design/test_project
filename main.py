class Add:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def user_info(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"

add = Add("Adam_Champ", 222)
print(add.user_info())