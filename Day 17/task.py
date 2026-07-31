class User:
    def __init__(self, user_id, username):  #attributes, class constructors and __init__()
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0 #adding methods to class

    def follow(self,user):
        user.followers += 1
        self.followers += 1

        # print("new user being created.....")# that means it calls out evry time when new user is created
    # pass
#using pass is simply moving forward without considering function and continue with nxt line without error
user_1 = User("001","sonu")
user_2 = User("002","jack")
# print(user_1.followers)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# user_1 = User()
# user_1.id = "001"
# user_1.username = "sonu"

# print(user_1.id)
# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "sonu"

# print(user_2.id)
# print(user_2.username)

# print(user_1.id)
# print(user_1.username)