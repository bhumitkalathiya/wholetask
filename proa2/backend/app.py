from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def fetch_events():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("SELECT name, date, url FROM events")
    events = [{"name": row[0], "date": row[1], "url": row[2]} for row in c.fetchall()]
    conn.close()
    return events

@app.route("/api/events", methods=["GET"])
def get_events():
    return jsonify(fetch_events())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
