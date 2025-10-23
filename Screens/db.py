import sqlite3, os, hashlib

DB_PATH = os.path.join(os.getcwd(), "app.db")

def _hash(pw:str)->str:
    return hashlib.sha256(pw.encode()).hexdigest()

class DB:
    @staticmethod
    def init():
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (u TEXT PRIMARY KEY, p TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS notes (u TEXT, note TEXT)")
        con.commit(); con.close()

    @staticmethod
    def create_user(u, p):
        u, p = u.strip(), p.strip()
        if len(u) < 3 or len(p) < 4:
            return False, "Username(>=3) & Password(>=4)"
        con = sqlite3.connect(DB_PATH); cur = con.cursor()
        try:
            cur.execute("INSERT INTO users(u,p) VALUES(?,?)", (u, _hash(p)))
            con.commit(); ok=True; msg="Account created. Login now."
        except sqlite3.IntegrityError:
            ok=False; msg="User already exists"
        con.close(); return ok, msg

    @staticmethod
    def check_login(u, p):
        con = sqlite3.connect(DB_PATH); cur = con.cursor()
        cur.execute("SELECT 1 FROM users WHERE u=? AND p=?", (u, _hash(p)))
        ok = cur.fetchone() is not None
        con.close(); return ok

    @staticmethod
    def add_note(u, note):
        con = sqlite3.connect(DB_PATH); cur = con.cursor()
        cur.execute("INSERT INTO notes(u,note) VALUES(?,?)", (u, note))
        con.commit(); con.close()

    @staticmethod
    def list_notes(u):
        con = sqlite3.connect(DB_PATH); cur = con.cursor()
        cur.execute("SELECT note FROM notes WHERE u=? ORDER BY rowid DESC", (u,))
        rows = [r[0] for r in cur.fetchall()]
        con.close(); return rows
