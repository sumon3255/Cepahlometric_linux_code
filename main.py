import os, cv2, random, shutil
from random import sample
import numpy as np

from FIxNumbeOfFrame import *
# Source path
source = r"H:\Conferernce setup\Dataset\Cobineresized"
# Destination path
dest = r"H:\Conferernce setup\Codes\Main_code\datasetraw"

# setting the total number of frames will be available in the converted video
sequence_number= 30


for root,_,files in os.walk(source):
    if files:
        for file in files:
            # Finding the class name
            class_name = root.split(os.sep)[-1:]

            # destination file path
            dest_folder_path = os.path.join(dest, *class_name)
            # checking if the destination folder exists
            if not os.path.exists(dest_folder_path):
                os.makedirs(dest_folder_path)

            # file path
            file_path=os.path.join(root,  file)

            # destination file path
            dest_file_path = os.path.join(dest_folder_path, file.split('.')[0]+'.avi')

            # Capturing the video from file path
            video_cap = cv2.VideoCapture(file_path)
            # finding the fps to keep the fps same in the converted  video
            fps = int(video_cap.get(cv2.CAP_PROP_FPS))
            # counting the total number of frames in the video
            frame_number = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # check if the video has more frames than our required number
            if sequence_number < frame_number:
                # print('DownSampling ', frame_number, ' to ', sequence_number)
                frame_DownSample(video_cap, fps, frame_number, sequence_number, dest_file_path)
            # check if the video has less number of video than our required number
            elif sequence_number > frame_number:
                # print('UpSampling', frame_number, ' to ', sequence_number)
                # print('Destination: ', dest_file_path)
                upSample(video_cap, fps, frame_number, sequence_number, dest_file_path)

            else:
                upSample(video_cap, fps, frame_number, sequence_number, dest_file_path)
            # check  the converted video is actually having the required number of frames
            if os.path.exists(dest_file_path):
                cap = cv2.VideoCapture(dest_file_path)
                dest_frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                if dest_frame_number!=sequence_number:
                    print('Conversion problem: ', dest_file_path)
                if dest_frame_number>=frame_number:
                    print(f'Upsample {frame_number} to {dest_frame_number}')
                elif dest_frame_number<=frame_number:
                    print(f'Downsample {frame_number} to {dest_frame_number}')

                cap.release()
                del frame_number