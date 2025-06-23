from python_ds.data_structures.stack import Stack
from python_ds.data_structures.linked_list import LinkedList
from python_ds.data_structures.binary_search_tree import BinarySearchTree
from python_ds.algorithms.sorting.bubble_sort import bubble_sort

s = Stack()
s.push(10)
s.push(20)
print(s.pop())          # 20

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.traverse()           # prints 1 2

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
print(bst.search(3))    # True

arr = [3,1,2]
print(bubble_sort(arr)) # [1, 2, 3]

s.push(30)
print(s.peek())         # 30
