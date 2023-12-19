from moviepy.editor import *
from openai import OpenAI
import os


def convert_script_to_audio(script: str) -> None:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    response = client.audio.speech.create(
        model="tts-1",
        voice="Onyx",
        input=script
    )
    response.stream_to_file("test.mp3")
    



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