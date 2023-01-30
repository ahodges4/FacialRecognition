import string
import cv2, os, shutil
from User import User
import numpy as np
from PIL import Image,ImageTk
from textwrap import wrap
import pandas as pd
from Log import Log

def take_img(user, amount):

    try:
        cam = cv2.VideoCapture(0)
        classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        directory = "TrainingImage/"
        
        if os.path.exists(directory) == False:
            os.mkdir(directory)
        
        

        count = 0
        loop = True
        while loop == True:
            ret, img = cam.read()#Captures image from the camera
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray_img, 1.4, 5)#find faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)#draw rectangle around faces
                count = count + 1#increase count by 1

                cv2.imwrite("TrainingImage/ " + user.getName() + "." + str(user.getID()) + '.' + str(count) + ".jpg", gray_img[y:y + h, x:x + w])#Saves image to a file
                cv2.imshow("Frame", img)#Displays camera output 
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    loop = False
                elif count > amount:
                    loop = False
        cam.release() # Release the camera so that it can be used else where
        cv2.destroyAllWindows()#close the camera display window   
    except FileExistsError as F:
        print("Files already Exist")
        return False
    return True

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global faceCascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces,Id
        faces, Id = getImagesAndLabels("TrainingImage")#Load all of the images and Names from the folder "trainingImage"
        recognizer.train(faces, np.array(Id)) #Train model with images and a numpy array of ID's
        modeltrained = True
    except Exception as e:
        modeltrained = False
        return e
        
    
    if modeltrained == True: 
        recognizer.write("TrainingImageLabel\Trainner.yml")#Save the model
    
    return modeltrained
        
        
def getImagesAndLabels(path):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empty face list
    faceSamples = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image

        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces = faceCascade.detectMultiScale(imageNp)
        # If a face is there then append that in the list as well as Id of it
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids


def facialRecognition():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    try:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    except:
        return False
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    
    camera = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = camera.read()
        gray_img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_img, 1.4, 5)
        for (x, y, w, h) in faces:
            global Id
            Id, confidence = recognizer.predict(gray_img[y:y + h, x:x + w])
            if (confidence < 70):
                global aa
                global tt
                user = User.findUser(Id)
                text = str(user.getID()) + "-" + user.getName()
                #print("Hello " + text)
                #Log.saveLog(user)
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                cv2.putText(im, str(text), (x + h, y), font, 1, (255, 255, 0,), 4)
            else:
                Id = 'Unknown'
                tt = str(Id)
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
        cv2.imshow("Facial Recogntion", im)
        key = cv2.waitKey(30) & 0xff
        if key == 27:
            break










    

    


