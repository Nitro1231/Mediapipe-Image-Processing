import cv2
import time
import image_processing as ip
import mediapipe_processing as mp

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


while True:
    start_time = time.time()
    ret, image_org = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    # Our operations on the frame come here
    # image = image_org

    # image = ip.to_gray(image_org)
    # image = ip.bgr2rgb(image_org)
    # image = ip.face_detection(image_org)

    # image = mp.face_detection_tracking(image_org)
    # image = mp.face_mesh_tracking(image_org)
    image = mp.hands_tracking(image_org)
    # image = mp.holistic_tracking(image_org)
    # image = mp.object_detection(image_org)
    # image = mp.pose_tracking(image_org)


    # FPS Counter
    end_time = time.time()
    fps = 1 / (end_time - start_time)
    cv2.putText(image, f'FPS: {int(fps)}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (161, 252, 3), 3)

    # Display the resulting frame
    cv2.imshow('image', image)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()