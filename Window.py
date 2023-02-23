import tkinter
import customtkinter


from SQL.CrudDollar import insertDollar
from Analysis.DollarAnalysis import plotGraph, getAverage

root_tk = tkinter.Tk()
root_tk.geometry("480x80")
root_tk.title("Finance")
customtkinter.set_appearance_mode("Dark")

search_button = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='New Search', command=insertDollar)
average_button = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='Average', command=getAverage)
graph_button = customtkinter.CTkButton(master=root_tk, corner_radius=10, text='Plot Graph', command=plotGraph)

search_button.grid(row=0, column=0, padx=10, pady=10)
average_button.grid(row=0, column=1, padx=10, pady=10)
graph_button.grid(row=0, column=2, padx=10, pady=10)

root_tk.mainloop()