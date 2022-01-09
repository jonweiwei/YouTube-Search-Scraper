from ytscraper import *
from tkinter import *

root = Tk()

array = getData()
array = sortBySubsReverse(array)
for i in range(3):
    print(array[i])