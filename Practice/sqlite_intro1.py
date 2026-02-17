import sqlite3

# Connect to a database file (or create one)
conn = sqlite3.connect("test.db")

# create a cursor object

cur = conn.cursor()

# create a table

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
)
            """)

# Insert data

cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John", 42))

# save (commit) changes
conn.commit()

# Query data
cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print(row)

# Close the connection
conn.close()