from collections import ChainMap, defaultdict, namedtuple


# CHAINMAP - Combine multiple dicts into one view
# Useful for: Configuration settings, scoped variables, template contexts
user_config = {'theme': 'dark', 'lang': 'en'}
default_config = {'theme': 'light', 'lang': 'en', 'timeout': 30}
config = ChainMap(user_config, default_config)
print(f"Theme: {config['theme']}")  # 'dark' (user overrides default)


# DEFAULTDICT - Dict with default values for missing keys
# Useful for: Grouping data, avoiding KeyError exceptions
groups = defaultdict(list)
for name, age in [('Alice', 25), ('Bob', 30), ('Alice', 26)]:
    groups[name].append(age)
print(dict(groups))  # {'Alice': [25, 26], 'Bob': [30]}


# NAMEDTUPLE - Lightweight class for structured data
# Useful for: Records, coordinates, immutable data structures
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: {p.x}, {p.y}")  # More readable than p[0], p[1]
