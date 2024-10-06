import numpy as np
import cv2
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import os
import sys

parametros = sys.argv
parametros.pop(0)

image_path = '''images/'''+parametros[0]+'''.png'''
if os.path.isfile(image_path) == False:
  print('Imagem não encontrada')
  exit(1);

img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
#plt.imshow(img)

detector = MTCNN()
result = detector.detect_faces(img)

#print(result)

x1, y1, width, height = result[0]['box']
left_eye, right_eye = result[0]['keypoints']['left_eye'], result[0]['keypoints']['right_eye']
mouth_left, mouth_right = result[0]['keypoints']['mouth_left'], result[0]['keypoints']['mouth_right']
nose = result[0]['keypoints']['nose']

fig = plt.figure()

radius_size = 6

supposed_height_value = 50
count = 1
while supposed_height_value < height:
  radius_size = radius_size + 1
  supposed_height_value = supposed_height_value * count
  count = count + 1

ax = fig.add_subplot(111)
ax.imshow(img)
ax.add_patch(Rectangle((x1,y1), width, height, fill=False, ec='r', lw=2))
ax.add_patch(Circle(left_eye, fill=True, color='red', radius=radius_size))
ax.add_patch(Circle(right_eye, fill=True, color='red', radius=radius_size))
ax.add_patch(Circle(mouth_left, fill=True, color='red', radius=radius_size))
ax.add_patch(Circle(mouth_right, fill=True, color='red', radius=radius_size))
ax.add_patch(Circle(nose, fill=True, color='red', radius=radius_size))

ax.axis('off')
plt.savefig('''images_marked/'''+parametros[0]+'''_marked.png''', pad_inches=0.1)

plt.show()