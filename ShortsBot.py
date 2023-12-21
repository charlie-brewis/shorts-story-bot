from moviepy.editor import *
import pyttsx3


#! NEW IDEA: SPLIT SCRIPT INTO LINES AND THEN SEPERATELY TTS EACH LINE
#! THEN WE CAN JUST ALIGN THE CAPTION OF THE LINE CHANGING WITH THE NEXT AUDIO FILE
def convert_script_to_audio(script: str) -> None:
    engine = pyttsx3.init()
    engine.setProperty('rate', 225)
    engine.say(script)
    engine.save_to_file(script, "output-video/test.mp3")
    engine.runAndWait()


def split_script_to_screen_lines(script: str, chars_per_line: int) -> list[str]:
    '''
    Splits the script into a list of lines given how many charachters should be on each line.
    My idea is that each line will be showed on the screen as the tts says said line and then replaced once the tts moves on.
    This is a prototype function to test if the script split could be done this simply.
    '''
    # words_per_second = tts_rate / 51 # Estimated by counting 5 words in 1 second at a rate of 225
    script_words = script.split(" ")
    screen_lines = []
    line = ""
    for word in script_words:
        new_num_chars = len(line) + len(word)
        if new_num_chars <= chars_per_line:
            line += ' ' + word
        # If we get closer to chars_per_line by adding the word to the line anyway, as opposed to not adding the word, add the word
        elif abs(chars_per_line - new_num_chars) < abs(chars_per_line - len(line)):
            line += ' ' + word
        else:
            screen_lines.append(line)
            line = word
    return screen_lines





    



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
    # convert_script_to_audio(plain_text)
    # Guess of 25 chars per line
    script_lines = split_script_to_screen_lines(plain_text, 25)
    # for line in script_lines:
    #     print(f"{len(line)}: {line}")
     
main()