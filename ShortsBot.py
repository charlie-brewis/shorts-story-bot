from moviepy.editor import *

# access to video
clip = VideoFileClip("stock-background-videos/test-video.mp4", audio=False)

# downloads video clip
clip.write_videofile("output-video/new-test-video.mp4")