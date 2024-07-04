from tkinter import *

#import tkinter as tk 




import sqlite3
from tkinter import messagebox
from datetime import datetime
root=Tk()
#root=tk.Tk()
root.title("Clinica")


barraMenu=Menu(root)
root.config(menu=barraMenu,width=1200,height=600)




#******variables pacientes****************
miid=StringVar()
midoc=StringVar()
minombre=StringVar()
miapellido=StringVar()
midireccion=StringVar()
misexo=StringVar()
miedad=StringVar()
miobrasocial=StringVar()
micorreo=StringVar()
mitelefono=StringVar()
mihc=StringVar()

#****variables medicos****
medmatricula=StringVar()
medoc=StringVar()
mednombre=StringVar()
medapellido=StringVar()
medireccion=StringVar()
medsexo=StringVar()
mededad=StringVar()
medobrasocial=StringVar()
medcorreo=StringVar()
medtelefono=StringVar()

fechahora=datetime
varfechahora=StringVar()





# ++++++Funciones+++++++++

def conexionbasedatos():
     
     miConexion=sqlite3.connect("usuarios.db")
      
     miCursor=miConexion.cursor()
     try:  

          miCursor.execute (''' 
            CREATE TABLE DATOSUSUARIOS(ID INTEGER PRIMARY KEY 
            AUTOINCREMENT,DOCUMENTO INTEGER(10) UNIQUE,NOMBRE VARCHAR(50),APELLIDO VARCHAR(50),DIRECCION VARCHAR(50),OBRASOCIAL VARCHAR(50),SEXO VARCHAR(30),EDAD INTEGER(2),CORREO VARCHAR(20),TELEFONO VARCHAR(20),HISTORIACLINICA VARCHAR(20))''' )

          miCursor.execute (''' 
            CREATE TABLE DATOSMEDICOS(ID INTEGER PRIMARY KEY 
            AUTOINCREMENT,DOCUMENTO INTEGER(10) UNIQUE, MATRICULA VARCHAR(20) UNIQUE,NOMBRE VARCHAR(50),APELLIDO VARCHAR(50),DIRECCION VARCHAR(50),OBRASOCIAL VARCHAR(50),SEXO VARCHAR(30),EDAD INTEGER(2),CORREO VARCHAR(20),TELEFONO VARCHAR(20))''' )


          miCursor.execute (''' 
            CREATE TABLE  TURNOS (ID INTEGER PRIMARY KEY 
            AUTOINCREMENT,DOCUMENTO INTEGER(10), MATRICULA VARCHAR(20) NOT NULL ,FECHAHORA DATETIME ,midoc INTEGER,medmatricula VARCHAR(20), FOREIGN KEY(midoc) REFERENCES DATOSUSUARIOS(midoc),FOREIGN KEY (medmatricula) REFERENCES DATOSMEDICOS(medmatricula))''' )







          messagebox.showinfo("Base Datos creada con exito")
     except:
          messagebox.showwarning("Atencion","Base Datos ya creada")

     miConexion.commit()
        
     miConexion.close()



def borrardatos():

  miid.set("")
  midoc.set("")
  minombre.set("")
  miapellido.set("")
  miedad.set("")
  midireccion.set("")
  misexo.set("")
  miobrasocial.set("") 
  micorreo.set("")
  mitelefono.set("")
  mihc.set("")                 

          


def borrardatosmed():

  medmatricula.set("")
  medoc.set("")
  mednombre.set("")
  medapellido.set("")
  medsexo.set("")
  mededad.set("")
  medireccion.set("")
  medobrasocial.set("") 
  medcorreo.set("")
  medtelefono.set("")

                    


  
                 


def crear():

    miConexion=sqlite3.connect("usuarios.db")

    miCursor=miConexion.cursor()

#miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (‘"+midoc.get()+"‘,‘"+minombre.get() +"‘,‘"+miapellido.get()+"´,´" +midireccion.get()+"´,´"+misexo.get()+"´,´" 
   # ‘"+miedad.get() +"´,´"+miobrasocial.get() +"´)") 
    miCursor.execute("INSERT INTO DATOSUSUARIOS(DOCUMENTO,NOMBRE,APELLIDO,SEXO,EDAD,DIRECCION,OBRASOCIAL,CORREO,TELEFONO,HISTORIACLINICA)VALUES(?,?,?,?,?,?,?,?,?,?)",(midoc.get(),minombre.get(),miapellido.get(),misexo.get(),miedad.get(),midireccion.get(),miobrasocial.get(),micorreo.get(),mitelefono.get(),mihc.get()))

    miConexion.commit()

    messagebox.showinfo("usuarios","registro insertado con exito") 




