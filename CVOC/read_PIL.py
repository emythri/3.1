# import cv2

# image1=cv2.imread('Cat.jpg')
# type(image1)
# cv2.imshow("Image",image1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#---------------------------------------
import cv2

# Read the main image and logo
image = cv2.imread('Cat.jpg')
logo = cv2.imread('klh.jpg')

# Resize logo if needed (optional, here resized to 200x100)
logo = cv2.resize(logo, (200, 100))

# Get dimensions
image_height, image_width = image.shape[:2]
logo_height, logo_width = logo.shape[:2]

# Define the position for the top-right corner
top_left_y = 0
top_left_x = image_width - logo_width

# Place the logo on the image
image[top_left_y:top_left_y + logo_height, top_left_x:top_left_x + logo_width] = logo

# Show the result
cv2.imshow("Image with Logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

