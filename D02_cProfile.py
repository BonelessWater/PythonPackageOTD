'''
Day 2, June 5th 2025: 

Welcome to cProfile.py!

A chain is only as strong as its weakest link, and as a developer,
your weakness likely lies somewhere in your code. This library
specializes in snitching on those links so you can revert to 
the teachings of time complexity and memory access patterns.
'''

import cProfile

def slow_func():
    return sum(i**2 for i in range(1000000))

def fast_func():
    return sum(range(10000))

def main():
    for _ in range(10):
        slow_func()
    for _ in range(100):
        fast_func()

if __name__ == "__main__":
    cProfile.run('main()')