# Take in an image, locates the faces and displays each face in a seperate photo
import face_recognition
from PIL import Image

# Loads image as a numpy array
image = face_recognition.load_image_file('./images/groups/team1.jpg')
# Location for the faces in the image
face_location = face_recognition.face_locations(image)

for face_location in face_locations:
    top, right, botton, left =

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    # Saves each face in the photo as a seperate .jpg file
    pil_image.save('f{top}.jpg')
