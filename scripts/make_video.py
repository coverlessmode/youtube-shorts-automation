import os

cmd="""
ffmpeg -i output/background.mp4 \
-i output/voice.wav \
-vf "scale=1080:1920,subtitles=output/subtitles.srt" \
-shortest output/video.mp4
"""

os.system(cmd)
