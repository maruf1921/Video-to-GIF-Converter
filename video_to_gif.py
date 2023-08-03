from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

link = askopenfilename()
video = VideoFileClip(link)

name = link.split("/")
for i in name:
    name2 = i.split(".")
print(name2[0])

video.write_gif(name2[0]+".gif", fps=10)