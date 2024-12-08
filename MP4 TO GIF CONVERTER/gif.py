from moviepy.editor import VideoFileClip

video = VideoFileClip("video.mp4")

fps = 24
video.write_gif("final.gif", fps=fps)

video.close()