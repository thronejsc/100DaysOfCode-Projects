class User:
    def __init__(self, user_id, username, followers):
        self.id = user_id
        self.username = username
        self.followers = followers

user1 = User("001", "Dani", 3)

print(user1.username)