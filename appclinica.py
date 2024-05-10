from tkinter import *

#import tkinter as tk 




import sqlite3
from tkinter import messagebox

root=Tk()
#root=tk.Tk()
root.title("Clinica")


barraMenu=Menu(root)
root.config(menu=barraMenu,width=1200,height=600)




#******variables****************
miid=StringVar()
midoc=StringVar()
minombre=StringVar()
miapellido=StringVar()
midireccion=StringVar()
misexo=StringVar()
miedad=StringVar()
miobrasocial=StringVar()


# ++++++Funciones+++++++++

def conexionbasedatos():
    
     miConexion=sqlite3.connect("usuarios.db")
     miCursor=miConexion.cursor()
     try:  

          miCursor.execute (''' 
            CREATE TABLE DATOSUSUARIOS(ID INTEGER PRIMARY KEY 
            AUTOINCREMENT,DOCUMENTO INTEGER(10) UNIQUE,NOMBRE VARCHAR(50),APELLIDO VARCHAR(50),DIRECCION VARCHAR(50),OBRASOCIAL VARCHAR(50),SEXO VARCHAR(30),EDAD INTEGER(2))''' )
                         
          messagebox.showinfo("Base Datos creada con exito")
     except:
          messagebox.showwarning("Atencion","Base Datos ya creada")

     #miConexion.commit()
        
    # miConexion.close()



def borrardatos():
  miid.set("")
  midoc.set("")
  minombre.set("")
  miapellido.set("")
  miedad.set("")
  midireccion.set("")
  misexo.set("")
  miobrasocial.set("")

def crear():

    miConexion=sqlite3.connect("usuarios.db")

    miCursor=miConexion.cursor()

#miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (‘"+midoc.get()+"‘,‘"+minombre.get() +"‘,‘"+miapellido.get()+"´,´" +midireccion.get()+"´,´"+misexo.get()+"´,´" 
   # ‘"+miedad.get() +"´,´"+miobrasocial.get() +"´)") 
    miCursor.execute("INSERT INTO DATOSUSUARIOS(DOCUMENTO,NOMBRE,APELLIDO,SEXO,EDAD,DIRECCION,OBRASOCIAL)VALUES(?,?,?,?,?,?,?)",(midoc.get(),minombre.get(),miapellido.get(),misexo.get(),miedad.get(),midireccion.get(),miobrasocial.get()))

    miConexion.commit

    messagebox.showinfo("usuarios","registro insertado con exito")
          


def carga():
    
      
     miframe1=Frame(root)
     root.title("Ingreso PacienteS")
     miframe1.pack() 

     #miframe1=tk.Toplevel()
     #miframe1.title=("ingreso pacientes")
     #miframe1.geometry("1000x600")
     
     #*****Botones********
         
     botonborrar=Button(miframe1,text="Borrar",command=borrardatos)
     botonborrar.grid(row=9,column=0,sticky="e",padx=10,pady=10)

     botoncrear=Button(miframe1,text="Grabar",command=crear) 
     botoncrear.grid( row=9,column=2,sticky="e",padx=10,pady=10)

     botonsalir=Button(miframe1,text="Salir",command=root)
     botonsalir.grid(row=9,column=1,sticky="e",padx=10,pady=10)



     #midoc=StringVar()
     #minombre=StringVar()
     #miapellido=StringVar()
     #midireccion=StringVar()
     #misexo=StringVar()
     #miedad=StringVar()
     #miobrasocial=StringVar()

     Id=Entry(miframe1,textvariable=miid)
     Id.grid(row=1,column=1)
     IdLabel=Label(miframe1,text="Id")
     IdLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)




     documento=Entry(miframe1,textvariable=midoc)
     documento.grid(row=2,column=1)
     documentoLabel=Label(miframe1,text="Documento")
     documentoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)


     nombre=Entry(miframe1,textvariable=minombre)
     nombre.grid(row=3,column=1)
     nombreLabel=Label(miframe1,text="Nombre")
     nombreLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

      

     apellido=Entry(miframe1,textvariable=miapellido)
     apellido.grid(row=4,column=1)
     apellidoLabel=Label(miframe1,text="Apellido")
     apellidoLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

     sexo=Entry(miframe1,textvariable=misexo)
     sexo.grid(row=5,column=1)
     sexoLabel=Label(miframe1,text="Sexo")
     sexoLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

     edad=Entry(miframe1,textvariable=miedad)
     edad.grid(row=6,column=1)
     edadLabel=Label(miframe1,text="Edad")
     edadLabel.grid(row=6,column=0,sticky="e",padx=10,pady=10)


     direccion=Entry(miframe1,textvariable=midireccion)
     direccion.grid(row=7,column=1)
     direccionLabel=Label(miframe1,text="Direccion")
     direccionLabel.grid(row=7,column=0,sticky="e",padx=10,pady=10)
     

     obrasocial=Entry(miframe1,textvariable=miobrasocial)
     obrasocial.grid(row=8,column=1)
     obrasocialLabel=Label(miframe1,text="Obra social")
     obrasocialLabel.grid(row=8,column=0,sticky="e",padx=10,pady=10)


     
     
