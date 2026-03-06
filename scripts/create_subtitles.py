text=open("output/script.txt").read()

subtitle=f"""1
00:00:00,000 --> 00:00:10,000
{text}
"""

open("output/subtitles.srt","w").write(subtitle)
