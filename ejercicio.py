from tkinter import*
from tkinter import messagebox
interfaz=Tk()

def dividir():
    if divisor.get()==0:
        messagebox.showinfo("Error", f"no se puede dividir dentro de 0")
    else:

        Resto=dividendo.get() % divisor.get()
  
  
        if Resto==0:
            messagebox.showinfo("Correcto", f"la division es exacta")
        else:
            messagebox.showinfo("incorrecto", f"la division es inexacta")
             
interfaz.geometry("500x300+100+100")
interfaz.title("divisor Exacto")

lbltitulo=Label(text="Ejercicio #1").pack()

valor1=Label(text="ingresa el dividendo:").place(x=10,y=40)
dividendo=DoubleVar()
ingreso=Entry(interfaz,textvariable=dividendo).place(x=150,y=45)


valor2=Label(text="ingresa el divisor:").place(x=10,y=70)
divisor=DoubleVar()
ingreso=Entry(interfaz,textvariable=divisor).place(x=150,y=78)

respuesta=Button(interfaz,text="dividir", command=dividir).place(x=10,y=90)


interfaz.mainloop()