# creear menu en cascada
menu_pacientes=Menu(barraMenu,tearoff=0)
menu_medicos=Menu(barraMenu,tearoff=0)
menu_turnos=Menu(barraMenu,tearoff=0)
menu_base=Menu(barraMenu,tearoff=0)
menu_borrar=Menu(barraMenu,tearoff=0)
menu_salir=Menu(barraMenu,tearoff=0)
#crear agregar opciones
barraMenu.add_cascade(label="pacientes",menu=menu_pacientes)
barraMenu.add_cascade(label="medicos",menu=menu_medicos)
barraMenu.add_cascade(label="Turnos",menu=menu_turnos)
barraMenu.add_cascade(label="Base de Datos",menu=menu_base)
barraMenu.add_cascade(label="Borrar datos",menu=menu_borrar)
barraMenu.add_cascade(label="Salir",menu=menu_salir)

#crear subopciones
menu_pacientes.add_command(label="carga de Pacientes",command=carga) 
menu_pacientes.add_command(label="Borrar carga de Pacientes",command=borrardatos) 
menu_pacientes.add_command(label="Listado de Pacientes",)
menu_pacientes.add_command(label="Consulta de Pacientes")
menu_pacientes.add_command(label="Modificar Datos")
menu_pacientes.add_command(label="Salir",command=root)

menu_base.add_command(label="conectar", command=conexionbasedatos)
menu_base.add_command(label="salir")

menu_salir.add_command(label="salir",command=quit)
#******Botones************




#botonborrar=Button(miframe1,text="Borrar",command=borrardatos)
#botonborrar.grid(row=1,column=0,sticky="e",padx=10,pady=10)












#Labelcarga=Label(barraMenu,text="1-Carga de paciente")
 #Labelcarga.grid(row=1,column=0,padx=10,pady=10)
#Labelcarga.config(fg="blue",justify="right")
#Labellistado=Label(barraMenu,text="2-Listado de pacientes")
#Labelopcion.grid(row=2,column=0,padx=16,pady=10)
#Labelopcion.config(fg="blue",justify="right")
#Labelconsulta=Label(barraMenu,text="3-Consulta de pacientes")
#Labelopcion.grid(row=3,column=0,padx=10,pady=10)
#Labelopcion.config(fg="blue",justify="right")
#Labelmodificar=Label(barraMenu,text="4-Modificar datos de pacientes")
#Labelopcion.grid(row=4,column=0,padx=20,pady=10)
#Labelopcion.config(fg="blue",justify="right")
#Labelsalir=Label(barraMenu,text="5-Salir del menu")
#Labelopcion.grid(row=5,column=0,padx=10,pady=10)
#Labelopcion.config(fg="blue",justify="right")

root.mainloop()