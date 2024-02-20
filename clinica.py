import tkinter as tk  
root= tk.Tk()
root.title("Clinica")
root.geometry=("400,200")
menu=tk.Menu()


class paciente :

    def __init__(self) :
        self.contacto={}
        
     

    def  menu (self):
         opcion=0
         opcion=int(input("ingrese su opcion"))
         
         while opcion != 5 :
             print ("1- Carga de Pacientes")
             print ("2-Listado de Pacientes")
             print ("3-Consulta de Paciente")
             print ("4-Modificar Datos")
             print ("5-Salir del Menu")
             

             if opcion == 1:
               self.carga()
             else :
                 if opcion==2:
                     self.listado()
                 else:
                     if opcion==3:
                         self.consulta()
                     else:
                         if opcion==4 :
                             self.modificar()
                            
    def carga (self) :
        dni=int(input("ingrese dni paciente")) 
        nombre=input("ingrese nombre del paciente") 
        apellido=input("ingrese apellido") 
        direccion=input("ingrese direccion paciente") 
        telefono=input("ingrese telefono paciente") 
        mail=input("ingrese mail paciente") 
        obrasocial=input("ingrese obra social paciente")
        sexo=input("ingrese sexo paciente")
        self.contacto[dni]=(dni,nombre,apellido,direccion,telefono,obrasocial,sexo )
        print("------------------------------")

    def listado (self) :
        print("listado pacientes")
             
        for  dni in  self.contacto : 
             
             print( self.contacto[dni][0],self.contacto[dni][1],self.contacto[dni][2],self.contacto[dni][3],self.contacto[dni][4],self.contacto[dni][5],self.contacto[dni][6],self.contacto[dni][7])
             print("----------------------------------------------")

    def consulta (self): 
        print("------------------------")

        print("consulta paciente")
        dni= int(input("ingrese dni"))
        for  dni in self.contacto :
         print(dni,self.contacto [dni][0],self.contacto[dni][1],self.contacto[dni][2],self.contacto[dni][3])

    def modificar (self) :
        print("-----------------")
        dni=int(input("ingrese dni a modificar"))
        if dni==self.contacto[dni]:
          obrasocial=input("ingrese obra social a modificar")
          direccion=input("ingrese direccion a modificar")
          mail=input("ingrese mail a modificar")
          self.contacto[dni][5]=(obrasocial)
        else:
            print("no existe el dni")  

        for dni in self.contacto :
         self.contacto[dni]=(obrasocial,direccion,mail) 
  
 
#class Aplicacion:
   #  def __init__(self):
    #   self.ventana1=tk.TK()
    #   self.ventana1.title("menu clinica")
     #  self.ventana1.mainloop()   
#crear menu
 #menu=tk.Menu()


menu_pacientes=tk.Menu(menu,tearoff=0)
menu_medicos=tk.Menu(menu,tearoff=0)
menu_turnos=tk.Menu(menu,tearoff=0)
menu_salir=tk.Menu(menu,tearoff=0)
#crear agregar opciones
menu.add_cascade(label="pacientes",menu=menu_pacientes)
menu.add_cascade(label="medicos",menu=menu_medicos)
menu.add_cascade(label="Turnos",menu=menu_turnos)
menu.add_cascade(label="Salir",menu=menu_salir)
#crear subopciones
menu_pacientes.add_command(label="carga de Pacientes",command=tk.Menu)
 
menu_pacientes.add_command(label="Listado de Pacientes")
menu_pacientes.add_command(label="Consulta de Pacientes")
menu_pacientes.add_command(label="Modificar Datos")

menu_pacientes.add_command(label="Salir",command=root.quit)



                                                                
root.config(menu=menu)
root.mainloop()

#programa principal
paciente1=paciente()
paciente1.menu()
#aplicacion1=Aplicacion()


        
                      
                            
                                 




    


#class medico :

   #  def _init_ (self):
     #     self.medicos={}
         
         
#programa principal
