from google.cloud import vision
export GOOGLE_APPLICATION_CREDENTIALS="./luggage.json"

client = vision.ImageAnnotatorClient()

with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations
print('Labels:')

for label in labels:
    print(label.description)