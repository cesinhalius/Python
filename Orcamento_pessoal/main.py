from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk

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


app_img = Image.open("img/icons8-person.png")
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameUp, image=app_img, text='Orçamento Pessoal', width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)


frame_renda = Frame(frameDown, width=300, height=250, bg=co1)
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frameDown, width=220, height=250, bg=co1)
frame_operacoes.grid(row=0, column=1,padx=5)

frame_configuracao = Frame(frameDown, width=220, height=250, bg=co1)
frame_configuracao.grid(row=0, column=2,padx=5)

app_tabela = Label(frameHalf, text='Tabela Receitas e Desespesas', anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
app_tabela.place(x=5, y=309)


def Tabela_Renda():
    tabela_head = ['ID', 'Categoria', 'Data', 'Valor']

    list_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]

    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended", columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd =["center","center","center","center"]
    h = [30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col,width=h[n],anchor=hd[n])

        n+=1

    for item in list_itens:
        tree.insert('', 'end', values=item)    

Tabela_Renda()

window.mainloop()