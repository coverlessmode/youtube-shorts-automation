import requests

url="https://videos.pexels.com/video-files/3195394/3195394-hd_1080_1920_25fps.mp4"

r=requests.get(url)

with open("output/background.mp4","wb") as f:
    f.write(r.content)
