# rppg-video-preprocessing

## Overview
This repository is designed to process videos in the VIPL-HR dataset. It performs two main operations: converting the frame rate of raw videos to 30 fps and then using OpenFace to generate facial landmarks for the converted videos. These operations are crucial for rPPG data analysis and are often missing in many rPPG open-source codes. 

## Features
1. Frame rate conversion: Converts all videos in the VIPL-HR dataset to a frame rate of 30 fps. Special attention is paid to video encoding formats to minimize quality loss, which could potentially damage the rPPG signals within the video.
2. Facial landmark generation: Utilizes OpenFace to extract 2D facial landmarks from the 30 fps videos.

## Prerequisites
- Python environment with necessary libraries installed, including those used in `utils.py`.
- OpenFace installed and the path to `FeatureExtraction.exe` configured correctly.

## How to Use
1. Configure the paths:
    - In the script, set the `openface_path` to the path of `FeatureExtraction.exe` in your OpenFace installation.
    - Set the `raw_folder` and `raw_30_folder` according to your dataset directory structure.
    - The `lmk_folder` is where the generated facial landmarks will be stored.
2. Run the script:
    Simply execute the Python script in your terminal or IDE.

## Directory Structure
- `dataset/VIPL-HR/data`: The original video dataset.
- `dataset/VIPL-HR/data_30`: The converted 30 fps video dataset.
- `dataset/VIPL-HR/lmk`: The directory where facial landmarks are stored.

## Code Structure
- Frame rate conversion: The script iterates through all the sub - folders of the VIPL-HR dataset, skips the low - illumination source folders, and converts each video to 30 fps.
- Facial landmark generation: After the frame rate conversion, it uses OpenFace to generate facial landmarks for each 30 fps video.

```python
import os
import re
from utils import *

openface_path = r"openface\FeatureExtraction.exe"
raw_30_folder = r"dataset\VIPL-HR\data_30"
raw_folder = r"dataset\VIPL-HR\data"
lmk_folder = r"dataset\VIPL-HR\lmk"

Frame rate conversion...
Facial landmark generation...
```

## Notes
- Make sure all the necessary libraries in `utils.py` are installed correctly.
- Ensure that the OpenFace `FeatureExtraction.exe` can be accessed from the specified path.  
