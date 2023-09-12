from tkinter import *
from tkinter import Tk, ttk

#Cores 
co0 = "#2e2d2b"  
co1 = "#feffff"  
co2 = "#4fa882"  
co3 = "#38576b"  
co4 = "#403d3d"   
co5 = "#e06636"   
co6 = "#038cfc"   
co7 = "#3fbfb9"   
co8 = "#263238"   
co9 = "#e9edf5"

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

window = Tk()
window.title('Orçamento Pessoal')
window.geometry('900x650')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

style=ttk.Style(window)
style.theme_use("clam")

# divisão de frames na tela

frameUp = Frame(window, width=1043, height=50, bg=co1, relief="flat")
frameUp.grid(row=0, column=0)

frameHalf = Frame(window, width=1043, height=361, bg=co1, pady=20, relief="raised")
frameHalf.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameDown = Frame(window, width=1043, height=300, bg=co1, relief="flat")
frameDown.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)




window.mainloop()