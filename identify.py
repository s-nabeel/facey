# Takes in an image and recognizes their faces, if a match is found.
# Once a match is found, a box with a name of the person will appear over the image.
# Quite similar to how Facebook suggests auto-tagging your freinds.

import face_recognition
from PIL import Image, ImageDraw

# Loads image as a numpy array
image_of_bill = face_recognition.load_image_file('./images/known/Bill Gates.jpg')
# Obtains the face encoding of Bill Gates and attemps to match them with the faces in ./images
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

image_of_steve = face_recognition.load_image_file('./images/known/Steve Jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

# Create an array of encodings and names
known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding
]

known_face_names = [
    "Bill Gates",
    "Steve Jobs"
]

# Load the image
test_image = face_recognition.load_image_file('./images/groups/bill-elon-steve.jpg')

# Find the faces in test_image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert test_image into PIL format (so its drawable)
pil_image = Image.fromarray(test_image)

# Create an ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through the faces found in the test_image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If match found
    if True in matches:
        first_match_ndex = matches.index(True)
        name = known_face_names[first_match_ndex]

    # Draw the box
    draw.rectangle(((left, top), (right, bottom)), outline = (0, 0, 0))

    # Draw the label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill = (0, 0, 0), outline = (0, 0, 0))
    draw.text((left + 6, bottom - text_height - 5), name, fill = (255, 255, 255, 255))

# Delete the draw instance for efficient memory usage
del draw

# Display the image
pil_image.show()

# Save the image
pil_image.save('identify.jpg')
