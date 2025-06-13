import sqlite3

# 1) Connect and enable dict-like rows
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# 2) Create table & insert data
cur.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
cur.executemany('INSERT INTO users(name,email) VALUES(?,?)',
                [('Alice','alice@example.com'), ('Bob','bob@mail.com')])
conn.commit()

# 3) Read before changes
print('Before:', [dict(r) for r in cur.execute('SELECT * FROM users')])

# 4) Update & delete
cur.execute('UPDATE users SET email=? WHERE name=?',
            ('alice@newdomain.com','Alice'))
cur.execute('DELETE FROM users WHERE name=?', ('Bob',))
conn.commit()

# 5) Read after changes
print('After: ', [dict(r) for r in cur.execute('SELECT * FROM users')])

# 6) Clean up
conn.close()
