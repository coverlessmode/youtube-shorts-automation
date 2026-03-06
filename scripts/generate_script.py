import random

topic=open("output/topic.txt").read()

hooks=[
"You won't believe this...",
"This sounds fake but it's real...",
"Scientists discovered something shocking...",
"This fact will blow your mind..."
]

facts=[
"Octopuses have three hearts.",
"Venus spins backwards.",
"Sharks existed before trees.",
"The ocean is 95% unexplored."
]

script=random.choice(hooks)+" "+random.choice(facts)

with open("output/script.txt","w") as f:
    f.write(script)

print(script)
