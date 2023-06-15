from tkinter import *



root = Tk()
root.title('Minha calculadora')
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)


root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, fg='#ffffff', relief=FLAT, bg='#a7a28f', font=('futura', 25, 'bold'),justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2

)






root.mainloop()