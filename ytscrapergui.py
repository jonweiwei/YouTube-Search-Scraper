from ytscraper import *
from tkinter import *
from tkinter import ttk
from os import path

root = Tk()
root.title('YouTube Search Web Scraper')
icon = path.dirname(path.realpath(__file__)) + '\images\icon.ico'
root.iconbitmap(icon)

#array = getData('f1')
#array = sortByViews(array)
#for i in range(3):
#    print(array[i])

root.mainloop()
