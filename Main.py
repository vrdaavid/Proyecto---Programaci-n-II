from tkinter import *
import tkinter.font as TkFont
from Utilidades import * 
from tkinter import messagebox
from tkinter import ttk

import datetime



class Inicio:
    # atributos de la clase Inicio, acá se colocan todas las variables globales dentro del código para poder parametrizar tamaños, colores, etc
    colorPanel = "#273c75"
    colorError = "#d63031"
    colorExito = "#27ae60"
    pantallas = []
    medidaCentroMenus_X = 260
    medidaCentroMenus_Y = 100

    def __init__(self, master = None):

        ## Inicializar aplicación padre de Tkinter, raíz será la aplicación donde se colocarán todos los canvas (ventanas)
        self.raiz = Tk()

        # Tamaños estándar de letra para ser usados en los labels
        self.estiloBoton = TkFont.Font(self.raiz, family='Helvetica', size=12, weight="bold")
        self.estiloLabel = TkFont.Font(self.raiz, family='Helvetica', size=16, weight="bold")
        self.estiloMensaje = TkFont.Font(self.raiz, family='Helvetica', size=10, weight="bold")

        # Definir tamaño de la ventana padre
        self.raiz.geometry("1080x720") 
        self.raiz.resizable(width=False, height=False)  # Deshabilitar tamaño variable 
        self.raiz.title("Prueba") 
        
        self.mostrarLogin()

        # Esta función es necesaria para que se ejecute la interfaz gráfica
        self.raiz.mainloop()
    
    def mostrarLogin(self):

        # Se crea una nueva pantalla (canvas) dentro de la raíz
        self.pantallaLogin = Canvas(self.raiz, width = 1080, height = 720, bg = "#ecf0f1", highlightthickness=0, relief='ridge')

        # Se inicializan labels, campos y boton dentro del canvas login
        self.labelBienvenida = Label(self.pantallaLogin, text="¡Bienvenido al Sistema!", font=('Helvetica', 25))
        self.labelUsuario = Label(self.pantallaLogin, text="USUARIO: ", font = self.estiloLabel)
        self.labelPassword = Label(self.pantallaLogin, text="CONTRASEÑA: ", font = self.estiloLabel)
        self.campoUsuario = Entry(self.pantallaLogin, justify="left")
        self.campoClave = Entry(self.pantallaLogin, justify="left", show = "*")
        self.botonLogin = Button(self.pantallaLogin, command = self.login,  text = "Ingresar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        
        # Se colocan dentro del canvas en las diferentes posiciones x, y
        self.labelBienvenida.place(x = 400, y = 250)
        self.labelUsuario.place(x = 400, y = 360)
        self.labelPassword.place(x = 400, y = 400)
        self.campoUsuario.place(x = 580, y = 360, width = 130, height = 30)
        self.campoClave.place(x = 580, y = 400, width = 130, height = 30)
        self.botonLogin.place(x = 500, y = 500)

        # Este método es necesario para poder cargar el canvas con todos los gadgets agregados
        self.pantallaLogin.pack()


    def login(self):
        # Función para verificar el usuario y contraseña

        if ingresar(self.campoUsuario.get(), self.campoClave.get()): ## Si es true, entonces se ingresa en el sistema
            
            # se limpia la raíz y se elimina la pantalla login
            self.pantallaLogin.destroy()
           
            # se carga la barra lateral y la pantalla principal 
            self.agregarBarraLateral()
            self.mostrarMenuPrincipal()


        else:          
            # muestra error 
            self.mostrarMensaje("Error", "Usuario / Contraseña incorrecta")
            

    def eliminarMenus(self):
        # Función para limpiar todos los menus creados
        
        try:
            for pantalla in self.pantallas:
                pantalla.destroy()

        except:
            pass
    
    def agregarBarraLateral(self):
        ## Canvas
        self.barraLateral = Canvas(self.raiz, bg = self.colorPanel, width = 180)   ## Barra lateral
        self.barraLateral.pack(side = LEFT, fill = BOTH)

        self.agregarBotones()
    

    def agregarBotones(self):
        self.botonMenuInicio = Button(self.barraLateral, command = self.mostrarMenuPrincipal ,text = "Inicio",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonMenuInicio.place(x = 40, y = 40)

        # Botones menu usuario
        self.labelUsuarios = Label(self.barraLateral ,text = "Usuarios",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.labelUsuarios.place(x = 40, y = 140)
    
        self.botonMenuUsuarios1 = Button(self.barraLateral, command = self.mostrarMenuCrearUsuarios ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuUsuarios1.place(x = 40, y = 160)

        self.botonMenuUsuarios4 = Button(self.barraLateral, command = self.mostrarMenuConsultarUsuarios ,text = "Consultar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuUsuarios4.place(x = 40, y = 180)

        # Botones menu miembros

        self.labelMiembros= Label(self.barraLateral ,text = "Miembros",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.labelMiembros.place(x = 40, y = 250)

        self.botonMenuMiembros1 = Button(self.barraLateral, command = self.mostrarMenuCrearMiembros ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuMiembros1.place(x = 40, y = 270)

        self.botonMenuMiembros2 = Button(self.barraLateral, command = self.mostrarMenuConsultarMiembros ,text = "Consultar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuMiembros2.place(x = 40, y = 290)


        # Boton Menu Niños
        self.boton3 = Button(self.barraLateral, text = "Apadrinados",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
        self.boton3.place(x = 40, y = 350)

        self.boton3 = Button(self.barraLateral, text = "prueba",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
        self.boton3.place(x = 40, y = 450)

        self.boton4 = Button(self.barraLateral, command = self.salirMenuPrincipal, text = "Salir",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
        self.boton4.place(x = 40, y = 550)


    def salirMenuPrincipal(self):
        self.eliminarMenus()
        self.barraLateral.destroy()
        self.mostrarLogin()

    def mostrarMenuPrincipal(self):
        self.eliminarMenus()

        self.menuPrincipal = Canvas(self.raiz, width = 800, height = 720, bg = "#ecf0f1", highlightthickness=0, relief='ridge')
        self.menuPrincipal.pack()

        self.pantallas.append(self.menuPrincipal)

        titulo = " " * (22 - len("BIENVENIDO AL SISTEMA")) + "BIENVENIDO AL SISTEMA"

        self.titulo = Label(self.menuPrincipal, text=titulo, font = self.estiloLabel)
        self.titulo.place(x = self.medidaCentroMenus_X, y = self.medidaCentroMenus_Y)
       
    def mostrarMenuCrearUsuarios(self): 
        self.eliminarMenus()
        self.menuCrearUsuarios = Canvas(self.raiz, width = 800, height = 720, bg = "#ecf0f1", highlightthickness=0, relief='ridge')
        self.menuCrearUsuarios.pack()
        self.pantallas.append(self.menuCrearUsuarios)
        titulo = " " * (22 - len("USUARIOS")) + "USUARIOS"
        self.titulo = Label(self.menuCrearUsuarios, text=titulo, font = self.estiloLabel)
        self.titulo.place(x = self.medidaCentroMenus_X, y = self.medidaCentroMenus_Y)

        espacioY = 80
        
        # Labels
        self.labelNombreCompleto = Label(self.menuCrearUsuarios, text="Nombre Completo", name = "labelNombreCompleto" , font = ('Helvetica' , 10, "bold"))
        self.labelUsuario = Label(self.menuCrearUsuarios, text="Usuario", name = "labelUsuario" , font = ('Helvetica' , 10, "bold"))
        self.labelClave = Label(self.menuCrearUsuarios, text="Contraseña", name = "labelClave" , font = ('Helvetica' , 10, "bold"))
        self.labelRol = Label(self.menuCrearUsuarios, text="Rol", name = "labelRol" , font = ('Helvetica' , 10, "bold"))
        
        self.labelNombreCompleto.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.labelUsuario.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 2) 
        self.labelClave.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 3) 
        self.labelRol.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 4) 

        # Campos
        self.campoNombreCompleto = Entry(self.menuCrearUsuarios, justify="left", name = "campoNombreCompleto", font = ('Helvetica' , 10, "bold"))
        self.campoUsuario = Entry(self.menuCrearUsuarios, justify="left", name = "campoUsuario", font = ('Helvetica' , 10, "bold"))
        self.campoClave = Entry(self.menuCrearUsuarios, justify="left", name = "campoClave", font = ('Helvetica' , 10, "bold"), show="*")

        self.campoNombreCompleto.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.campoUsuario.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 2)
        self.campoClave.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 3)

        self.campoClave.config(state="normal")

        #roles = obtenerRoles()

        # Lista
        self.listaRoles = ttk.Combobox(self.menuCrearUsuarios, state="readonly")
        self.listaRoles["values"] = ["Administrador", "Agente"]
        self.listaRoles.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 4, height="30", width="130")
        self.listaRoles.current(0)

        # Asignar dinamicamente eventos a cada label creado
        ##self.label1.bind("<Button-1>", lambda event, label = self.label1 : print(label)
        
        # Botones
        self.botonCrearUsuario = Button(self.menuCrearUsuarios, command=self.crearUsuario ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonCrearUsuario.place(x = self.medidaCentroMenus_X - 30 , y = self.medidaCentroMenus_Y + espacioY * 5,  width = 130, height = 30)

        self.botonLimpiarFormulario = Button(self.menuCrearUsuarios, command= lambda : self.limpiarFormulario(self.campoNombreCompleto, self.campoClave, self.campoUsuario)  ,text = "Limpiar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonLimpiarFormulario.place(x = self.medidaCentroMenus_X + 120 , y = self.medidaCentroMenus_Y + espacioY * 5,  width = 130, height = 30)

    def mostrarMenuConsultarUsuarios(self): 
        self.eliminarMenus()
        self.menuConsultarUsuarios = Canvas(self.raiz, width = 800, height = 720, bg = "#ecf0f1", highlightthickness=0, relief='ridge')
        self.menuConsultarUsuarios.pack()
        self.pantallas.append(self.menuConsultarUsuarios)
        titulo = " " * (22 - len("USUARIOS")) + "USUARIOS"
        self.titulo = Label(self.menuConsultarUsuarios, text=titulo, font = self.estiloLabel)
        self.titulo.place(x = self.medidaCentroMenus_X, y = self.medidaCentroMenus_Y)

        self.usuarioEncontrado = False 

        espacioY = 80

         # Labels 
        self.labelNombreCompleto = Label(self.menuConsultarUsuarios, text="Nombre Completo", name = "labelNombreCompleto" , font = ('Helvetica' , 10, "bold"))
        self.labelUsuario = Label(self.menuConsultarUsuarios, text="Usuario", name = "labelUsuario" , font = ('Helvetica' , 10, "bold"))
        self.labelClave = Label(self.menuConsultarUsuarios, text="Contraseña", name = "labelClave" , font = ('Helvetica' , 10, "bold"))

        self.labelUsuario.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.labelNombreCompleto.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 2)
        self.labelClave.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 3) 

        # Campos
        self.campoUsuario = Entry(self.menuConsultarUsuarios, justify="left", name = "campoUsuario", font = ('Helvetica' , 10, "bold"))
        self.campoNombreCompleto = Entry(self.menuConsultarUsuarios, justify="left", name = "campoNombreCompleto", font = ('Helvetica' , 10, "bold"))
        self.campoClave = Entry(self.menuConsultarUsuarios, justify="left", name = "campoClave", font = ('Helvetica' , 10, "bold"), show="*")

        self.campoUsuario.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.campoNombreCompleto.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 2)
        self.campoClave.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 3)

        # Desactivamos los campos
        self.campoClave.config(state="disabled")     
        self.campoNombreCompleto.config(state="disabled") 
        
        # Botones
        self.botonBuscarUsuario = Button(self.menuConsultarUsuarios, command=self.buscarUsuario ,text = "Buscar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonBuscarUsuario.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 1,  width = 80, height = 25)
        
        # Boton Modificar Nombre

        self.botonMostrarModificarNombre = Button(self.menuConsultarUsuarios, 
                                            command=lambda: self.mostrarModificar(self.botonMostrarModificarNombre, self.botonGuardarModificarNombre, self.botonCancelarModificarNombre, 
                                            self.medidaCentroMenus_X + 280 ,  self.medidaCentroMenus_Y + espacioY * 2,
                                            self.medidaCentroMenus_X + 400 ,   self.medidaCentroMenus_Y + espacioY * 2, 
                                            self.campoNombreCompleto)  
                                            ,text = "Modificar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonMostrarModificarNombre.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 2,  width = 80, height = 25)


        self.botonGuardarModificarNombre = Button(self.menuConsultarUsuarios, 
                                                    command= lambda: self.actualizarInformacionUsuario("NombreCompleto", 
                                                    self.campoNombreCompleto, self.botonCancelarModificarNombre) ,                                                  
                                                    text = "Guardar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonCancelarModificarNombre = Button(self.menuConsultarUsuarios, 
                                                    command=lambda: self.esconderBotonesModificar(self.botonMostrarModificarNombre,  
                                                    self.medidaCentroMenus_X + 280, self.medidaCentroMenus_Y + espacioY * 2, 
                                                    self.botonGuardarModificarNombre, self.botonCancelarModificarNombre, 
                                                    self.campoNombreCompleto)  
                                                    ,text = "Cancelar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        

         # Boton Modificar Contraseña

        # Cambiar nombre de variables botonMostrar, botonGuardar, botonCancelar, nombre de columna y los campos 


        self.botonMostrarModificarClave = Button(self.menuConsultarUsuarios, 
                                            command=lambda: self.mostrarModificar(self.botonMostrarModificarClave, self.botonGuardarModificarClave, self.botonCancelarModificarClave, 
                                            self.medidaCentroMenus_X + 280 ,  self.medidaCentroMenus_Y + espacioY * 3,
                                            self.medidaCentroMenus_X + 400 ,   self.medidaCentroMenus_Y + espacioY * 3, 
                                            self.campoClave)  
                                            ,text = "Modificar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonMostrarModificarClave.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 3,  width = 80, height = 25)


        self.botonGuardarModificarClave = Button(self.menuConsultarUsuarios, 
                                                    command= lambda: self.actualizarInformacionUsuario("Clave", 
                                                    self.campoClave, self.botonCancelarModificarClave) ,                                                  
                                                    text = "Guardar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonCancelarModificarClave = Button(self.menuConsultarUsuarios, 
                                                    command=lambda: self.esconderBotonesModificar(self.botonMostrarModificarClave,  
                                                    self.medidaCentroMenus_X + 280, self.medidaCentroMenus_Y + espacioY * 3, 
                                                    self.botonGuardarModificarClave, self.botonCancelarModificarClave, 
                                                    self.campoClave)  
                                                    ,text = "Cancelar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)


        self.botonBorrarUsuario = Button(self.menuConsultarUsuarios, 
                                                    command=lambda: self.borrarUsuario()
                                                    ,text = "Borrar",  bg = self.colorError, fg = "white",  relief = "flat", font = self.estiloBoton)

        self.botonBorrarUsuario.place(x = self.medidaCentroMenus_X + 50, y = self.medidaCentroMenus_Y + espacioY * 4,  width = 200, height = 25)  

    def mostrarMenuCrearMiembros(self): 
        self.eliminarMenus()
        self.menuCrearMiembros = Canvas(self.raiz, width = 800, height = 720, bg = "#ecf0f1", highlightthickness=0, relief='ridge')
        self.menuCrearMiembros.pack()
        self.pantallas.append(self.menuCrearMiembros)
        titulo = " " * (22 - len("MIEMBROS")) + "MIEMBROS"
        self.titulo = Label(self.menuCrearMiembros, text=titulo, font = self.estiloLabel)
        self.titulo.place(x = self.medidaCentroMenus_X, y = self.medidaCentroMenus_Y)

        espacioY = 80
        
        # Labels
        self.labelNombreCompleto = Label(self.menuCrearMiembros, text="Nombre Completo", name = "labelNombreCompleto" , font = ('Helvetica' , 10, "bold"))
        self.labelCedula = Label(self.menuCrearMiembros, text="Cedula", name = "labelCedula" , font = ('Helvetica' , 10, "bold"))
        self.labelFechaNacimiento= Label(self.menuCrearMiembros, text="Fecha Nacimiento", name = "labelFechaNacimiento" , font = ('Helvetica' , 10, "bold"))
        self.labelID = Label(self.menuCrearMiembros, text="ID", name = "labelID" , font = ('Helvetica' , 10, "bold"))
        self.labelColaboracion = Label(self.menuCrearMiembros, text="Colaboracion", name = "labelColaboracion" , font = ('Helvetica' , 10, "bold"))
        self.labelTipo = Label(self.menuCrearMiembros, text="Tipo", name = "labelTipo" , font = ('Helvetica' , 10, "bold"))
        
        self.labelNombreCompleto.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.labelCedula.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 2) 
        self.labelFechaNacimiento.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 3) 
        self.labelID.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 4) 
        self.labelColaboracion.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 5) 
        self.labelTipo.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 6) 


        # Labels Fecha
        self.labelDia = Label(self.menuCrearMiembros, text="Dia", font = ('Helvetica' , 9, "bold"))
        self.labelDia.place(x = self.medidaCentroMenus_X  + 130, y = self.medidaCentroMenus_Y + espacioY * 3 * 0.9 ) 

        self.labelMes = Label(self.menuCrearMiembros, text="Mes", font = ('Helvetica' , 9, "bold"))
        self.labelMes.place(x = self.medidaCentroMenus_X  + 190, y = self.medidaCentroMenus_Y + espacioY * 3 * 0.9 ) 

        self.labelAno = Label(self.menuCrearMiembros, text="Año", font = ('Helvetica' , 9, "bold"))
        self.labelAno.place(x = self.medidaCentroMenus_X  + 250, y = self.medidaCentroMenus_Y + espacioY * 3 * 0.9 ) 

        # Campos
        self.campoNombreCompleto = Entry(self.menuCrearMiembros, justify="left", name = "campoNombreCompleto", font = ('Helvetica' , 10, "bold"))
        self.campoCedula = Entry(self.menuCrearMiembros, justify="left", name = "campoUsuario", font = ('Helvetica' , 10, "bold"))
        self.campoID = Entry(self.menuCrearMiembros, justify="left", name = "campoID", font = ('Helvetica' , 10, "bold"))
        self.campoColaboracion = Entry(self.menuCrearMiembros, justify="left", name = "campoClave", font = ('Helvetica' , 10, "bold"))

        self.campoNombreCompleto.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.campoCedula.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 2)
        self.campoID.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 4)
        self.campoColaboracion.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 5)

        self.campoCedula.config(state="normal")

        # Lista
        self.listaDias = ttk.Combobox(self.menuCrearMiembros, state="readonly")
        self.listaDias["values"] = [""] + [x for x in range(1, 32)]
        self.listaDias.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 3, height="35", width="50")
        self.listaDias.current(0)

        self.listaMeses = ttk.Combobox(self.menuCrearMiembros, state="readonly")
        self.listaMeses["values"] = [""] + [x for x in range(1, 13)]
        self.listaMeses.place(x = self.medidaCentroMenus_X  + 180, y = self.medidaCentroMenus_Y + espacioY * 3, height="35", width="50")
        self.listaMeses.current(0)

        self.listaAnos = ttk.Combobox(self.menuCrearMiembros, state="readonly")
        self.listaAnos["values"] = [""] + sorted([x for x in range(1950, int(datetime.datetime.now().year))], reverse=True)
        self.listaAnos.place(x = self.medidaCentroMenus_X  + 240, y = self.medidaCentroMenus_Y + espacioY * 3, height="35", width="50")
        self.listaAnos.current(0)

        self.listaRoles = ttk.Combobox(self.menuCrearMiembros, state="readonly")
        self.listaRoles["values"] = ["Padrinos", "Apadrinados", "CES", "Becados", "Postulantes"]
        self.listaRoles.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 6, height="30", width="130")
        self.listaRoles.current(0)

        # Crear trigger para la lista, en caso de seleccionar apadrinado, mostrar la lista de categorias
        self.listaRoles.bind('<<ComboboxSelected>>', 
                             lambda event: self.listaCategorias.place(x = self.medidaCentroMenus_X  + 270, y = self.medidaCentroMenus_Y + espacioY * 6, height="30", width="130") 
                                                                     if (self.listaRoles.get() == "Apadrinados") else self.listaCategorias.place_forget())

        self.listaCategorias = ttk.Combobox(self.menuCrearMiembros, state="readonly")
        self.listaCategorias["values"] = ["", "Niño", "Adulto Mayor"]
        self.listaCategorias.current(0)

        # Botones
        self.botonCrearMiembro = Button(self.menuCrearMiembros, command=self.crearMiembro ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonCrearMiembro.place(x = self.medidaCentroMenus_X - 30 , y = self.medidaCentroMenus_Y + espacioY * 7,  width = 130, height = 30)

        self.botonLimpiarFormulario = Button(self.menuCrearMiembros, 
                                    command = lambda : self.limpiarFormulario(self.campoNombreCompleto, self.campoColaboracion, self.campoID, self.campoCedula)
                                    , text = "Limpiar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)

        self.botonLimpiarFormulario.place(x = self.medidaCentroMenus_X + 120 , y = self.medidaCentroMenus_Y + espacioY * 7,  width = 130, height = 30)

    def mostrarMenuConsultarMiembros(self): 
        self.eliminarMenus()
        self.menuConsultarMiembros = Canvas(self.raiz, width = 800, height = 720, bg = "#ecf0f1", highlightthickness=0, relief='ridge')
        self.menuConsultarMiembros.pack()
        self.pantallas.append(self.menuConsultarMiembros)
        titulo = " " * (22 - len("MIEMBROS")) + "MIEMBROS"
        self.titulo = Label(self.menuConsultarMiembros, text=titulo, font = self.estiloLabel)
        self.titulo.place(x = self.medidaCentroMenus_X, y = self.medidaCentroMenus_Y)

        self.usuarioEncontrado = False 

        espacioY = 80

         # Labels 
        self.labelNombreCompleto = Label(self.menuConsultarMiembros, text="Nombre Completo", name = "labelNombreCompleto" , font = ('Helvetica' , 10, "bold"))
        self.labelCedula = Label(self.menuConsultarMiembros, text="Cedula", name = "labelCedula" , font = ('Helvetica' , 10, "bold"))
        self.labelFechaNacimiento= Label(self.menuConsultarMiembros, text="Fecha Nacimiento", name = "labelFechaNacimiento" , font = ('Helvetica' , 10, "bold"))
        self.labelID = Label(self.menuConsultarMiembros, text="ID", name = "labelID" , font = ('Helvetica' , 10, "bold"))
        self.labelColaboracion = Label(self.menuConsultarMiembros, text="Colaboracion", name = "labelColaboracion" , font = ('Helvetica' , 10, "bold"))
        self.labelTipo = Label(self.menuConsultarMiembros, text="Tipo", name = "labelTipo" , font = ('Helvetica' , 10, "bold"))

        self.labelNombreCompleto.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 2)
        self.labelCedula.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 1) 
        self.labelFechaNacimiento.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 3) 
        self.labelID.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 4) 
        self.labelColaboracion.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 5) 
        self.labelTipo.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 6) 

        # Campos

        self.campoNombreCompleto = Entry(self.menuConsultarMiembros, justify="left", name = "campoNombreCompleto", font = ('Helvetica' , 10, "bold"))
        self.campoCedula = Entry(self.menuConsultarMiembros, justify="left", name = "campoUsuario", font = ('Helvetica' , 10, "bold"))
        self.campoID = Entry(self.menuConsultarMiembros, justify="left", name = "campoID", font = ('Helvetica' , 10, "bold"))
        self.campoColaboracion = Entry(self.menuConsultarMiembros, justify="left", name = "campoClave", font = ('Helvetica' , 10, "bold"))

        self.campoNombreCompleto.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 2)
        self.campoCedula.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.campoID.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 4)
        self.campoColaboracion.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 5)
        
        # Botones
        self.botonBuscarCedula = Button(self.menuConsultarMiembros, command=self.buscarMiembro ,text = "Buscar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonBuscarCedula.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 1,  width = 80, height = 25)

         # Labels Fecha
        self.labelDia = Label(self.menuConsultarMiembros, text="Dia", font = ('Helvetica' , 9, "bold"))
        self.labelDia.place(x = self.medidaCentroMenus_X  + 130, y = self.medidaCentroMenus_Y + espacioY * 3 * 0.9 ) 

        self.labelMes = Label(self.menuConsultarMiembros, text="Mes", font = ('Helvetica' , 9, "bold"))
        self.labelMes.place(x = self.medidaCentroMenus_X  + 190, y = self.medidaCentroMenus_Y + espacioY * 3 * 0.9 ) 

        self.labelAno = Label(self.menuConsultarMiembros, text="Año", font = ('Helvetica' , 9, "bold"))
        self.labelAno.place(x = self.medidaCentroMenus_X  + 250, y = self.medidaCentroMenus_Y + espacioY * 3 * 0.9 ) 
        
        # Lista
        self.listaDias = ttk.Combobox(self.menuConsultarMiembros, state="readonly")
        self.listaDias["values"] = [""] + [x for x in range(1, 32)]
        self.listaDias.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 3, height="35", width="50")
        self.listaDias.current(0)

        self.listaMeses = ttk.Combobox(self.menuConsultarMiembros, state="readonly")
        self.listaMeses["values"] = [""] + [x for x in range(1, 13)]
        self.listaMeses.place(x = self.medidaCentroMenus_X  + 180, y = self.medidaCentroMenus_Y + espacioY * 3, height="35", width="50")
        self.listaMeses.current(0)

        self.listaAnos = ttk.Combobox(self.menuConsultarMiembros, state="readonly")
        self.listaAnos["values"] = [""] + sorted([x for x in range(1950, int(datetime.datetime.now().year))], reverse=True)
        self.listaAnos.place(x = self.medidaCentroMenus_X  + 240, y = self.medidaCentroMenus_Y + espacioY * 3, height="35", width="50")
        self.listaAnos.current(0)

        self.listaRoles = ttk.Combobox(self.menuConsultarMiembros, state="readonly")
        self.listaRoles["values"] = ["Padrinos", "Apadrinados", "CES", "Becados", "Postulantes"]
        self.listaRoles.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 6, height="30", width="130")
        self.listaRoles.current(0)
        
        self.listaRoles.bind('<<ComboboxSelected>>', 
                             lambda event: self.listaCategorias.place(x = self.medidaCentroMenus_X  + 270, y = self.medidaCentroMenus_Y + espacioY * 6, height="30", width="130") 
                                                                     if (self.listaRoles.get() == "Apadrinados") else self.listaCategorias.place_forget())
        
        self.listaCategorias = ttk.Combobox(self.menuConsultarMiembros, state="readonly")
        self.listaCategorias["values"] = ["", "Niño", "Adulto Mayor"]
        self.listaCategorias.current(0)

        # Desactivamos los campos  
        self.campoNombreCompleto.config(state="disabled") 
        self.campoID.config(state="disabled") 
        self.campoColaboracion.config(state="disabled") 
        self.listaAnos.config(state="disabled") 
        self.listaMeses.config(state="disabled") 
        self.listaDias.config(state="disabled") 
        self.listaRoles.config(state="disabled") 
        self.listaCategorias.config(state="disabled") 

        # Boton Modificar Nombre
        
        self.botonMostrarModificarNombre = Button(self.menuConsultarMiembros, 
                                            command=lambda: self.mostrarModificar(self.botonMostrarModificarNombre, self.botonGuardarModificarNombre, self.botonCancelarModificarNombre, 
                                            self.medidaCentroMenus_X + 280 ,  self.medidaCentroMenus_Y + espacioY * 2,
                                            self.medidaCentroMenus_X + 400 ,   self.medidaCentroMenus_Y + espacioY * 2, 
                                            self.campoNombreCompleto)  
                                            ,text = "Modificar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonMostrarModificarNombre.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 2,  width = 80, height = 25)
        

        self.botonGuardarModificarNombre = Button(self.menuConsultarMiembros, 
                                                    command= lambda: self.actualizarInformacionMiembro("NombreCompleto", 
                                                    self.campoNombreCompleto, self.botonCancelarModificarNombre) ,                                                  
                                                    text = "Guardar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonCancelarModificarNombre = Button(self.menuConsultarMiembros, 
                                                    command=lambda: self.esconderBotonesModificar(self.botonMostrarModificarNombre,  
                                                    self.medidaCentroMenus_X + 280, self.medidaCentroMenus_Y + espacioY * 2, 
                                                    self.botonGuardarModificarNombre, self.botonCancelarModificarNombre, 
                                                    self.campoNombreCompleto)  
                                                    ,text = "Cancelar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       

        # Boton Modificar Fecha Nacimiento

        self.botonMostrarModificarFecha = Button(self.menuConsultarMiembros, 
                                            command=lambda: self.mostrarModificar(self.botonMostrarModificarFecha, self.botonGuardarModificarFecha, self.botonCancelarModificarFecha, 
                                            self.medidaCentroMenus_X + 300 ,  self.medidaCentroMenus_Y + espacioY * 3,
                                            self.medidaCentroMenus_X + 420 ,   self.medidaCentroMenus_Y + espacioY * 3, 
                                            self.listaAnos, self.listaDias, self.listaMeses)  
                                            ,text = "Modificar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonMostrarModificarFecha.place(x = self.medidaCentroMenus_X + 300, y = self.medidaCentroMenus_Y + espacioY * 3,  width = 80, height = 25)
        

        self.botonGuardarModificarFecha = Button(self.menuConsultarMiembros, 
                                                    command= lambda: self.actualizarFechaMiembro("FechaNacimiento", 
                                                     self.botonCancelarModificarFecha) ,                                                  
                                                    text = "Guardar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonCancelarModificarFecha = Button(self.menuConsultarMiembros, 
                                                    command=lambda: self.esconderBotonesModificar(self.botonMostrarModificarFecha,  
                                                    self.medidaCentroMenus_X + 300, self.medidaCentroMenus_Y + espacioY * 3, 
                                                    self.botonGuardarModificarFecha, self.botonCancelarModificarFecha, 
                                                    self.listaAnos, self.listaDias, self.listaMeses)   
                                                    ,text = "Cancelar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
                                                    

        # Boton Modificar ID
        
        self.botonMostrarModificarID = Button(self.menuConsultarMiembros, 
                                            command=lambda: self.mostrarModificar(self.botonMostrarModificarID, self.botonGuardarModificarID, self.botonCancelarModificarID, 
                                            self.medidaCentroMenus_X + 280 ,  self.medidaCentroMenus_Y + espacioY * 4,
                                            self.medidaCentroMenus_X + 400 ,   self.medidaCentroMenus_Y + espacioY * 4, 
                                            self.campoID)  
                                            ,text = "Modificar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonMostrarModificarID.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 4,  width = 80, height = 25)
        

        self.botonGuardarModificarID = Button(self.menuConsultarMiembros, 
                                                    command= lambda: self.actualizarInformacionMiembro("ID", 
                                                    self.campoID, self.botonCancelarModificarID) ,                                                  
                                                    text = "Guardar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonCancelarModificarID = Button(self.menuConsultarMiembros, 
                                                    command=lambda: self.esconderBotonesModificar(self.botonMostrarModificarID,  
                                                    self.medidaCentroMenus_X + 280, self.medidaCentroMenus_Y + espacioY * 4, 
                                                    self.botonGuardarModificarID, self.botonCancelarModificarID, 
                                                    self.campoID)  
                                                    ,text = "Cancelar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)


        # Boton Modificar Colaboracion
        
        self.botonMostrarModificarColaboracion = Button(self.menuConsultarMiembros, 
                                            command=lambda: self.mostrarModificar(self.botonMostrarModificarColaboracion, self.botonGuardarModificarColaboracion, self.botonCancelarModificarColaboracion, 
                                            self.medidaCentroMenus_X + 280 ,  self.medidaCentroMenus_Y + espacioY * 5,
                                            self.medidaCentroMenus_X + 400 ,   self.medidaCentroMenus_Y + espacioY * 5, 
                                            self.campoColaboracion)  
                                            ,text = "Modificar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonMostrarModificarColaboracion.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 5,  width = 80, height = 25)
        

        self.botonGuardarModificarColaboracion = Button(self.menuConsultarMiembros, 
                                                    command= lambda: self.actualizarInformacionMiembro("Colaboracion", 
                                                    self.campoColaboracion, self.botonCancelarModificarColaboracion) ,                                                  
                                                    text = "Guardar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonCancelarModificarColaboracion = Button(self.menuConsultarMiembros, 
                                                    command=lambda: self.esconderBotonesModificar(self.botonMostrarModificarColaboracion,  
                                                    self.medidaCentroMenus_X + 280, self.medidaCentroMenus_Y + espacioY * 5, 
                                                    self.botonGuardarModificarColaboracion, self.botonCancelarModificarColaboracion, 
                                                    self.campoColaboracion)  
                                                    ,text = "Cancelar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)              
        
# Funciones para menús de Consulta

    def esconderBotonesModificar(self, botonMostrar, x1, y1, button1, button2, *camposDeshabilitar):
        # Esconde button1 y button2 y muestra el boton botonMostrar
        button1.place_forget()
        button2.place_forget()
        botonMostrar.place(x = x1, y = y1, width = 80, height = 25)

        for campo in camposDeshabilitar:
            campo.config(state="disabled")

    def mostrarModificar(self, botonEsconder, button1, button2, x1, y1, x2, y2, *camposHabilitar):
        # Escode el boton botonEsconder y muestra button1 en x1,y1 y button2 en x2,y2
        if self.usuarioEncontrado:
            botonEsconder.place_forget()
            button1.place(x = x1, y = y1,  width = 80, height = 25)
            button2.place(x = x2, y = y2,  width = 80, height = 25)

            for campo in camposHabilitar:
                campo.config(state="normal")
        
        else:
            self.mostrarMensaje("Error", "Se requiere un usuario válido") 

    def escribirTextoCampo(self, campo, text): 
        estadoOriginal = campo.cget("state")
        campo.config(state="normal")    
        campo.delete(0, 'end')
        campo.insert(0, text)  
        campo.config(state = estadoOriginal)

    def buscarUsuario(self):

        informacion = obtenerInformacionUsuario(self.campoUsuario.get().strip())

        if informacion:
            self.escribirTextoCampo(self.campoNombreCompleto, informacion[0][1])
            self.escribirTextoCampo(self.campoClave, informacion[0][2])
            self.usuarioEncontrado = True
        
        else:
            self.mostrarMensaje("Error", "Usuario no encontrado")
            self.escribirTextoCampo(self.campoNombreCompleto, "")
            self.escribirTextoCampo(self.campoClave, "")
            self.usuarioEncontrado = False

    def buscarMiembro(self):
        informacion = obtenerInformacionMiembro(self.campoCedula.get().strip())

        if informacion:
            self.escribirTextoCampo(self.campoNombreCompleto, informacion[0][1])

            self.listaDias.current(int(str(informacion[0][2]).split("-")[2]))
            self.listaMeses.current(int(str(informacion[0][2]).split("-")[1]))
            self.listaAnos.current(int(datetime.datetime.now().year) -  int(str(informacion[0][2]).split("-")[0]))

            self.escribirTextoCampo(self.campoID, informacion[0][3])
            self.escribirTextoCampo(self.campoColaboracion, informacion[0][4])
        
            self.listaRoles.current(self.listaRoles.cget("values").index(informacion[0][5]))


            if self.listaRoles.get() == "Apadrinados":
                self.listaCategorias.place(x = self.medidaCentroMenus_X  + 270, y = self.medidaCentroMenus_Y + 80 * 6, height="30", width="130") 
                self.listaCategorias.current(self.listaCategorias.cget("values").index(informacion[0][6]))
            
            else:
                self.listaCategorias.place_forget()

            self.usuarioEncontrado = True
        
        else:
            self.mostrarMensaje("Error", "Miembro no encontrado")
            self.escribirTextoCampo(self.campoNombreCompleto, "")

            self.listaDias.current(0)
            self.listaMeses.current(0)
            self.listaAnos.current(0)

            self.escribirTextoCampo(self.campoID, "")
            self.escribirTextoCampo(self.campoColaboracion, "")
            self.listaRoles.current(0)
            self.usuarioEncontrado = False


    def actualizarInformacionUsuario(self, columna, campoNuevoDato, botonCancelar):
        resultado = actualizarInformacionUsuario(self.campoUsuario.get().strip(), columna, campoNuevoDato.get().strip())

        if resultado:
            botonCancelar.invoke()
            self.mostrarMensaje("Exito", "Cambios Realizados") 
        
        else:
            self.mostrarMensaje("Error", "Un error ocurrió, inténtelo de nuevo") 
        return None

    def actualizarInformacionMiembro(self, columna, campoNuevoDato, botonCancelar):
        resultado = actualizarInformacionMiembro(self.campoCedula.get().strip(), columna, campoNuevoDato.get().strip())
        
        if resultado:
            botonCancelar.invoke()
            self.mostrarMensaje("Exito", "Cambios Realizados") 
        
        else:
            self.mostrarMensaje("Error", "Un error ocurrió, inténtelo de nuevo") 
    
        return None

    def actualizarFechaMiembro(self, columna, botonCancelar):
        fecha = self.listaAnos.get() + "-" + self.listaMeses.get() + "-" + self.listaDias.get()
        resultado = actualizarInformacionMiembro(self.campoCedula.get().strip(), columna, fecha)
        
        if resultado:
            botonCancelar.invoke()
            self.mostrarMensaje("Exito", "Cambios Realizados") 
        
        else:
            self.mostrarMensaje("Error", "Un error ocurrió, inténtelo de nuevo") 
    
        return None

    def borrarUsuario(self):
        if self.usuarioEncontrado:

            mensajeConfirmacion = messagebox.askquestion('Borrar Usuario','Está seguro de borrar este usuario?', icon = 'warning')

            if mensajeConfirmacion == "yes":
                borrarUsuario(self.campoUsuario.get().strip())
                self.mostrarMensaje("Exito", "Usuario eliminado con éxito")

        
        else:
            self.mostrarMensaje("Error", "Se requiere un usuario valido")

    def borrarMiembro(self):
        if self.usuarioEncontrado:

            mensajeConfirmacion = messagebox.askquestion('Borrar Miembro','Está seguro de borrar este miembro?', icon = 'warning')

            if mensajeConfirmacion == "yes":
                borrarUsuario(self.campoUsuario.get().strip())
                self.mostrarMensaje("Exito", "Miembro eliminado con éxito")
   
        else:
            self.mostrarMensaje("Error", "Se requiere un miembro valido")
# Funciones para menús de Creación de Usuarios y Miembros

    def crearUsuario(self):
        if self.campoClave.get().strip() == "" or self.campoClave.get().strip() == " " or self.campoClave.get() == False:
            self.mostrarMensaje("Error","Coloque una contraseña por favor")


        elif len(self.campoClave.get().strip()) < 4:
            self.mostrarMensaje("Error","Coloque una contraseña con 4 o más caracteres")
        
        else:

            if verificarUsuario(self.campoUsuario.get()) == False: ## si usuario NO existe
                 
                resultado = agregarUsuario(self.campoNombreCompleto.get(), self.campoUsuario.get(), self.campoClave.get() ,self.listaRoles.get())
                
                if resultado:
                    self.mostrarMensaje("Exito","Usuario creado con éxito")
                    self.limpiarFormulario(self.campoNombreCompleto, self.campoClave, self.campoUsuario)

                else: 
                    self.mostrarMensaje("Error","Ocurrió un error, inténtelo de nuevo")
    
            else:
                self.mostrarMensaje("Error","Ya existe un usuario registrado")

    def crearMiembro(self):

        # Verificacion de campos
        if self.campoNombreCompleto.get().strip() == "" or self.campoNombreCompleto.get().strip() == " " or self.campoNombreCompleto.get() == False:
            self.mostrarMensaje("Error","Coloque un nombre y apellidos por favor")
            return

        elif self.campoCedula.get().strip() == "" or self.campoCedula.get().strip() == " " or self.campoCedula.get() == False:
            self.mostrarMensaje("Error","Coloque una cédula")
            return

        elif self.campoID.get().strip() == "" or self.campoID.get().strip() == " " or self.campoID.get() == False:
            self.mostrarMensaje("Error","Coloque un ID")
            return

        elif self.campoColaboracion.get().strip() == "" or self.campoColaboracion.get().strip() == " " or self.campoColaboracion.get() == False:
            self.mostrarMensaje("Error","Coloque un monto de colaboración")
            return
        
        elif self.listaAnos.current() == 0 or self.listaMeses.current() == 0 or self.listaDias.current() == 0:
            self.mostrarMensaje("Error", "Fecha incorrecta, verificar")
            return

        
        elif self.listaRoles.get() == "Apadrinados" and self.listaCategorias.current() == 0:
            self.mostrarMensaje("Error", "Escoja una categoria para el apadrinado")
            return 

        ## Verificar que monto colaboracion sea numero

        try:
            valorColaboracion = int(self.campoColaboracion.get().strip())

        except: 
            self.mostrarMensaje("Error","Monto de colaboración tiene que ser numérico")
            return

        else:

            if verificarMiembro(self.campoCedula.get()) == False: ## si miembro NO existe

                fecha = self.listaAnos.get() + "-" + self.listaMeses.get() + "-" + self.listaDias.get()
                resultado = agregarMiembro(self.campoNombreCompleto.get(), self.campoCedula.get(), fecha, self.campoID.get(),
                                                self.campoColaboracion.get(), self.listaRoles.get(), self.listaCategorias.get())
                
                if resultado:
                    self.mostrarMensaje("Exito","Usuario creado con éxito")
                    self.limpiarFormulario(self.campoNombreCompleto, self.campoColaboracion, self.campoID, self.campoCedula)

                    # Restablecer listas
                    self.listaRoles.current(0)
                    self.listaCategorias.current(0)
                    self.listaDias.current(0)
                    self.listaMeses.current(0)
                    self.listaAnos.current(0)

                else: 
                    self.mostrarMensaje("Error","Ocurrió un error, inténtelo de nuevo")
    
            else:
                self.mostrarMensaje("Exito","Ya existe un miembro registrado con la cédula")
        
    def prueba(self):
        None

# Funciones extra         
    def limpiarFormulario(self, *campos):
        for campo in campos:
            campo.delete(0,'end')
 
    def mostrarMensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

Inicio()


