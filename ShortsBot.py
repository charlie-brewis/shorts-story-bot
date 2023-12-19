from moviepy.editor import *

# access to video
clip = VideoFileClip("stock-background-videos/.mp4")

# downloads video clip
clip.write_videofile("movie.mp4")