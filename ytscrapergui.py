from ytscraper import *
from tkinter import *
from tkinter import ttk
from os import path

root = Tk()
root.title('YouTube Search Web Scraper')
icon = path.dirname(path.realpath(__file__)) + '\images\icon.ico'
root.iconbitmap(icon)
root.state('zoomed')

table = ttk.Treeview(root)

table['columns'] = ("Channel", "Views", "Date", "Duration", "Likes", "Comments", "Channel Subscribers", "URL")
table.column("#0", anchor = W, width = 600)
table.column("Channel", anchor = CENTER, width = 200)
table.column("Views", anchor = CENTER, width = 100)
table.column("Date", anchor = CENTER, width = 80)
table.column("Duration", anchor = CENTER, width = 80)
table.column("Likes", anchor = CENTER, width = 80)
table.column("Comments", anchor = CENTER, width = 80)
table.column("Channel Subscribers", anchor = CENTER, width = 80)
table.column("URL", anchor = CENTER, width = 350)

table.heading("#0", text = "Title", anchor = CENTER)
table.heading("Channel", text = "Channel", anchor = CENTER)
table.heading("Views", text = "Views", anchor = CENTER)
table.heading("Date", text = "Date", anchor = CENTER)
table.heading("Duration", text = "Duration", anchor = CENTER)
table.heading("Likes", text = "Likes", anchor = CENTER)
table.heading("Comments", text = "Comments", anchor = CENTER)
table.heading("Channel Subscribers", text = "Subscribers", anchor = CENTER)
table.heading("URL", text = "URL", anchor = CENTER)
table.pack(pady = 100)

searchbox = Entry(root, font = 12)
searchbox.place(x = 650, y = 50, width = 450, height = 30)

def search():
    table.delete(*table.get_children())
    array = getData(searchbox.get())
    # The following code allows for sorting by various categories
    #array = sortByViews(array)
    #array = sortByLikes(array)
    #array = sortByComments(array)
    #array = sortBySubs(array)
    count = 0
    for i in array:
        table.insert(parent = '', index = 'end', iid = count, text = i[0], values = (i[1], i[2].split()[0], i[3], i[4], i[5], i[6].split()[0], i[7].split()[0], i[8]))
        count += 1

searchbutton = Button(root, text = "Search", command = search)
searchbutton.place(x = 1110, y = 50, width = 50, height = 30)

root.mainloop()
