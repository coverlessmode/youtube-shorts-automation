import random

topics = [
"space mysteries",
"psychology tricks",
"AI facts",
"ancient civilizations",
"deep ocean creatures"
]

topic = random.choice(topics)

with open("output/topic.txt","w") as f:
    f.write(topic)

print(topic)
