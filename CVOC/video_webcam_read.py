# #Reading video from Webcam:

# import cv2


# video = cv2.VideoCapture(0)


# if (video.isOpened() == False):
#     print("Error reading video file")


# frame_width = int(video.get(3))
# frame_height = int(video.get(4))

# size = (frame_width, frame_height)

# result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

# while (True):
#     ret, frame = video.read()

#     if ret == True:

#         result.write(frame)

#         cv2.imshow('Frame', frame)

#         if cv2.waitKey(1) & 0xFF == ord('s'):
#             break

#     # Break the loop
#     else:
#         break
# video.release()
# result.release()
# cv2.destroyAllWindows()
#-------------------------------------------------------------------------------------
import cv2

# Open webcam
video = cv2.VideoCapture(0)

# Read logo image
logo = cv2.imread('klh.jpg')
logo = cv2.resize(logo, (200, 100))  # Resize if needed

if not video.isOpened():
    print("Error reading video stream")
    exit()

# Get video frame dimensions
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Resize logo to fit frame better, optional
logo_height, logo_width = logo.shape[:2]

# Top-right corner placement
top_left_y = 0
top_left_x = frame_width - logo_width

# Video writer setup
size = (frame_width, frame_height)
result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

while True:
    ret, frame = video.read()

    if ret:
        # Overlay the logo on the frame
        frame[top_left_y:top_left_y + logo_height, top_left_x:top_left_x + logo_width] = logo

        # Write and show the frame
        result.write(frame)
        cv2.imshow('Frame with Logo', frame)

        # Exit on 's' key
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        break

# Release everything
video.release()
result.release()
cv2.destroyAllWindows()
