from Match import *
from Agents import *


match = Match(Joss_Agent(),TFT_Agent())

for i in range(201):
    print("round",i)
    print(f"score 1: {match.score1}")
    print(f"score 2: {match.score2}")
    print("")
    match.round()