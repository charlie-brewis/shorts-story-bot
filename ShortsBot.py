from moviepy.editor import *


def convert_script_to_audio(script: str) -> None:
    
    



def generate_background_video() -> None:
    # file location for background video
    clip = VideoFileClip("stock-background-videos/test-video.mp4", audio=False)
    
    
    start = 0
    # cuts video from 1st paramter to second paramter (in seconds)
    clip = clip.subclip(start, start + 60)
    
    # choose where to download output video
    clip.write_videofile("output-video/new-test-video.mp4")


def main() -> None:
    plain_text = input("Enter script: ")
    convert_script_to_audio(plain_text)
    print("E")
     
main()