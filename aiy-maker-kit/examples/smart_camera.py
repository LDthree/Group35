# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Performs continuous object detection with the camera.

Simply run the script and it will draw boxes around detected objects along
with the predicted labels:

    python3 detect_objects.py

For more instructions, see g.co/aiy/maker
"""

from aiymakerkit import vision
from aiymakerkit import utils
import models
from pycoral.adapters.detect import BBox

# Define the protected fence region
width, height = vision.VIDEO_SIZE
xmin = 0
ymin = 0
xmax = int(width * 0.5)
ymax = int(height * 0.5)
fence_box = BBox(xmin, ymin, xmax, ymax)

detector = vision.Detector(models.OBJECT_DETECTION_MODEL)
labels = utils.read_labels_from_metadata(models.OBJECT_DETECTION_MODEL)

for frame in vision.get_frames():
    vision.draw_rect(frame, fence_box)
    objects = detector.get_objects(frame, threshold=0.4)
    for obj in objects:
        label = labels.get(obj.id)
        if 'person' in label:
            print('A person was detected!')


