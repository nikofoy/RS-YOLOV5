import cv2
import os

# 检查文件路径
video_path = "./SVID.mp4"
if not os.path.exists(video_path):
    print(f"文件 {video_path} 不存在")
    exit()

# 检查文件权限
if not os.access(video_path, os.R_OK):
    print(f"没有权限读取文件 {video_path}")
    exit()

# 打开视频文件
video = cv2.VideoCapture(video_path)

# 尝试读取视频帧
try:
    # 检查视频是否成功打开
    if not video.isOpened():
        print("无法打开视频文件")
        exit()

    # 获取视频的帧率 (FPS)
    fps = video.get(cv2.CAP_PROP_FPS)

    # 计算每 20 秒的帧数
    interval_frames = int(fps * 3)

    # 创建保存图像的文件夹
    output_folder = "./datasets/images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 初始化帧计数器
    frame_count = 0
    image_count = 0

    while True:
        # 读取帧
        ret, frame = video.read()

        # 如果无法读取帧，则退出循环
        if not ret:
            break

        # 每 20 秒保存一帧
        if frame_count % interval_frames == 0:
            # 生成文件名
            image_name = f"{image_count:04d}.png"
            image_path = os.path.join(output_folder, image_name)

            # 保存帧
            cv2.imwrite(image_path, frame)
            print(f"保存帧: {image_path}")

            # 增加图像计数器
            image_count += 1

        # 增加帧计数器
        frame_count += 1

    # 释放视频对象
    video.release()

except Exception as e:
    print(f"发生错误: {e}")