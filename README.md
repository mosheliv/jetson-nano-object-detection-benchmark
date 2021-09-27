# Jetson Nano Object Detection Benchmark

This repository was created becuase of the difficulty in finding consistent, easy to use and understand options regarding deploying object detection on the Jetson Nano.
The information and published benchmarks usually borderline misleading or just not reproducible.

In this repository i'll summerize my experiments with code that measure the inference and post processing 
(one of the usual cheats is not measuring the nms/postprocessing which sometimes takes longer than the actual inference). I also did not use deepstream/gstreamer as it 
obfuscates the basic speed of the inference. 

The basic structure of the code is:

load model
load image
do one warmup inference

start overall clock
loop 10 times:
    start iteration clock
    pre-process
    inference
    post process
    print detection results (this is becuase some models have lazy post process)
    print iteration time

print overall speed

Any contributions to the repository are welcome, please create a pull request.

All expriments were done with the same image, https://ultralytics.com/images/bus.jpg

I do not include in this repository mAP results etc, as basically its best to test the models on your own data and see how well it works.

The repository is split by object detection method (yolov3, yolov4, etc 

## Yolov5

| model | size |platform | speed | fps | link to code | comments |
| --- | --- | --- | --- | --- | --- | --- |
| Yolov5s | 320 | pytorch | 0.0794ms | 12.59 | | ultralytics model from pytorch hub, jp 4.6, pytorch 1.9 | 
| Yolov5s | 418 | pytorch | 0.1159ms | 8.62 | | ultralytics model from pytorch hub, jp 4.6, pytorch 1.9 |
| Yolov5s | 640 | pytorch | 0.1884ms | 5.30 | | ultralytics model from pytorch hub, jp 4.6, pytorch 1.9 |
