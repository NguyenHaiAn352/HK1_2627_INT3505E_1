import sqlite3

books_data = [
    {"id": 1, "name": "The Silent Code", "author": "Lena Hart"},
    {"id": 2, "name": "Echoes of Tomorrow", "author": "Marcus Vail"},
    {"id": 3, "name": "Whispers in the Library", "author": "Nora Finch"},
    {"id": 4, "name": "Beyond the Horizon", "author": "Ethan Cole"},
    {"id": 5, "name": "Fragments of Light", "author": "Clara Wynn"},
    {"id": 6, "name": "The Quantum Garden", "author": "Julian Frost"},
    {"id": 7, "name": "Dreams of Steel", "author": "Sophie Lang"},
    {"id": 8, "name": "The Forgotten Algorithm", "author": "Adrian Blake"},
    {"id": 9, "name": "Voices of the Deep", "author": "Tessa Monroe"},
    {"id": 10, "name": "Chronicles of Ember", "author": "Gavin Rhodes"},
    {"id": 11, "name": "The Infinite Path", "author": "Isla Trent"},
    {"id": 12, "name": "Shadows of the Mind", "author": "Caleb Stone"},
    {"id": 13, "name": "The Last Equation", "author": "Maya Cross"},
    {"id": 14, "name": "A Symphony of Stars", "author": "Leo Grant"},
    {"id": 15, "name": "The Glass Horizon", "author": "Elena Pierce"},
    {"id": 16, "name": "Echo Chamber", "author": "Dylan Shaw"},
    {"id": 17, "name": "The Binary Heart", "author": "Riley Quinn"},
    {"id": 18, "name": "Threads of Reality", "author": "Harper Lee"},
    {"id": 19, "name": "The Crimson Archive", "author": "Owen Hale"},
    {"id": 20, "name": "Winds of Eternity", "author": "Ivy Brooks"},
    {"id": 21, "name": "Python of the Wild", "author": "Noah Reed"}
]

con = sqlite3.connect("books.db")
cur = con.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                author TEXT NOT NULL)""")

cur.executemany(
    "INSERT OR REPLACE INTO books (id, name, author) VALUES (:id, :name, :author)", books_data
)

cur.execute("SELECT * FROM books")
print(cur.fetchall())
con.commit()
con.close()