from datetime import datetime
import os
import User


class Log:
    def __init__(self,User,date,time):
        self.ID = User
        self.date = date
        self.time = time

    def getUser(self):
        return self.User
    
    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def saveLog(User):
        onlyFiles = [f for f in os.listdir("Logs") if os.path.isfile(os.path.join("Logs", f))]
        logName = str(len(onlyFiles) + 1)
        f = open("Logs/" + logName, "w")
        log = str(User.getID()) + "," + User.getName() + "," + datetime.now().strftime("%d/%m/%Y,%H:%M:%S")
        f.write(log)
        f.close()
    
