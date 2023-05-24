import re
from time import time
from sortedcontainers import SortedList
s=input()
start = time()
indexes = {}
for x in set(s):
    indexes.setdefault(x, SortedList([_.start() for _ in re.finditer(x, s)] + [len(s)]))

left, right = 0, max(min(x) for x in indexes.values())
current_min = right - left + 1
while right < len(s) - 1:
    next_pos = next(indexes.get(s[left:left + 1]).irange(left, inclusive=(False, True)))
    right = max(right, next_pos)
    left += 1
    current_min = min(current_min, right - left + 1)
print(current_min)