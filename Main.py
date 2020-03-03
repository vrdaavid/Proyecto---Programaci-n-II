from tkinter import *
import tkinter.font as TkFont
from Utilidades import * 
from tkinter import messagebox
from tkinter import ttk


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

        self.botonMenuMiembros2 = Button(self.barraLateral, command = self.mostrarMenuConsultarUsuarios ,text = "Consultar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuMiembros2.place(x = 40, y = 290)


        ###
        self.boton3 = Button(self.barraLateral, text = "prueba",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
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
        self.listaRoles["values"] = ["end", "hola", "adios"]
        self.listaRoles.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 4, height="30", width="130")
        self.listaRoles.current(0)

        # Asignar dinamicamente eventos a cada label creado
        ##self.label1.bind("<Button-1>", lambda event, label = self.label1 : print(label)
        
        # Botones
        self.botonCrearUsuario = Button(self.menuCrearUsuarios, command=self.crearUsuario ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonCrearUsuario.place(x = self.medidaCentroMenus_X - 30 , y = self.medidaCentroMenus_Y + espacioY * 5,  width = 130, height = 30)

        self.botonLimpiarFormulario = Button(self.menuCrearUsuarios, command= lambda : self.limpiarFormulario(self.campoNombreCompleto, self.campoClave, self.campoUsuario)  ,text = "Limpiar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonLimpiarFormulario.place(x = self.medidaCentroMenus_X + 120 , y = self.medidaCentroMenus_Y + espacioY * 5,  width = 130, height = 30)

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
        self.labelCedula = Label(self.menuCrearMiembros, text="Usuario", name = "labelCedula" , font = ('Helvetica' , 10, "bold"))
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

        #roles = obtenerRoles()

        # Lista
        self.listaRoles = ttk.Combobox(self.menuCrearMiembros, state="readonly")
        self.listaRoles["values"] = ["Apadrinados", "Padrinos", "CES", "Becados", "Postulantes"]
        self.listaRoles.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 6, height="30", width="130")
        self.listaRoles.current(0)

        # Botones
        self.botonCrearUsuario = Button(self.menuCrearMiembros, command=self.crearUsuario ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonCrearUsuario.place(x = self.medidaCentroMenus_X - 30 , y = self.medidaCentroMenus_Y + espacioY * 7,  width = 130, height = 30)

        self.botonLimpiarFormulario = Button(self.menuCrearMiembros, command= lambda : self.limpiarFormulario(self.campoNombreCompleto, self.campoClave, self.campoUsuario)  ,text = "Limpiar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonLimpiarFormulario.place(x = self.medidaCentroMenus_X + 120 , y = self.medidaCentroMenus_Y + espacioY * 7,  width = 130, height = 30)

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
                                                    command=lambda: print("borrar")
                                                    ,text = "Borrar",  bg = self.colorError, fg = "white",  relief = "flat", font = self.estiloBoton)

        self.botonBorrarUsuario.place(x = self.medidaCentroMenus_X + 50, y = self.medidaCentroMenus_Y + espacioY * 4,  width = 200, height = 25)  

    def mostrarMenuConsultarMiembros(self): 
        self.eliminarMenus()
        self.menuCrearMiembros = Canvas(self.raiz, width = 800, height = 720, bg = "#ecf0f1", highlightthickness=0, relief='ridge')
        self.menuCrearMiembros.pack()
        self.pantallas.append(self.menuConsultarUsuarios)
        titulo = " " * (22 - len("MIEMBROS")) + "MIEMBROS"
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
                                                    command=lambda: print("borrar")
                                                    ,text = "Borrar",  bg = self.colorError, fg = "white",  relief = "flat", font = self.estiloBoton)

        self.botonBorrarUsuario.place(x = self.medidaCentroMenus_X + 50, y = self.medidaCentroMenus_Y + espacioY * 4,  width = 200, height = 25)              

    def esconderBotonesModificar(self, botonMostrar, x1, y1, button1, button2, campoDeshabilitar):
        # Esconde button1 y button2 y muestra el boton botonMostrar
        button1.place_forget()
        button2.place_forget()
        botonMostrar.place(x = x1, y = y1, width = 80, height = 25)
        campoDeshabilitar.config(state="disabled")

    def mostrarModificar(self, botonEsconder, button1, button2, x1, y1, x2, y2, campoHabilitar):
        # Escode el boton botonEsconder y muestra button1 en x1,y1 y button2 en x2,y2
        if self.usuarioEncontrado:
            botonEsconder.place_forget()
            button1.place(x = x1, y = y1,  width = 80, height = 25)
            button2.place(x = x2, y = y2,  width = 80, height = 25)
            campoHabilitar.config(state="normal")
        
        else:
            ##self.mostrarMensajeErr(self.menuConsultarUsuarios, "Se requiere un usuario valido", 350, 500)
            self.mostrarMensaje("Error", "Se requiere un usuario valido") 
    
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
            # self.mostrarMensajeErr(self.menuConsultarUsuarios, "Usuario no encontrado", 350, 500)
            self.mostrarMensaje("Error", "Usuario no encontrado")
            self.escribirTextoCampo(self.campoNombreCompleto, "")
            self.escribirTextoCampo(self.campoClave, "")
            self.usuarioEncontrado = False
        
    def actualizarInformacionUsuario(self, columna, campoNuevoDato, botonCancelar):
        actualizarInformacionUsuario(self.campoUsuario.get().strip(), columna, campoNuevoDato.get().strip())
        botonCancelar.invoke()
        #self.mostrarMensajeExito(self.menuConsultarUsuarios, "Cambios Realizados", 350, 500)  
        self.mostrarMensaje("Exito", "Cambios Realizados") 
    
        return None

    def crearUsuario(self):
        if self.campoClave.get().strip() == "" or self.campoClave.get().strip() == " " or self.campoClave.get() == False:
            print ("Coloque una contraseña por favor")


        elif len(self.campoClave.get().strip()) < 4:
            print("Coloque una contraseña con 4 o más caracteres")
        
        else:

            if verificarUsuario(self.campoUsuario.get()) == False: ## si usuario NO existe
                 
                resultado = agregarUsuario(self.campoNombreCompleto.get(), self.campoUsuario.get(), self.campoClave.get() ,None)
                
                if resultado:
                    print ("Usuario registrado")
                    self.limpiarFormulario(self.campoNombreCompleto, self.campoClave, self.campoUsuario)

                else: 
                    print("Un error ocurrió, intentelo nuevamente")
    
            else:
                print("Ya existe un usuario")
            

    def limpiarFormulario(self, *campos):
        for campo in campos:
            campo.delete(0,'end')
         
 
    def mostrarMensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

Inicio()


