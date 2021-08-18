import cv2
import face_detection
from face_detection import available_detectors, build_detector
from face_detection.utils import draw_detections


print(available_detectors)
WEIGHTS_PATH = "./weights/RetinaFace_mobilenet025.pth"
detector = build_detector("RetinaNetMobileNetV1", model_path=WEIGHTS_PATH, confidence_threshold=.2, nms_iou_threshold=.3)

# BGR to RGB

source = "./videos/vid.mp4"
cap = cv2.VideoCapture(source)

while True:
    ret, frame = cap.read()
    if ret:
        detections = detector.detect(frame)
        image_final = draw_detections(frame, detections, color="red", thickness=3)

        #cv2.namedWindow("Face Detection", cv2.WINDOW_AUTOSIZE)  # Create window with freedom of dimensions
        cv2.imshow("Face Detection", image_final)
        cv2.waitKey(20)

    else:
        break