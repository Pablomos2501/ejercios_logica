from tkinter import *
from tkinter import messagebox

interfaz=Tk()

def comparar():
    if num1.get() > num2.get():
        messagebox.showinfo("gg", f"{num1.get()} es mayor que {num2.get()}")
    else:
        messagebox.showinfo("gg", f"{num2.get()} es mayor que {num1.get()}")
        if num1.get() == num2.get():
            messagebox.showinfo("hey",f"estos numeros son iguales")

interfaz.geometry("500x300+100+100")
interfaz.title("comparador de numeros")


lbl1=Label(text="ingrese un numero").place(x=10,y=40)
num1=IntVar()
ingreso=Entry(interfaz,textvariable=num1).place(x=130,y=40)

lbl1=Label(text="ingrese otro numero").place(x=10,y=90)
num2=IntVar()
ingreso=Entry(interfaz,textvariable=num2).place(x=130,y=90)


comparar=Button(interfaz,text="comparar",command=comparar).place(x=10, y=120)


interfaz.mainloop()










"""
num1=int(input("ingrese un numero"))
num2=int(input("ingrese otro numero"))

if num1>num2:
    print(num1,"es el mayor")
else:
    print(num2,"es el mayor")
    if num1==num2:
        print("los numeros son iguales")
"""        