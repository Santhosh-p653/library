from flask import Flask, render_template, request, jsonify
import requests
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE ----------------

def init_db():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT
            )
        ''')
        conn.commit()

init_db()

# ---------------- HOME ROUTE ----------------

@app.route('/')
def home():
    return render_template('index.html')

# ---------------- SEARCH ROUTE ----------------

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify([])

    url = f'https://openlibrary.org/search.json?q={query}'

    try:
        response = requests.get(url)
        data = response.json()
        books = []
        docs = data.get('docs', [])

        for item in docs[:12]:
            title = item.get('title', 'No Title')
            author_list = item.get('author_name', ['Unknown Author'])
            author = author_list[0]
            cover_id = item.get('cover_i')

            if cover_id:
                image = f'https://covers.openlibrary.org/b/id/{cover_id}-M.jpg'
            else:
                image = 'https://via.placeholder.com/200x300?text=No+Cover'

            books.append({
                'title': title,
                'author': author,
                'image': image
            })

        return jsonify(books)

    except Exception as e:
        print("ERROR:", e)
        return jsonify([])

# ---------------- SAVE ROUTE ----------------

@app.route('/save', methods=['POST'])
def save():
    try:
        data = request.json
        title = data.get('title')
        author = data.get('author')

        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO books (title, author) VALUES (?, ?)',
                (title, author)
            )
            conn.commit()

        return jsonify({'message': 'Book Saved Successfully'})

    except Exception as e:
        print("SAVE ERROR:", e)
        return jsonify({'message': 'Error Saving Book'})

# ---------------- SAVED BOOKS ROUTE ----------------

@app.route('/saved')
def saved():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()

    books = []
    for row in rows:
        books.append({
            'id': row[0],
            'title': row[1],
            'author': row[2]
        })

    return render_template('saved.html', books=books)

# ---------------- DELETE ROUTE ----------------

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    try:
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM books WHERE id=?', (id,))
            conn.commit()
        return jsonify({'message': 'Book Deleted Successfully'})
    except Exception as e:
        print("DELETE ERROR:", e)
        return jsonify({'message': 'Error Deleting Book'}), 500

# ---------------- RUN APP ----------------

if __name__ == '__main__':
    app.run(debug=True)