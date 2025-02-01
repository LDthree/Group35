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
Performs continuous face detection with the camera.

Simply run the script and it will draw boxes around detected faces:

    python3 detect_faces.py

For more instructions, see g.co/aiy/maker
"""

from aiymakerkit import vision
from aiymakerkit import utils
import models
from pycoral.adapters.detect import BBox

detector = vision.Detector(models.FACE_DETECTION_MODEL)

# Define the auto shutter detection zone
width, height = vision.VIDEO_SIZE
xmin = int(width * 0.25)
xmax = int(width - (width * 0.25))
ymin = int(height * 0.2)
ymax = int(height - (height * 0.2))
camera_bbox = BBox(xmin, ymin, xmax, ymax)

# Define the protected fence region
width, height = vision.VIDEO_SIZE
xmin = 0
ymin = 0
xmax = int(width * 0.5)
ymax = int(height * 0.5)
fence_box = BBox(xmin, ymin, xmax, ymax)

# Check if in box
def box_is_in_box(bbox_a, bbox_b):
    if ((bbox_a.xmin > bbox_b.xmin) and (bbox_a.xmax < bbox_b.xmax)) and (
        (bbox_a.ymin > bbox_b.ymin) and (bbox_a.ymax < bbox_b.ymax)):
        return True
    return False

for frame in vision.get_frames():
    faces = detector.get_objects(frame, threshold=0.1)
    print(faces)
    vision.draw_objects(frame, faces)
    vision.draw_rect(frame, camera_bbox)
    if faces and box_is_in_box(faces[0].bbox, camera_bbox):
        print("Face is inside the box!")
        
for frame in vision.get_frames():
    vision.draw_rect(frame, fence_box)
    objects = detector.get_objects(frame, threshold=0.4)
    for obj in objects:
        label = labels.get(obj.id)
        if 'person' in label:
            print('A person was detected!')