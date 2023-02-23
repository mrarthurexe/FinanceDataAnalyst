import tkinter
import customtkinter
from tkinter import Text

from SQL.CrudDollar import insertDollar
from Analysis.DollarAnalysis import plotDollarGraph, getDollarAverage

root_tk = tkinter.Tk()
root_tk.geometry("550x150")
root_tk.title("Finance")
customtkinter.set_appearance_mode("dark")

text = tkinter.Text(root_tk)

# Initializing the buttons
dollar_text = tkinter.Label(master=root_tk, text="Dollar:")
dollar_search = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='New Search', command=insertDollar)
dollar_average = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='Average', command=getDollarAverage)
dollar_graph = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='Plot Graph', command=plotDollarGraph)
euro_text = tkinter.Label(master=root_tk, text="Euro:")
euro_search = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='New Search')
euro_average = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='Average')
euro_graph = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='Plot Graph')


# Dollar
dollar_text.grid(row=0, column=0)
dollar_search.grid(row=0, column=1, padx=10, pady=10)
dollar_average.grid(row=0, column=2, padx=10, pady=10)
dollar_graph.grid(row=0, column=3, padx=10, pady=10)

#Euro
euro_text.grid(row=1, column=0)
euro_search.grid(row=1, column=1, padx=10, pady=10)
euro_average.grid(row=1, column=2, padx=10, pady=10)
euro_graph.grid(row=1, column=3, padx=10, pady=10)

root_tk.mainloop()