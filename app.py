from flask import Flask, render_template, request
import cv2
from google.cloud import vision
import io

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
    print('Labels:')

    for label in labels:
        print(label.description)


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "luggage{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        detect_labels('luggage'+str(img_counter) + '.png')
        print()
        print()
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

@app.route('/', methods=['POST'])
def parse_request():
    data = request.data  # data is empty
    # need posted data here
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)