import random


MIN_NUM = 1
MAX_NUM = 45
NUM_PER_LINE = 6

# get users input
num_quick_picks = int(input("How many quick picks? "))

for _ in range(num_quick_picks):
    quick_pick = []
    while len(quick_pick) < NUM_PER_LINE:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num not in quick_pick:
            quick_pick.append(num)
    quick_pick.sort()

    print(" ".join(f"{num:2}" for num in quick_pick))