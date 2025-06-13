import heapq

# Priority queue for task scheduling
tasks = [(3, 'low priority'), (1, 'urgent'), (2, 'medium')]
heapq.heapify(tasks)

# Process tasks by priority
while tasks:
   priority, task = heapq.heappop(tasks)
   print(f"Processing: {task}")

# Find 3 largest numbers efficiently
numbers = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
top_3 = heapq.nlargest(3, numbers)
print(f"Top 3: {top_3}")

# Merge multiple sorted iterables
merged = list(heapq.merge([1, 3, 5], [2, 4, 6], [0, 7, 8]))
print(f"Merged: {merged}")