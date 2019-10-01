import face_recognition
import detect_anime
import cv2
import numpy
from PIL import Image

a = 0
r = 0
for i in range(1,203):
    try:
        filename = "Results\\Generation 6\\epoch{}.png".format(i)
        img = Image.open(filename)

        for face in detect_anime.detect(filename):
            r += 1
            face_img = img.crop(face)
            face_img = face_img.convert("RGB")
            face_img.save("GENERATED_FACES\\face_{}.jpg".format(r), "JPEG")

        for face in face_recognition.api.face_locations(face_recognition.load_image_file(filename)): #(top, right, bottom, left)
            r += 1
            face_img = img.crop((face[3], face[0], face[1], face[2])) #(left, upper, right, lower)
            face_img = face_img.convert("RGB")
            face_img.save("GENERATED_FACES\\face_{}.jpg".format(r), "JPEG")
    except:
        print("Error, continuing.")
