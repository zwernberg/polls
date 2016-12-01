import random

def GenerateSlug():
    colors = ['red', 'blue', 'white', 'yellow', 'green', 'black', 'orange']
    numbers = ['1','2','3','4','5','6','7','8','9']
    words = ['monkey', 'cow', 'chicken', 'bull', 'moose','hawk', 'lion', 'rat', 'dog', 'cat']
    return random.choice(colors) + random.choice(numbers) + random.choice(words)