from moviepy.editor import *
import os

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #print(root) #当前目录路径
        #print(dirs) #当前路径下所有子目录
        #print(files) #当前路径下所有非目录子文件
        for i in files:
            if i.endswith('mp4') or i.endswith('avi'):
                files_path = (root + '\\' + i)
                files_path.replace('\\', '\\\\')
                video = VideoFileClip(files_path)
                audio = video.audio
                to_mp3 = files_path.replace('4','3').replace('avi', 'mp3').replace('videos', 'songs')
                audio.write_audiofile(to_mp3)
                print(files_path)
            else:
                print('error:' + i + '文件格式错误')
                pass
            
file_dir = r'C:\Users\86157\Desktop\moives\videos'

file_name(file_dir)