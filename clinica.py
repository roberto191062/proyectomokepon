class paciente :

    def __init__(self) :
        self.contacto={}


    def  menu (self):
         opcion=0
         while opcion != 5 :
             print ("1- Carga de Pacientes")
             print ("2-Listado de Pacientes")
             print ("3-Consulta de Paciente")
             print ("4-Modificar Datos")
             print ("5-Salir del Menu")
             opcion=int(input("ingrese su opcion"))

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
        self.contacto[dni]=(nombre,apellido,direccion,telefono,obrasocial,sexo )
        print("------------------------------")

    def listado (self) :
        print("listado pacientes")
             
        for  dni in  self.contacto : 
             
             print( dni,self.contacto[dni][0],self.contacto[dni][1])
             print("----------------------------------------------")

    def consulta (self) :
        print("------------------------")

        print("consulta paciente")
        dni= int(input("ingrese dni"))
        for  dni in self.contacto :
         print(dni,self.contacto [dni][0],self.contacto[dni][1],self.contacto[dni][2])

    def modificar (self) :
        print("-----------------")
        dni=int(input("ingrese dni a modificar"))
        obrasocial=input("ingrese obra social a modificar")
        direccion=input("ingrese mail a modificar")
        mail=input("ingrese mail a modificar")

        for dni in self.contacto :
            print(dni,self.contacto[dni][obrasocial],self.contacto[dni][direccion],self.contacto[5])

            


#programa principal
paciente1=paciente()
paciente1.menu()
     


        
                      
                            
                                 




    


#class medico :

   #  def _init_ (self):
     #     self.medicos={}
         
         
#programa principal
