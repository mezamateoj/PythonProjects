class User:

    # constructor of my class, attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # print(f'new user: {self.username} is created..')
        # print(f'the user id is {self.id}.')

    # adding methods
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User('001', 'yogu')
user2 = User('002', 'sonia')

user1.follow(user2)
print(user2.followers)
print(user1.following)