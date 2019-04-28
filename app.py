from flask import Flask, render_template, request
import cv2
from google.cloud import vision
import io
import re # for regular expressions in getting label 
import time # for sleep
from twil import isamatch
from faceCheck import faceCheck

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    #print('Labels:')

    regex = "red|luggage|bag"
    boolRed = False
    boolBag = False
    for label in labels:
        desc = label.description
        desc
        if(boolRed and boolBag):
            isamatch(True)
            return True
        if(desc == 'Red'):
            boolRed = True
        elif(desc == 'Luggage' or desc == 'Bag' or desc == 'Backpack'):
            boolBag = True
        #else:
            #print("aww not a match")
        #print(label.description)
    return False
def loggedIn():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("security")

    img_counter = 0

    while True:
        (ret, frame) = cam.read()
        cv2.imshow("security", frame)
        
        # if the frame was not grabbed, then we have reached the end
        # of the stream 
        if not ret:
            break
        k = cv2.waitKey(500)

        #if k%256 == 27:
         #   # ESC pressed
         #   print("Escape hit, closing...")
         #   break
        #elif k%256 == 32:
            # SPACE pressed
        img_name = "luggage{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        #print("{} written!".format(img_name))
        if(detect_labels('luggage'+str(img_counter) + '.png')):
            break

    cam.release()

    cv2.destroyAllWindows()

def checkLogin():
    faceCheck()
    cv2.destroyAllWindows()
    loggedIn()


@app.route('/', methods=['POST'])
def parse_request():
    checkLogin()
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def parse_log():
    return render_template()

if __name__ == "__main__":
    app.run(debug=True)