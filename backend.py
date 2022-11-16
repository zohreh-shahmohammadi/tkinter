import sqlite3
def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,auth text,year INTEGER,isbn INTEGER) ")
    conn.commit()
    conn.close()
def insert(title,auth,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,auth,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="",auth="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE  title=? OR auth=? OR year=? OR isbn=?",(title,auth,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id,title,auth,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,auth=? ,year=?,isbn=? WHERE id=?", (title,auth,year,isbn,id))
    conn.commit()
    conn.close()
connect()
#insert("python ebook","zahra",215,2565)
#delete(5)
#update(1,"new book title","new author name",2020,564565)
print(search(auth="sara"))