import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

def take_picture(name = 'academia'):
  ret, frame = cap.read()
  current_timestamp = time.time()

  cv2.imwrite("%s_%s.jpg" % (name,current_timestamp), frame)
  print("Imagem capturada")

if not cap.isOpened():
  raise IOError("Cannot open webcam")

cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)

while True:
  ret, frame = cap.read()

  if not ret:
    break

  cv2.imshow('Webcam', frame)

  #aperte 'q' para sair
  if cv2.waitKey(1) == ord('q'):
    break

cv2.createTrackbar("Tirar foto", "Webcam", 0, 100, take_picture('sb'))

cap.release()
cv2.destroyAllWindows()