import os

text=open("output/script.txt").read()

cmd=f'echo "{text}" | piper --model en_US-lessac-medium.onnx --output_file output/voice.wav'

os.system(cmd)
