class Add:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def user_info(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"

add = Add("Adam_Champ", 222)
print(add.user_info())


class Naslednik(Add):
    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
    def user_info(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info2(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info3(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info4(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info5(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info6(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info7(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info8(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info9(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info10(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info11(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info12(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info13(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info14(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"
    def user_info15(self):
        return f"ID: {self.user_id}, Name: {self.user_name}"