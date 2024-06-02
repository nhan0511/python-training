import os
import subprocess

path = "videos"
output_path = "mp3s"


def convert(s):
    last_index = s.rfind('4')
    return s[:last_index] + '3'


os.makedirs(output_path, exist_ok=True)

mp4s = os.listdir(path)

for mp4_file in mp4s:
    path_mp4 = os.path.join(path, mp4_file)
    mp3_file = convert(mp4_file)
    mp3_path = os.path.join(output_path, mp3_file)
    subprocess.run(f"ffmpeg -i {path_mp4} {mp3_path}", shell=True)
