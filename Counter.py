from collections import Counter

text = 'the quick brown fox jumps over the lazy dog'

counter = Counter(text.split())

print(counter) #Counter({'the': 2, 'over': 1, 'quick': 1, 'fox': 1, 'brown': 1, 'dog': 1, 'jumps': 1, 'lazy': 1})
