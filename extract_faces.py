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

x1, y1, width, height = result[0]['box']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img)
ax.add_patch(Rectangle((x1,y1), width, height, fill=False, ec='r', lw=2))

ax.axis('off')
plt.savefig(parametros[0]+'''_marked.png''', pad_inches=0.1)



plt.show()