import sqlite3 as sql
import tkinter
from tkinter import ttk

#create a connection to connect to a database
connection = sql.connect("gym.db")
#create a cursor to connect to schema
cursor = connection.cursor()
# open the schema file
with open("schema.sql", "r") as file:
    sql_script = file.read()
# execute all SQL commands inside schema.sql
cursor.executescript(sql_script)
# save changes
connection.commit()
# close connection
connection.close()

#create the pop-up window
window = tkinter.Tk()
#sets the size of the popup window and the position of the window
# geometry(width x height (+-)x (+-)y)
window.geometry("1600x1400+50+50")
#create a title
window.title("Workout Tracker Demo")
#create a message widget
message = tkinter.Label(window, text="Workout Tracker",font=("Segoe UI", 50))
#display text
message.pack()
window.iconbitmap('./dumbell_image.ico')

# keep the window displaying
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    window.mainloop()#keep as last command to keep the tk window open