def crearmed():

    miConexion=sqlite3.connect("usuarios.db")

    miCursor=miConexion.cursor()

#miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (‘"+midoc.get()+"‘,‘"+minombre.get() +"‘,‘"+miapellido.get()+"´,´" +midireccion.get()+"´,´"+misexo.get()+"´,´" 
   # ‘"+miedad.get() +"´,´"+miobrasocial.get() +"´)") 
    miCursor.execute("INSERT INTO DATOSMEDICOS(MATRICULA,DOCUMENTO,NOMBRE,APELLIDO,SEXO,EDAD,DIRECCION,OBRASOCIAL,CORREO,TELEFONO)VALUES(?,?,?,?,?,?,?,?,?,?)",(medmatricula.get(),medoc.get(),mednombre.get(),medapellido.get(),medsexo.get(),mededad.get(),medireccion.get(),medobrasocial.get(),medcorreo.get(),medtelefono.get()))

    miConexion.commit()

    messagebox.showinfo("usuarios","registro insertado con exito") 


def crearturnos(midoc,medmatricula,fechahora):
  if isinstance (fechahora,datetime):
   fechahora=fechahora.strftime("%y-%m-%d %H:%M:%S")

   miConexion=sqlite3.connect("usuarios.db")

   miCursor=miConexion.cursor()

   miCursor.execute("INSERT INTO TURNOS (MATRICULA,DOCUMENTO,FECHAHORA)VALUES(?,?,?)",(medmatricula.get(),medoc.get(),fechahora))


   miConexion.commit()

   messagebox.showinfo("usuarios","registro insertado con exito") 










def listar():

    miConexion=sqlite3.connect("usuarios.db")
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE DOCUMENTO="+midoc.get())
    elpaciente=miCursor.fetchall
    for usuarios in elpaciente():
      midoc.set(usuarios[1])
      minombre.set(usuarios[2])
      miapellido.set(usuarios[3])
      miedad.set(usuarios[4])
      misexo.set(usuarios[5])
      midireccion.set(usuarios[6])
      miobrasocial.set(usuarios[7])
      micorreo.set(usuarios[8])
      mitelefono.set(usuarios[9])
      mihc.set(usuarios[10])
      
    miConexion.commit()


def listarmed():

    miConexion=sqlite3.connect("usuarios.db")
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSMEDICOS WHERE DOCUMENTO="+medoc.get())
    elmedico=miCursor.fetchall
    for usuarios in elmedico():
      medmatricula.set(usuarios[2])
      medoc.set(usuarios[1])
      mednombre.set(usuarios[3])
      medapellido.set(usuarios[4])
      mededad.set(usuarios[5])
      medsexo.set(usuarios[6])
      medireccion.set(usuarios[7])
      medobrasocial.set(usuarios[8])
      medcorreo.set(usuarios[9])
      medtelefono.set(usuarios[10])

    miConexion.commit()













def actualizar():   

  miConexion=sqlite3.connect("usuarios.db")
  miCursor=miConexion.cursor()

  valores=(midoc.get(),
  minombre.get(),
  miapellido.get(),
  misexo.get(),
  miedad.get(),
  midireccion.get(),
  miobrasocial.get(),
  micorreo.get(),
  mitelefono.get())

  

 # consulta= """ UPDATE DATOSUSUARIOS SET NOMBRE=?,APELLIDO=?,SEXO=?,EDAD=?,DIRECCION=?,OBRASOCIAL=? WHERE DOCUMENTO=?"""  
 # miCursor.execute(consulta,valores)


  miCursor.execute("UPDATE DATOSUSUARIOS SET DOCUMENTO=?,NOMBRE=?,APELLIDO=?,SEXO=?,EDAD=?,DIRECCION=?,OBRASOCIAL=?,CORREO=?,TELEFONO=?"+"WHERE DOCUMENTO=" +midoc.get(),(valores))
   
  
  miConexion.commit()

  messagebox.showinfo("usuarios","registro Actualizado con exito") 



