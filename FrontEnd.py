import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import requests
import re

def main():
    main = tk.Tk()
    main.geometry("800x800")
    main.title("Search")
    searchBar = tk.Entry(main, width=50)
    languages = ['English', 'Norwegian', 'Spanish', 'German']
    clicked = tk.StringVar()
    clicked.set( "English" )
    drop = tk.OptionMenu(main,clicked,*languages)

    frame = tk.Frame(main)
    def search():
        nonlocal frame
        frame.destroy()
        frame = tk.Frame()
        labels = ['Positive', 'Negative']
        request = requests.get(f'http://127.0.0.1:8000/Search?term={str(searchBar.get())}&lang={str(clicked.get())}').text
        values = [int(s) for s in re.findall(r'\b\d+\b', request)]
        figure = Figure(figsize=(6,4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, frame)
        NavigationToolbar2Tk(figure_canvas, frame)
        axes = figure.add_subplot()
        axes.bar(labels, values)
        axes.set_title(f'Positive and Negative tweets about {searchBar.get()} in {clicked.get()}')

        frame.pack()
        figure_canvas.get_tk_widget().pack()
        
    
    searchButton = tk.Button(main, text="Search", width=20, command=search)

    searchBar.pack()
    drop.pack()
    searchButton.pack()
    main.mainloop()

main()

