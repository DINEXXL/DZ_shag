import sqlite3
from tkinter import *
from tkinter import messagebox

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
        messagebox.showinfo("Реєстрація", "Реєстрація пройшла успішно")
    except sqlite3.IntegrityError:
        messagebox.showerror("Помилка", "Користувач з таким ім'ям вже існує")

def login(cursor, username, password):
    cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?;
    ''', (username, password))
    data = cursor.fetchone()
    if data:
        messagebox.showinfo("Вхід", "Вхід виконано успішно")
    else:
        messagebox.showerror("Помилка", "Неправильне ім'я користувача або пароль")

def main():
    conn, cursor = connect_db()

    window = Tk()
    window.title("Реєстрація та вхід")

    username_label = Label(window, text="Ім'я користувача")
    username_label.pack()
    username_entry = Entry(window)
    username_entry.pack()

    password_label = Label(window, text="Пароль")
    password_label.pack()
    password_entry = Entry(window, show="*")
    password_entry.pack()

    def do_register():
        register(conn, cursor, username_entry.get(), password_entry.get())

    def do_login():
        login(cursor, username_entry.get(), password_entry.get())

    register_button = Button(window, text="Реєстрація", command=do_register)
    register_button.pack()

    login_button = Button(window, text="Вхід", command=do_login)
    login_button.pack()

    window.mainloop()

if __name__ == '__main__':
    main()