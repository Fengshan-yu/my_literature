# This is to manage my literature

import sqlite3
import tkinter as tk
from tkinter import messagebox


class LiteratureDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("literature.db")
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS literature (
                        author TEXT,
                        title TEXT,
                        journal TEXT,
                        year TEXT,
                        comment TEXT,
                        topic TEXT);''')

    def add_literature(self):
        author = input("Please enter the name of authors: ")
        title = input("Literature title please: ")
        journal = input("Please enter the journal:")
        year = input("Enter the date")
        comment = input("Please enter the major comment:")
        topic = input("Enter the related topic:")

        self.c.execute("INSERT INTO literature (author, title, journal, year, comment, topic) VALUES (?,?,?,?,?,?)",
                       (author, title, journal, year, comment, topic))
        self.conn.commit()
        tk.messagebox.showinfo("", "New literature added!")

    def delete_literature(self):
        column = input("Select the column to enter text: ")
        text = input("Enter the text: ")

        self.c.execute(f"DELETE FROM literature WHERE {area}=?", (f"{text}",))
        self.conn.commit()
        tk.messagebox.showinfo("", "The literature was deleted!")

    def show_literature(self):
        self.c.execute('SELECT * FROM literature')
        rows = self.c.fetchall()
        for row in rows:
            print(row[0])
            print(row[1])
            print(row[2], end=", ")
            print(row[3])
            print()
        tk.messagebox.showinfo("", "Here is the database!")

    def update_literature(self):
        column1 = input("Select the column to identify the literature (author, title,journal, year, comment, topic): ")
        text1 = input("Enter the text to identify the literature: ")
        column2 = input("Select the column to be updated (author, title,journal, year, comment, topic): ")
        text2 = input("Enter the text to update: ")

        self.c.execute(f"UPDATE literature SET {column2} = ? WHERE {column1} = ?", (f"{text2}", f"{text1}"))
        self.conn.commit()
        tk.messagebox.showinfo("", "The literature was updated!")

my_literature = LiteratureDatabase()

def click1():
    return my_literature.show_literature()

def click2():
    return my_literature.add_literature()

def click3():
    return my_literature.delete_literature()

def click4():
    return my_literature.update_literature()

def click5():
    window.destroy()

window = tk.Tk()
window.title("Literature")
window.geometry("200x200")
window.resizable(width=True, height=True)
button1 = tk.Button(window, text="Show Database", command=click1)
button2 = tk.Button(window, text="Add Literature", command=click2)
button3 = tk.Button(window, text="Delete Literature", command=click3)
button4 = tk.Button(window, text="Update Literature", command=click4)
button5 = tk.Button(window, text="Exit", command=click5)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
window.mainloop()