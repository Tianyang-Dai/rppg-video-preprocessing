import os
import ffmpeg


def get_video_codec(input_video):
    # 获取视频文件的编解码信息
    probe = ffmpeg.probe(input_video, v='error', select_streams='v:0', show_entries='stream=codec_name')
    return probe['streams'][0]['codec_name']


def convert_video_fps(input_video, output_video, target_fps=30):
    # 将输入视频的帧率转换为指定的输出帧率
    # input_video: 输入视频文件的路径
    # output_video: 输出视频文件的路径
    # output_fps: 输出视频的帧率

    # 获取视频编码格式
    codec = get_video_codec(input_video)
    
    # 根据视频编码格式选择编码器
    if codec in ['ffv1', 'huffyuv']:  # 无损编码格式
        print(f"输入视频使用无损编码({codec}), 保持无损转码...")
        ffmpeg.input(input_video).output(output_video, r=target_fps, vcodec=codec).run()
    else:  # 对于其他编码格式，使用libx264并尽量减少质量损失
        print(f"输入视频编码格式: {codec}, 使用libx264进行转码...")
        ffmpeg.input(input_video).output(output_video, r=target_fps, vcodec='libx264', crf=0).run()
    

def get_subfolders(folder: str):
    # 获取某个文件夹下一级子文件夹的完整路径
    # folder: 指定的父文件夹路径
    if not os.path.isdir(folder):
        raise ValueError(f"{folder} 不是一个有效的文件夹路径.")

    subfolders = [
        os.path.join(folder, name)
        for name in os.listdir(folder)
        if os.path.isdir(os.path.join(folder, name))
    ]

    return subfolders


def get_video_paths(folder: str, video_extensions=None):
    # 获取指定文件夹中所有视频文件的完整路径
    # folder: 指定的文件夹路径
    # video_extensions: 视频文件的扩展名列表
    if video_extensions is None:
        # 默认的视频文件扩展名
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm']

    if not os.path.isdir(folder):
        raise ValueError(f"{folder} 不是一个有效的文件夹路径.")

    video_files = [
        os.path.join(folder, name)
        for name in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, name)) and
        any(name.lower().endswith(ext) for ext in video_extensions)
    ]

    return video_files