def actualizarmed():   

  miConexion=sqlite3.connect("usuarios.db")
  miCursor=miConexion.cursor()

  valores=( medmatricula.get(),medoc.get(),
  mednombre.get(),
  medapellido.get(),
  medsexo.get(),
  mededad.get(),
  medireccion.get(),
  medobrasocial.get(),
  medcorreo.get(),
  medtelefono.get())

  

 # consulta= """ UPDATE DATOSUSUARIOS SET NOMBRE=?,APELLIDO=?,SEXO=?,EDAD=?,DIRECCION=?,OBRASOCIAL=? WHERE DOCUMENTO=?"""  
 # miCursor.execute(consulta,valores)


  miCursor.execute("UPDATE DATOSMEDICOS  SET MATRICULA=?, DOCUMENTO=?,NOMBRE=?,APELLIDO=?,SEXO=?,EDAD=?,DIRECCION=?,OBRASOCIAL=?,CORREO=?,TELEFONO=?"+"WHERE DOCUMENTO=" +medoc.get(),(valores))
   
  
  miConexion.commit()

  messagebox.showinfo("usuarios","registro Actualizado con exito") 





def eliminar():

    miConexion=sqlite3.connect("usuarios.db")
    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE DOCUMENTO="+midoc.get())

    miConexion.commit()
    messagebox.showinfo("Registro borrado con exito")

def mostrarroot():
    miframe1.pack_forget()
    root.title("Clinica")
    


def mostrarroot2():
    miframe2.pack_forget()
    root.title("Clinica")
       

def mostrarroot3():
    miframe3.pack_forget()
    root.title("Clinica")

     

def carga():
    
     global miframe1 
     miframe1=Frame(root)
     root.title("Ingreso PacienteS")
     miframe1.pack() 

     #miframe1=tk.Toplevel()
     #miframe1.title=("ingreso pacientes")
     #miframe1.geometry("1000x600")


   


     #*****Botones********
             
     botonborrar=Button(miframe1,text="Borrar",command=borrardatos)
     botonborrar.grid(row=12,column=2,sticky="e",padx=10,pady=10)

     botoncrear=Button(miframe1,text="Grabar",command=crear) 
     botoncrear.grid( row=12,column=3,sticky="e",padx=10,pady=10)

     botonsalir=Button(miframe1,text="Salir",command=mostrarroot)
     botonsalir.grid(row=12,column=7,sticky="e",padx=10,pady=10)

     botonlistar=Button(miframe1,text="Listar",command=listar)
     botonlistar.grid(row=12,column=4,sticky="e",padx=10,pady=10) 

     botonactualizar=Button(miframe1,text="Actualizar",command=actualizar)
     botonactualizar.grid(row=12,column=5,sticky="e",padx=10,pady=10) 

     botoneliminar=Button(miframe1,text="Eliminar",command=eliminar)
     botoneliminar.grid(row=12,column=6,sticky="e",padx=10,pady=10) 



     #------------Entrada datos pacientes--------

     Id=Entry(miframe1,textvariable=miid)
     Id.grid(row=1,column=2)
     IdLabel=Label(miframe1,text="Id")
     IdLabel.grid(row=1,column=1,sticky="e",padx=10,pady=10)


     documento=Entry(miframe1,textvariable=midoc)
     documento.grid(row=2,column=2)
     documentoLabel=Label(miframe1,text="Documento")
     documentoLabel.grid(row=2,column=1,sticky="e",padx=10,pady=10)


     nombre=Entry(miframe1,textvariable=minombre)
     nombre.grid(row=3,column=2)
     nombreLabel=Label(miframe1,text="Nombre")
     nombreLabel.grid(row=3,column=1,sticky="e",padx=10,pady=10)

      

     apellido=Entry(miframe1,textvariable=miapellido)
     apellido.grid(row=4,column=2)
     apellidoLabel=Label(miframe1,text="Apellido")
     apellidoLabel.grid(row=4,column=1,sticky="e",padx=10,pady=10)

     sexo=Entry(miframe1,textvariable=misexo)
     sexo.grid(row=5,column=2)
     sexoLabel=Label(miframe1,text="Sexo")
     sexoLabel.grid(row=5,column=1,sticky="e",padx=10,pady=10)

     edad=Entry(miframe1,textvariable=miedad)
     edad.grid(row=6,column=2)
     edadLabel=Label(miframe1,text="Edad")
     edadLabel.grid(row=6,column=1,sticky="e",padx=10,pady=10)


     direccion=Entry(miframe1,textvariable=midireccion)
     direccion.grid(row=7,column=2)
     direccionLabel=Label(miframe1,text="Direccion")
     direccionLabel.grid(row=7,column=1,sticky="e",padx=10,pady=10)
     

     obrasocial=Entry(miframe1,textvariable=miobrasocial)
     obrasocial.grid(row=8,column=2)
     obrasocialLabel=Label(miframe1,text="Obra social")
     obrasocialLabel.grid(row=8,column=1,sticky="e",padx=10,pady=10)

     mail=Entry(miframe1,textvariable=micorreo)
     mail.grid(row=9,column=2)
     mailLabel=Label(miframe1,text="Correo")
     mailLabel.grid(row=9,column=1,sticky="e",padx=10,pady=10)

     telefono=Entry(miframe1,textvariable=mitelefono)
     telefono.grid(row=10,column=2)
     telefonolabel=Label(miframe1,text="Telefono")
     telefonolabel.grid(row=10,column=1,sticky="e",padx=10,pady=10)

     historiaclinica=Entry(miframe1,textvariable=mihc)
     historiaclinica.grid(row=11,column=2)
     historiaclinicalabel=Label(miframe1,text="HistoriaClinica")
     historiaclinicalabel.grid(row=11,column=1)



