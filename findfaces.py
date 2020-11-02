# Takes in an image of a group of people, and recognizes their
# faces and locations (similar to how Facebook locates faces in your pictures)

import face_recognition

# Loads image as a numpy array
image = face_recognition.load_image_file('./images/groups/team1.jpg')
# Location for the faces in the image
face_location = face_recognition.face_locations(image)

# Array of coordinates for each face
print(face_location)

# Number of people within the image
print(f'There are {len(face_location)} people in this image')
