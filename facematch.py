# Takes in an image, and checks to see if the face(s) in the image
# match those faces for which we've assigned encodings for

import face_recognition

# Loads image as a numpy array
image_of_bill = face_recognition.load_image_file('./images/known/Bill Gates.jpg')
# Obtains the face encoding of Bill Gates and attemps to match them with the faces in ./images
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unknown_image = face_recognition.load_image_file('./images/known/Elon Musk.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Comparing the two faces (returns a boolean value)
results = face_recognition.compare_faces([bill_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is an image of Bill Gates')
else:
    print('This is NOT an image of Bill Gates')