#--------------carga medicos---------------
def carga2():
  global miframe2
  miframe2=Frame(root)
  root.title("Ingreso Medicos")
  miframe2.pack()



  matricula=Entry(miframe2,textvariable=medmatricula)
  matricula.grid(row=1,column=2)
  matriculaLabel=Label(miframe2,text="Matricula")
  matriculaLabel.grid(row=1,column=1,sticky="e",padx=10,pady=10)


  documento=Entry(miframe2,textvariable=medoc)
  documento.grid(row=2,column=2)
  documentoLabel=Label(miframe2,text="Documento")
  documentoLabel.grid(row=2,column=1,sticky="e",padx=10,pady=10)


  nombre=Entry(miframe2,textvariable=mednombre)
  nombre.grid(row=3,column=2)
  nombreLabel=Label(miframe2,text="Nombre")
  nombreLabel.grid(row=3,column=1,sticky="e",padx=10,pady=10)

      

  apellido=Entry(miframe2,textvariable=miapellido)
  apellido.grid(row=4,column=2)
  apellidoLabel=Label(miframe2,text="Apellido")
  apellidoLabel.grid(row=4,column=1,sticky="e",padx=10,pady=10)

  sexo=Entry(miframe2,textvariable=misexo)
  sexo.grid(row=5,column=2)
  sexoLabel=Label(miframe2,text="Sexo")
  sexoLabel.grid(row=5,column=1,sticky="e",padx=10,pady=10)

  edad=Entry(miframe2,textvariable=miedad)
  edad.grid(row=6,column=2)
  edadLabel=Label(miframe2,text="Edad")
  edadLabel.grid(row=6,column=1,sticky="e",padx=10,pady=10)


  direccion=Entry(miframe2,textvariable=midireccion)
  direccion.grid(row=7,column=2)
  direccionLabel=Label(miframe2,text="Direccion")
  direccionLabel.grid(row=7,column=1,sticky="e",padx=10,pady=10)
     

  obrasocial=Entry(miframe2,textvariable=miobrasocial)
  obrasocial.grid(row=8,column=2)
  obrasocialLabel=Label(miframe2,text="Obra social")
  obrasocialLabel.grid(row=8,column=1,sticky="e",padx=10,pady=10)

  mail=Entry(miframe2,textvariable=micorreo)
  mail.grid(row=9,column=2)
  mailLabel=Label(miframe2,text="Correo")
  mailLabel.grid(row=9,column=1,sticky="e",padx=10,pady=10)

  telefono=Entry(miframe2,textvariable=mitelefono)
  telefono.grid(row=10,column=2)
  telefonolabel=Label(miframe2,text="Telefono")
  telefonolabel.grid(row=10,column=1,sticky="e",padx=10,pady=10)




  botonborrar=Button(miframe2,text="Borrar",command=borrardatosmed)
  botonborrar.grid(row=11,column=2,sticky="e",padx=10,pady=10)

  botoncrear=Button(miframe2,text="Grabar",command=crearmed) 
  botoncrear.grid( row=11,column=3,sticky="e",padx=10,pady=10)

  botonsalir=Button(miframe2,text="Salir",command=mostrarroot2)
  botonsalir.grid(row=11,column=7,sticky="e",padx=10,pady=10)

  botonsalir=Button(miframe2,text="Listar",command=listarmed)
  botonsalir.grid(row=11,column=4,sticky="e",padx=10,pady=10) 

  botonsalir=Button(miframe2,text="Actualizar",command=actualizarmed)
  botonsalir.grid(row=11,column=5,sticky="e",padx=10,pady=10) 

  botoneliminar=Button(miframe2,text="Eliminar",command=eliminar)
  botoneliminar.grid(row=11,column=6,sticky="e",padx=10,pady=10) 


