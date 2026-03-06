import random
import os

# Make sure the folder exists
os.makedirs("output", exist_ok=True)

topics = [
    "space mysteries",
    "psychology tricks",
    "AI facts",
    "ancient civilizations",
    "deep ocean creatures"
]

topic = random.choice(topics)

with open("output/topic.txt", "w") as f:
    f.write(topic)

print(topic)
