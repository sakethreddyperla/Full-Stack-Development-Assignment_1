from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite database initialization
conn = sqlite3.connect('candidates.db')
cursor = conn.cursor()

# Create candidates table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                status TEXT,
                feedback TEXT,
                rating INTEGER
                )''')
conn.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/candidates', methods=['GET', 'POST', 'DELETE'])
def candidates():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM candidates")
        candidates_data = cursor.fetchall()
        return jsonify(candidates_data)

    elif request.method == 'POST':
        candidate_data = request.get_json()
        cursor.execute("INSERT INTO candidates (name, status, feedback, rating) VALUES (?, ?, ?, ?)",
                       (candidate_data['name'], candidate_data['status'], candidate_data['feedback'], candidate_data['rating']))
        conn.commit()
        return jsonify({"message": "Candidate added successfully"})

    elif request.method == 'DELETE':
        candidate_id = request.args.get('id')
        cursor.execute("DELETE FROM candidates WHERE id=?", (candidate_id,))
        conn.commit()
        return jsonify({"message": "Candidate deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
