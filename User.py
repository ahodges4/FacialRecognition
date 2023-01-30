class User:
    def __init__(self,ID,name):
        self.ID = ID
        self.name = name

    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name

    def save(self):
        f = open("Details/Details.txt", "a")
        f.write(str(self.ID) + "," + self.name + ":")
        f.close()

    def deleteUser(self):
        Users = self.readUsers()
        for x in Users:
            if self.ID == int(x.getID()):
                Users.remove(x)

        f = open("Details/Details.txt", "w")

        for x in Users:
            f.write(str(x.getID()) + "," + x.getName() + ":")
        f.close()

    def readUsers():
        Users = []
        f = open("Details/Details.txt", "r")
        UserList = f.read().split(":")[:-1]
        for x in UserList:
            x = x.split(",")
            user = User(x[0],x[1])
            Users.append(user)
        f.close()
        return Users

    def deleteAllUsers():
        f = open("Details/Details.txt", "w")
        f.write("")
        f.close()

    def findUser(ID):
        Users = User.readUsers()
        for user in Users:
            if int(user.getID()) == int(ID):
                return user