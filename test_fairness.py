import random
from rock_paper_scissors import CHOICES, decide_winner

scores = {"player": 0, "computer": 0, "tie": 0}
for _ in range(10000):
    result = decide_winner(random.choice(CHOICES), random.choice(CHOICES))
    scores[result] += 1

print(scores)