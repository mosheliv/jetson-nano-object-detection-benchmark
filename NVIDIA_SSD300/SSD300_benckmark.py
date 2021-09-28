# see https://pytorch.org/hub/nvidia_deeplearningexamples_ssd/

import torch
import time

ssd_model = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd')
utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd_processing_utils')

ssd_model.to('cuda')
ssd_model.eval()
classes_to_labels = utils.get_coco_object_dictionary()

uris = [
    'https://ultralytics.com/images/bus.jpg',
]

inputs = [utils.prepare_input(uri) for uri in uris]
#warmup
tensor = utils.prepare_tensor(inputs)
with torch.no_grad():
    detections_batch = ssd_model(tensor)
results_per_input = utils.decode_results(detections_batch)

tot_time = 0
for i in range(10):
    s = time.time()
    tensor = utils.prepare_tensor(inputs)
    with torch.no_grad():
        detections_batch = ssd_model(tensor)
    results_per_input = utils.decode_results(detections_batch)
    tot_time += time.time()-s
    print(time.time()-s, (i+1)/tot_time)

print(tot_time/10, 10/tot_time)