def cargaturnos():
   
     global  miframe3

     miframe3=Frame(root)
     root.title("Ingreso Turnos")
     miframe3.pack() 
     

     matricula=Entry(miframe3,textvariable=medmatricula)
     matricula.grid(row=1,column=2)
     matriculaLabel=Label(miframe3,text="Matricula")
     matriculaLabel.grid(row=1,column=1,sticky="e",padx=10,pady=10)


     nombre=Entry(miframe3,textvariable=mednombre)
     nombre.grid(row=2,column=2)
     nombreLabel=Label(miframe3,text="Nombre")
     nombreLabel.grid(row=2,column=1,sticky="e",padx=10,pady=10)

      

     apellido=Entry(miframe3,textvariable=miapellido)
     apellido.grid(row=3,column=2)
     apellidoLabel=Label(miframe3,text="Apellido")
     apellidoLabel.grid(row=3,column=1,sticky="e",padx=10,pady=10)


     documento=Entry(miframe3,textvariable=midoc)
     documento.grid(row=4,column=2)
     documentoLabel=Label(miframe3,text="Documento")
     documentoLabel.grid(row=4,column=1,sticky="e",padx=10,pady=10)


     nombre=Entry(miframe3,textvariable=minombre)
     nombre.grid(row=5,column=2)
     nombreLabel=Label(miframe3,text="Nombre")
     nombreLabel.grid(row=5,column=1,sticky="e",padx=10,pady=10)

      

     apellido=Entry(miframe3,textvariable=miapellido)
     apellido.grid(row=6,column=2)
     apellidoLabel=Label(miframe3,text="Apellido")
     apellidoLabel.grid(row=6,column=1,sticky="e",padx=10,pady=10)

     fechahora=Entry(miframe3,textvariable=varfechahora)
     fechahora.grid(row=7,column=2)
     fechahoraLabel=Label(miframe3,text="Fecha Hora")
     fechahoraLabel.grid(row=7,column=1,sticky="e",padx=10,pady=10)

     botonborrar=Button(miframe3,text="Borrar",command=borrardatos)
     botonborrar.grid(row=12,column=2,sticky="e",padx=10,pady=10)

     botoncrear=Button(miframe3,text="Grabar",command=crearturnos) 
     botoncrear.grid( row=12,column=3,sticky="e",padx=10,pady=10)

     botonsalir=Button(miframe3,text="Salir",command=mostrarroot3)
     botonsalir.grid(row=12,column=7,sticky="e",padx=10,pady=10)

     botonlistar=Button(miframe3,text="Listar",command=listar)
     botonlistar.grid(row=12,column=4,sticky="e",padx=10,pady=10) 

     botonactualizar=Button(miframe3,text="Actualizar",command=actualizar)
     botonactualizar.grid(row=12,column=5,sticky="e",padx=10,pady=10) 

     botoneliminar=Button(miframe3,text="Eliminar",command=eliminar)
     botoneliminar.grid(row=12,column=6,sticky="e",padx=10,pady=10) 




     
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

menu_medicos.add_command(label="carga medicos",command=carga2)

menu_turnos.add_command(label="Carga Turnos",command=cargaturnos)


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