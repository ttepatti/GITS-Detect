import cv2
import sys

# --------------- Image Paths ---------------
# Get user supplied image
faceImagePath = sys.argv[1]

# The Ghost in the Shell image
gitsImagePath = "laughing_man_transparent.png"

# Our cascade
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# --------------- Loading Images ---------------

# Read the image of faces
faceImage = cv2.imread(faceImagePath)

# Load unchanged so it keeps channel 4 (alpha)
gitsImage = cv2.imread(gitsImagePath, cv2.IMREAD_UNCHANGED)

# gitsAlpha = alpha channel of gitsImage (creating mask)
gitsAlpha = gitsImage[:,:,3]

# gitsAlpha_inv = inverted mask
gitsAlpha_inv = cv2.bitwise_not(gitsAlpha)

# Convert gits image to RGB (no Alpha)
gitsRGB = gitsImage[:,:,0:3]

# --------------- Face Detection ---------------

# Gray channel of background image for cascade
gray = cv2.cvtColor(faceImage, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

print(faces)

# --------------- Loop through faces ---------------

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    # Make x, y around 30% different from where they were (to deal with the bigger gits image)
    x = int(x - (w * 0.3))
    y = int(y - (h * 0.3))

    # Just in case we go out of bounds!
    if x < 0: x = 0
    if y < 0: y = 0


    # Grow the gits image by 50%
    w = int(w + (w * 0.5))
    h = int(h + (h * 0.5))

    # Get region of interest around faces
    # the y+h is because we're getting the y coord of the lower right corner
    # same with x+w
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = faceImage[y:y+h, x:x+w]

    # Resize the RGB image, mask, and inverted mask to the size of the face
    gits = cv2.resize(gitsRGB, (w, h), interpolation = cv2.INTER_AREA)
    mask = cv2.resize(gitsAlpha, (w, h), interpolation = cv2.INTER_AREA)
    mask_inv = cv2.resize(gitsAlpha_inv, (w, h), interpolation = cv2.INTER_AREA)

    # roi_bg will contain the original image only where there is no face
    roi_bg = cv2.bitwise_and(roi_color, roi_color, mask = mask_inv)

    # roi_fg contains the image of the gits symbol without the background (afaik?)
    roi_fg = cv2.bitwise_and(gits, gits, mask = mask)

    # join the roi_bg and roi_fg
    dst = cv2.add(roi_bg, roi_fg)

    # place the joined final image in dst
    faceImage[y:y+h, x:x+w] = dst

cv2.imshow("Faces found", faceImage)
cv2.waitKey(0)