from ytscraper import *
from tkinter import *
from tkinter import ttk
from os import path

root = Tk()
root.title('YouTube Search Web Scraper')
icon = path.dirname(path.realpath(__file__)) + '\images\icon.ico'
root.iconbitmap(icon)
root.geometry("800x600")

table = ttk.Treeview(root)

table['columns'] = ("Title", "Channel", "Views", "Date", "Duration", "Comments", "Channel Subscribers", "URL")
table.column("#0", width = 0)

#array = getData('f1')
#array = sortByViews(array)
#for i in range(3):
#    print(array[i])

root.mainloop()
