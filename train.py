from User import User
import cv, os, shutil

folder = "TrainingImage"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

People = ["Adam","Dylan"]

PersonOne = User(People[0],1)
for name in People:
    Person = User(People.index(name),name)
    cv.take_img(Person, 100)
    print(Person.getName())
    print(Person.getID())

cv.train_model()







