#!/usr/bin/env python3



#mp4 to mp3 convertion

from moviepy.editor import * 

import shutil   
import argparse


parser=argparse.ArgumentParser(description="makes mp3 from mp4 files ")
parser.add_argument("video_file",help="add video file to make mp3",type=str)
args=parser.parse_args()


filename=args.video_file


def mp4_to_mp3(video_name):

    video_path=f"./v/{video_name}"

    mp3_path=f"./audios/{video_name}.mp3"


    mp4_without_frames = AudioFileClip(video_path)     
    mp4_without_frames.write_audiofile(mp3_path)     
    mp4_without_frames.close()
    
mp4_to_mp3(filename)    
    
