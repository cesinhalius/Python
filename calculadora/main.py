from tkinter import *


root = Tk()
root.title('Minha calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)


numero1 = ''
divisao = FALSE
multiplica = FALSE
adicao = FALSE
subtracao = FALSE


root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, fg='#ffffff', relief=FLAT,
          bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2

)

# Função operedores


def botao_click(num):
    e.insert(END, num)


def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0,END)

def botao_adiciona():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0,END)
def botao_subtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0,END)
def botao_igual():
    return
def botao_limpa():
    return

divide = Button(root,
                text='/',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
divide.grid(row=0, column=4)
#primeira fileira

um = Button(root,
                text='1',
                padx=40,
                pady=20,
                command=lambda:botao_click(1),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
um.grid(row=1, column=1)

dois = Button(root,
                text='2',
                padx=40,
                pady=20,
                command=lambda:botao_click(2),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
dois.grid(row=1, column=2)

tres = Button(root,
                text='3',
                padx=40,
                pady=20,
                command=lambda:botao_click(3),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
tres.grid(row=1, column=3)

multiplica = Button(root,
                text='*',
                padx=40,
                pady=20,
                command=botao_multiplica,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
multiplica.grid(row=1, column=4)
#segunda fileira

quatro = Button(root,
                text='4',
                padx=40,
                pady=20,
                command=lambda:botao_click(4),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)

cinco = Button(root,
                text='5',
                padx=40,
                pady=20,
                command=lambda:botao_click(5),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)

seis = Button(root,
                text='6',
                padx=40,
                pady=20,
                command=lambda:botao_click(6),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
seis.grid(row=2, column=3)

adicao = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_adiciona,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
adicao.grid(row=2, column=4)
#terceira fileira

sete = Button(root,
                text='7',
                padx=40,
                pady=20,
                command=lambda:botao_click(7),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
sete.grid(row=3, column=1)

oito = Button(root,
                text='8',
                padx=40,
                pady=20,
                command=lambda:botao_click(8),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
oito.grid(row=3, column=2)

nove = Button(root,
                text='9',
                padx=40,
                pady=20,
                command=lambda:botao_click(9),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
nove.grid(row=3, column=3)

subtracao = Button(root,
                text='-',
                padx=41,
                pady=20,
                command=botao_subtracao,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
subtracao.grid(row=3, column=4)

# quarta fileira
zero = Button(root,
                text='0',
                padx=91,
                pady=20,
                command=lambda:botao_click(0),
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
zero.grid(row=4, column=1, columnspan=2)

limpa = Button(root,
                text='C',
                padx=40,
                pady=20,
                command=botao_limpa,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
limpa.grid(row=4, column=4)

igual = Button(root,
                text='=',
                padx=40,
                pady=20,
                command=botao_igual,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
igual.grid(row=4, column=3)

root.mainloop()