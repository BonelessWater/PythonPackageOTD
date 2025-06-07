from collections import deque, Counter

# DEQUE - Double-ended queue (efficient at both ends)
# Useful for: Sliding windows, breadth-first search, undo operations
dq = deque([1, 2, 3], maxlen=3)
dq.appendleft(0)  # [0, 1, 2] (3 falls off the right)
dq.append(4)      # [1, 2, 4] (0 falls off the left)
print(list(dq))

# COUNTER - Count hashable objects
# Useful for: Frequency analysis, statistics, finding most common items
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(f"Most common: {counter.most_common(1)}")  # [('apple', 3)]



