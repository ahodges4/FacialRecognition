import cv2, cv, os, shutil
from User import User
import numpy as np
from PIL import Image,ImageTk

folder = "Details"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
user2 = User(1, "Dylan")
user2.save()
user1 = User(0, "Adam")
user1.save()







cv.facialRecognition()


