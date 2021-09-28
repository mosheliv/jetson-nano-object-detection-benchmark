# Jetson Nano Object Detection Benchmark

This repository was created becuase of the difficulty in finding consistent, easy to use and understand information regarding deploying object detection on the Jetson Nano.
The information and published benchmarks are usually borderline misleading or just not reproducible.

In this repository i'll summerize my experiments with code that measure the inference and post processing 
(one of the usual cheats is not measuring the nms/postprocessing which sometimes takes longer than the actual inference). I also did not use deepstream/gstreamer as it 
obfuscates the basic speed of the inference. 

The basic structure of the code is:

```
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
```

Any contributions to the repository are welcome, please create a pull request.

All expriments were done with the same image, https://ultralytics.com/images/bus.jpg, same nano with jetpack 4.6 and MAXN power.

I do not include in this repository mAP results etc, as basically its best to test the models on your own data and see how well it works.

The repository is split by object detection method (yolov3, yolov4, etc 

## Yolov5

| model | size |platform | speed | fps | link to code | comments |
| --- | --- | --- | --- | --- | --- | --- |
| Yolov5s | 320 | pytorch | 0.090ms | 11 | [link](https://github.com/mosheliv/jetson-nano-object-detection-benchmark/yolov5/pytorch_hub.py) | ultralytics model from pytorch hub, jp 4.6, pytorch 1.9 | 
| Yolov5s | 418 | pytorch | 0.121ms | 8.23 | [link](https://github.com/mosheliv/jetson-nano-object-detection-benchmark/yolov5/pytorch_hub.py) | ultralytics model from pytorch hub, jp 4.6, pytorch 1.9 |
| Yolov5s | 640 | pytorch | 0.1934ms | 5.16 | [link](https://github.com/mosheliv/jetson-nano-object-detection-benchmark/yolov5/pytorch_hub.py) | ultralytics model from pytorch hub, jp 4.6, pytorch 1.9 |
| Yolov5s | 320 | tensorrtx | 0.0357ms | 27.97 | [link](https://github.com/mosheliv/jetson-nano-object-detection-benchmark/yolov5/tensorrtx.py) | from tensorrtx, see code for link. Note that size needs to be changed in yololayer.h|
| Yolov5s | 418 | tensorrtx | 0.0815ms | 12.27 | [link](https://github.com/mosheliv/jetson-nano-object-detection-benchmark/yolov5/tensorrtx.py) | from tensorrtx, see code for link. Note that size needs to be changed in yololayer.h |
| Yolov5s | 320 | tensorrtx | 0.1008ms | 9.917 | [link](https://github.com/mosheliv/jetson-nano-object-detection-benchmark/yolov5/tensorrtx.py) | from tensorrtx, see code for link. Note that size needs to be changed in yololayer.h |

## NVIDIA SSD300
| model | size |platform | speed | fps | link to code | comments |
| --- | --- | --- | --- | --- | --- | --- |
| SSD300 | 300 | pytorch | 0.66ms | 1.48 | | NVIDIA SSD example |

