import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox

#Creando la conexion
conexion = pymysql.connect(
    host = 'localhost', 
    user = 'root',
    password = 'edison',
    db = 'al3',
    port = 3334
)

print("Conexion exitosa")

#Empieza codigo tkinter
root = Tk()
root.title("PAGOS")



#Variables
id_pago = StringVar()
id_cliP = StringVar()
f_pago = StringVar()
f_pagado = StringVar()
monto = StringVar()
deuda = StringVar()

#Frame1
frame1=Frame(root)
frame1.pack()
    #Labels
labelId_pago = Label(frame1, text = "ID_PAGO ")    
labelId_pago.grid(row=1, column=1, padx=10, pady=10, sticky='e')
labelId_clip = Label(frame1, text = "ID_CLIENTE ")    
labelId_clip.grid(row=2, column=1, padx=10, pady=10, sticky='e')
labelF_pago = Label(frame1, text = "FECHA DE PAGO ")    
labelF_pago.grid(row=3, column=1, padx=10, pady=10, sticky='e')
labelF_pagado = Label(frame1, text = "PAGADO HASTA ")    
labelF_pagado.grid(row=4, column=1, padx=10, pady=10, sticky='e')
labelMonto = Label(frame1, text = "MONTO ")    
labelMonto.grid(row=5, column=1, padx=10, pady=10, sticky='e')
labelDeuda = Label(frame1, text = "DEUDA ")    
labelDeuda.grid(row=6, column=1, padx=10, pady=10, sticky='e')
    #Cuadros
entryId_pago = Entry(frame1, textvariable=id_pago)    
entryId_pago.grid(row=1, column=2, padx=10, pady=10)
entryId_clip = Entry(frame1, textvariable=id_cliP)    
entryId_clip.grid(row=2, column=2, padx=10, pady=10)
entryF_pago = Entry(frame1, textvariable=f_pago)    
entryF_pago.grid(row=3, column=2, padx=10, pady=10)
entryF_pagado = Entry(frame1, textvariable=f_pagado)    
entryF_pagado.grid(row=4, column=2, padx=10, pady=10)
entryMonto = Entry(frame1, textvariable=monto)    
entryMonto.grid(row=5, column=2, padx=10, pady=10)
entryDeuda = Entry(frame1, textvariable=deuda)    
entryDeuda.grid(row=6, column=2, padx=10, pady=10)

#dando definiciones a los botones
def codCrear():
    datos_pago = id_pago.get(), id_cliP.get(), f_pago.get(), f_pagado.get(), monto.get(), deuda.get()
    #idC=id.get()
    #nomC=nombre.get()
    #edC=edad.get()
    #usuC=usuario.get()
    #conC=contraseña.get()

    curCrear=conexion.cursor()
    curCrear.execute("INSERT INTO ALQUILER VALUES {}".format(datos_pago))
    conexion.commit()
    #conexion.close()
    print("Creado exitosamente")
    limpiar()
    
    
def codLeer():
    curLeer=conexion.cursor()
    curLeer.execute("SELECT ID_AL, ID_CLIENTE, F_PAGO, F_PAGADO, MONTO, DEUDA FROM ALQUILER WHERE ID_AL = '{}';".format(id_pago.get()))
    for ID_AL, ID_CLIENTE, F_PAGO, F_PAGADO, MONTO, DEUDA in curLeer.fetchall():
        print(ID_AL, ID_CLIENTE, F_PAGO, F_PAGADO, MONTO, DEUDA)

        id_pago.set(ID_AL)
        id_cliP.set(ID_CLIENTE)
        f_pago.set(F_PAGO)
        f_pagado.set(F_PAGADO)
        monto.set(MONTO)
        deuda.set(DEUDA)
        #conexion.close()

def codActualizar():
    datosA = [id_cliP.get(), f_pago.get(), f_pagado.get(), monto.get(), deuda.get(), id_pago.get()]
    #idA=id.get()
    #nomA=nombre.get()
    #edA=edad.get()
    #usuA=usuario.get()
    #conA=contraseña.get()

    curActualizar=conexion.cursor()
    #curActualizar.execute("UPDATE PERSONA SET NOMBRE={}, EDAD={}, USUARIO={}, CONTRASENA={} WHERE IDPERSONA={}".format(nomA, edA, usuA, conA, idA))
    curActualizar.execute("UPDATE ALQUILER SET ID_CLIENTE=%s, F_PAGO=%s, F_PAGADO=%s, MONTO=%s, DEUDA=%s WHERE ID_AL=%s", datosA)
    conexion.commit()
    limpiar()
    #conexion.close()
    print("Actualizacion exitosa")

def codEliminar():
    curElim=conexion.cursor()
    curElim.execute("DELETE FROM ALQUILER WHERE ID_AL=%s", id_pago.get())
    conexion.commit()
    limpiar()
    print("Eliminado con exito")

#frame2 (botones)
frame2 = Frame(root)
frame2.pack()
#botones
btnCrear=Button(frame2, text="Crear", cursor="hand2", command=codCrear)
btnCrear.grid(row=1, column=1, padx=10, pady=10)
btnLeer=Button(frame2, text="Leer", cursor="hand2", command=codLeer)
btnLeer.grid(row=1, column=2, padx=10, pady=10)
btnActualizar=Button(frame2, text="Actualizar", cursor="hand2", command=codActualizar)
btnActualizar.grid(row=1, column=3, padx=10, pady=10)
btnEliminar=Button(frame2, text="Eliminar", cursor="hand2", command=codEliminar)
btnEliminar.grid(row=1, column=4, padx=10, pady=10)


#Funciones para el menu var
#limpiar
def limpiar():
    id_pago.set("") 
    id_cliP.set("")
    f_pago.set("") 
    f_pagado.set("")
    monto.set("")
    deuda.set("")
#MENSAJE
def mensaje():
    messagebox.showinfo("Acerca", """ 
    Sistema de Registro de alquileres/ Pagos
    Version 1.0
    Unsando Tkinter y mysql
    Hecho por Edison Velasco Huaman
    """)
#Salir
def salir():
    root.destroy()

#############MENU BAR#################################
menuBar=Menu(root)
#menu1=Menu(menuBar, tearoff=0)
menuBar.add_command(label="Limpiar", command=limpiar)
menuBar.add_command(label="Acerca", command=mensaje)
#menuBar.add_cascade(label="Inicio", menu=menu1)

#menu2=Menu(menuBar, tearoff=0)
#menu2.add_command(label="Salir", command=salir)
menuBar.add_command(label="Salir",command=salir)

root.config(menu=menuBar)

root.mainloop()