from tkinter import *
from tkinter import messagebox


def comparar():
    diferencia = fecha1.get() - fecha2.get()
    if diferencia == 1:
        messagebox.showinfo("",f"Desde el año {fecha2.get()} ha pasado 1 año.")
    elif diferencia > 1:
        messagebox.showinfo("",f"Desde el año {fecha2.get()} han pasado {fecha1.get()-fecha2.get()} años.")
    elif diferencia == -1:
        messagebox.showinfo("",f"Para llegar al año {fecha2.get()} falta 1 año.")
    elif diferencia < -1:
        messagebox.showinfo("",f"Para llegar al año {fecha2.get()} faltan {fecha2.get()-fecha1.get()} años.")
    else:
        messagebox.showinfo("",f"¡Son el mismo año!")


interfaz=Tk()
interfaz.geometry("500x300+100+100")
interfaz.title("Años")


lbltitulo=Label(text="cuantos años faltan").pack()

valor1=Label(text="ingresa el año actual").place(x=10,y=40)
fecha1=IntVar()
ingreso=Entry(interfaz,textvariable=fecha1).place(x=150,y=45)


valor2=Label(text="ingresa un año cualquiera").place(x=10,y=70)
fecha2=IntVar()
ingreso=Entry(interfaz,textvariable=fecha2).place(x=150,y=78)

respuesta=Button(interfaz,text="comparar", command=comparar).place(x=10,y=90)

interfaz.mainloop()













"""
fecha_1 = int(input("¿En qué año estamos?: "))
fecha_2 = int(input("Escriba un año cualquiera: "))
diferencia = fecha_1 - fecha_2

if diferencia == 1:
    print(f"Desde el año {fecha_2} ha pasado 1 año.")
elif diferencia > 1:
    print(f"Desde el año {fecha_2} han pasado {diferencia} años.")
elif diferencia == -1:
    print(f"Para llegar al año {fecha_2} falta 1 año.")
elif diferencia < -1:
    print(f"Para llegar al año {fecha_2} faltan {-diferencia} años.")
else:
    print("¡Son el mismo año!")
"""