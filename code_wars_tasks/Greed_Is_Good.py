# Greed is Good
#
# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
#
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
#
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
#
# Example scoring
#
#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
#
# Note: your solution must not modify the input list.

rules = [
    {"value": 1, "count": 3, "points": 1000},
    {"value":6, "count": 3, "points":600},
    {"value":5, "count": 3, "points":500},
    {"value":4, "count": 3, "points":400},
    {"value":3, "count": 3, "points":300},
    {"value":2, "count": 3, "points":200},
    {"value":1, "count": 1, "points":100},
    {"value":5, "count": 1, "points":50},
]
def score(dice):
    copy_dice = dice[0:]
    points = 0
    points_found = True
    while points_found:
        points_found = False
        for rule in rules:
            if copy_dice.count(rule["value"]) >= rule["count"]:
                for i in range(rule["count"]):
                    copy_dice.remove(rule["value"])
                points += rule["points"]
                points_found = True
    return points
print(score( [1, 1, 1, 3, 1] ))
