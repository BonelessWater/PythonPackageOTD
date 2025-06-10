from collections import UserDict, UserList, UserString

# USER CLASSES - Base classes for custom dict/list/string types
# Useful for: Creating specialized containers with custom behavior
class UpperDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)

class EvenList(UserList):
    def append(self, item):
        if item % 2 == 0:
            super().append(item)

class ShoutString(UserString):
    def __add__(self, other):
        return ShoutString(self.data.upper() + str(other).upper())

# Demo the custom classes
ud = UpperDict({'hello': 'world'})
print(dict(ud))  # {'HELLO': 'world'}

el = EvenList([2, 4])
el.append(6)  # Added
el.append(5)  # Ignored (odd)
print(list(el))  # [2, 4, 6]

ss = ShoutString('hello') + ' world'
print(ss)  # HELLO WORLD