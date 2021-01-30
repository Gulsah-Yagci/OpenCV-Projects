# import libraries
import cv2
import imageio

#load cascade
face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade-eye.xml')

# face detection funcion
def detect(frame):

    # rgb to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # scale image and choosing the square's closest neighbors
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # rectangle function to be drawn for each face
    for(x, y, w, h) in faces:

        # rectangle coordinates and edge settings
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        #detection for eyes
        gray_face = gray[y:y+h,x:x+w]
        color_face = frame[y:y + h, x:x + w]
        
        # same scaling for face with different scale and different number of neighbors
        eyes = eye_cascade.detectMultiScale(gray_face, 1.1, 3)

        # drawing a rectangle for the eye
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(color_face, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame

# video processing

# read video
reader = imageio.get_reader('1.mp4')
# frame per second for video
fps = reader.get_meta_data()['fps']
# output video
writer= imageio.get_writer('output.mp4', fps=fps)

# detection face on video
for i, frame in enumerate(reader):
    frame = detect(frame)
    writer.append_data(frame)

    # traking frame
    print(i)

writer.close()