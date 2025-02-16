import sqlite3

# Connect to SQLite database (creates 'events.db' if not exists)
conn = sqlite3.connect("events.db")
c = conn.cursor()

# Create 'events' table
c.execute('''CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                url TEXT NOT NULL
            )''')

# Insert sample events
event_data = [
    ("Music Concert", "2025-02-20 18:00:00", "https://eventsite.com/concert"),
    ("Tech Conference", "2025-03-05 10:00:00", "https://eventsite.com/tech"),
    ("Startup Meetup", "2025-03-15 14:00:00", "https://eventsite.com/startup")
]

c.executemany("INSERT INTO events (name, date, url) VALUES (?, ?, ?)", event_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("✅ Database 'events.db' created with sample events!")
