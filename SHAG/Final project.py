from tkinter import messagebox
import sqlite3
from tkinter import *

def connect_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL);
    ''')
    return conn, cursor

def register(conn, cursor, username, password):
    try:
        cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?);
        ''', (username, password))
        conn.commit()
        messagebox.showinfo("Registration", "Registration was successful")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "User with this name already exists")

def login(cursor, username, password):
    cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?;
    ''', (username, password))
    data = cursor.fetchone()
    if data:
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid username or password")

def main():
    conn, cursor = connect_db()

    window = Tk()
    window.title("Registration and login")

    username_label = Label(window, text="Username")
    username_label.pack()
    username_entry = Entry(window)
    username_entry.pack()

    password_label = Label(window, text="Password.")
    password_label.pack()
    password_entry = Entry(window, show="*")
    password_entry.pack()

    def do_register():
        register(conn, cursor, username_entry.get(), password_entry.get())

    def do_login():
        login(cursor, username_entry.get(), password_entry.get())

    register_button = Button(window, text="Registration", command=do_register)
    register_button.pack()

    login_button = Button(window, text="Login", command=do_login)
    login_button.pack()

    window.mainloop()

if __name__ == '__main__':
    main()