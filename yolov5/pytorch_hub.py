# see https://pytorch.org/hub/ultralytics_yolov5/
# checked with jp46+pytorch 1.9
import torch
import time
import cv2

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5-tiny', pretrained=True)

# Images
image = cv2.imread("bus.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = model(image, size=320)
s0 = time.time()
tot_time = 0
for i in range(10):
    s = time.time()
    results = model(image, size=320)
    tot_time += time.time()-s
    print(time.time()-s, (i+1)/tot_time)
    results.print()

print(tot_time/10, 10/tot_time)
