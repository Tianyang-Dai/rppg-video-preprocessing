import os
import re
from utils import *

openface_path = r"openface\FeatureExtraction.exe"  # OpenFace路径
raw_30_folder = r"dataset\VIPL-HR\data_30"  # 30fps视频文件夹


# 1. 帧率转换为30fps
raw_folder = r"dataset\VIPL-HR\data"  # 原视频文件夹

p_folders = get_subfolders(raw_folder)
for p_folder in p_folders:  # 例如："dataset\VIPL-HR\data\p99"
    p = os.path.basename(p_folder)  # 例如："p99"
    
    v_folders = get_subfolders(p_folder)
    for v_folder in v_folders:  # 例如："dataset\VIPL-HR\data\p99\v9"
        v = os.path.basename(v_folder)  # 例如："v9"
        
        source_folders = get_subfolders(v_folder)
        for source_folder in source_folders:  # 例如："dataset\VIPL-HR\data\p99\v9\source2"
            source = os.path.basename(source_folder)  # 例如："source2"
            
            # 删除低照明
            if source == "source4":
                continue
            
            video_paths = get_video_paths(source_folder)
            for video_path in video_paths:  # 例如："dataset\VIPL-HR\data\p99\v9\source2\video.avi"
                video_30_folder = os.path.join(raw_30_folder, p, v, source)  # 例如："dataset\VIPL-HR\data_30\p99\v9\source2"
                os.makedirs(video_30_folder, exist_ok=True)
                video_30_path = os.path.join(video_30_folder, "vid.avi")  # 例如："dataset\VIPL-HR\data_30\p99\v9\source2\vid.avi"
                convert_video_fps(video_path, video_30_path)
    
    print(f'{p}帧率转换为30fps完成!')


# 2. 使用OpenFace生成面部标志点
raw_folder = raw_30_folder  # 例如："dataset\VIPL-HR\data_30"
lmk_folder = r"dataset\VIPL-HR\lmk"
os.makedirs(lmk_folder, exist_ok=True)

p_folders = get_subfolders(raw_folder)
for p_folder in p_folders:  # 例如："dataset\VIPL-HR\data_30\p99"
    p = os.path.basename(p_folder)  # 例如："p99"

    v_folders = get_subfolders(p_folder)
    for v_folder in v_folders:  # 例如："dataset\VIPL-HR\data_30\p99\v9"
        v = os.path.basename(v_folder)  # 例如："v9"

        source_folders = get_subfolders(v_folder)
        for source_folder in source_folders:  # 例如："dataset\VIPL-HR\data_30\p99\v9\source2"
            source = os.path.basename(source_folder)  # 例如："source2"

            video_paths = get_video_paths(source_folder)
            for video_path in video_paths:  # 例如："dataset\VIPL-HR\data_30\p99\v9\source2\vid.avi"
                lmk_path = os.path.join(lmk_folder, p, v, source)  # 例如："dataset\VIPL-HR\lmk\p99\v9\source2"
                os.system(f"{openface_path} -f {video_path} -out_dir {lmk_path} -2Dfp")
            
    print(f'{p}使用OpenFace生成面部标志点完成!')
