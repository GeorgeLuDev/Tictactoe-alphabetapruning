from collections import OrderedDict
import json
import random

moves = json.load(open("policy.txt"))

sortedmoves = OrderedDict(sorted(moves.items()))

with open("actualResult.txt","w") as f:
    for key,item in sortedmoves.items():
        f.write('%s%d\n' % (key,item))

# json.dump(sortedmoves,open("sortedpolicy.txt","w"))