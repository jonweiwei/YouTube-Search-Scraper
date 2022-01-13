from ytscraper import *
from tkinter import *
from tkinter import ttk
from os import path

root = Tk()
root.title('YouTube Search Web Scraper')
icon = path.dirname(path.realpath(__file__)) + '\images\icon.ico'
root.iconbitmap(icon)
root.geometry("900x700")

table = ttk.Treeview(root)

table['columns'] = ("Channel", "Views", "Date", "Duration", "Likes", "Comments", "Channel Subscribers", "URL")
table.column("#0", anchor = W, width = 120)
table.column("Channel", anchor = CENTER, width = 100)
table.column("Views", anchor = CENTER, width = 100)
table.column("Date", anchor = CENTER, width = 80)
table.column("Duration", anchor = CENTER, width = 80)
table.column("Likes", anchor = CENTER, width = 80)
table.column("Comments", anchor = CENTER, width = 80)
table.column("Channel Subscribers", anchor = CENTER, width = 80)
table.column("URL", anchor = E, width = 120)

table.heading("#0", text = "Title", anchor = W)
table.heading("Channel", text = "Channel", anchor = CENTER)
table.heading("Views", text = "Views", anchor = CENTER)
table.heading("Date", text = "Date", anchor = CENTER)
table.heading("Duration", text = "Duration", anchor = CENTER)
table.heading("Likes", text = "Likes", anchor = CENTER)
table.heading("Comments", text = "Comments", anchor = CENTER)
table.heading("Channel Subscribers", text = "Subscribers", anchor = CENTER)
table.heading("URL", text = "URL", anchor = CENTER)

table.pack(pady = 20)

#array = getData('f1')
#for i in range(3):
#    print(array[i])

root.mainloop()
