from tkinter import *
import tkinter.font as TkFont
from Utilidades import * 
from tkinter import messagebox


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


        self.labelUsuarios = Label(self.barraLateral ,text = "Usuarios",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.labelUsuarios.place(x = 40, y = 140)

        # Botones menu usuario
        self.botonMenuUsuarios1 = Button(self.barraLateral, command = self.mostrarMenuCrearUsuarios ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuUsuarios1.place(x = 40, y = 160)

        self.botonMenuUsuarios4 = Button(self.barraLateral, command = self.mostrarMenuConsultarUsuarios ,text = "Consultar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuUsuarios4.place(x = 40, y = 180)


        ####
        self.boton2 = Button(self.barraLateral, text = "prueba",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
        self.boton2.place(x = 40, y = 250)

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

        
        self.labelNombreCompleto.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.labelUsuario.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 2) 
        self.labelClave.place(x = self.medidaCentroMenus_X  - 30, y = self.medidaCentroMenus_Y + espacioY * 3) 

        # Campos
        self.campoNombreCompleto = Entry(self.menuCrearUsuarios, justify="left", name = "campoNombreCompleto", font = ('Helvetica' , 10, "bold"))
        self.campoUsuario = Entry(self.menuCrearUsuarios, justify="left", name = "campoUsuario", font = ('Helvetica' , 10, "bold"))
        self.campoClave = Entry(self.menuCrearUsuarios, justify="left", name = "campoClave", font = ('Helvetica' , 10, "bold"), show="*")

        self.campoNombreCompleto.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 1)
        self.campoUsuario.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 2)
        self.campoClave.place(x = self.medidaCentroMenus_X  + 120, y = self.medidaCentroMenus_Y + espacioY * 3)

        self.campoClave.config(state="normal")

        # Asignar dinamicamente eventos a cada label creado
        ##self.label1.bind("<Button-1>", lambda event, label = self.label1 : print(label)
        
        # Botones
        self.botonCrearUsuario = Button(self.menuCrearUsuarios, command=self.crearUsuario ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonCrearUsuario.place(x = self.medidaCentroMenus_X - 30 , y = self.medidaCentroMenus_Y + espacioY * 4,  width = 130, height = 30)

        self.botonLimpiarFormulario = Button(self.menuCrearUsuarios, command= lambda : self.limpiarFormulario(self.campoNombreCompleto, self.campoClave, self.campoUsuario)  ,text = "Limpiar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonLimpiarFormulario.place(x = self.medidaCentroMenus_X + 120 , y = self.medidaCentroMenus_Y + espacioY * 4,  width = 130, height = 30)


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

        # Asignar dinamicamente eventos a cada label creado
        ##self.label1.bind("<Button-1>", lambda event, label = self.label1 : print(label)
        
        # Botones
        self.botonBuscarUsuario = Button(self.menuConsultarUsuarios, command=self.buscarUsuario ,text = "Buscar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonBuscarUsuario.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 1,  width = 80, height = 25)
        
        # Boton Modificar Nombre


        self.botonMostrarModificar = Button(self.menuConsultarUsuarios, 
                                            command=lambda: self.mostrarModificar(self.botonMostrarModificar, self.botonGuardarModificarNombre, self.botonCancelarGuardarModificarNombre, 
                                            self.medidaCentroMenus_X + 280 ,  self.medidaCentroMenus_Y + espacioY * 2,
                                            self.medidaCentroMenus_X + 400 ,   self.medidaCentroMenus_Y + espacioY * 2, 
                                            self.campoNombreCompleto)  
                                            ,text = "Modificar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonMostrarModificar.place(x = self.medidaCentroMenus_X + 280, y = self.medidaCentroMenus_Y + espacioY * 2,  width = 80, height = 25)


        self.botonGuardarModificarNombre = Button(self.menuConsultarUsuarios, 
                                                    command= lambda: self.actualizarInformacionUsuario("NombreCompleto", 
                                                    self.campoNombreCompleto, self.botonCancelarGuardarModificarNombre) ,                                                  
                                                    text = "Guardar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
       
        self.botonCancelarGuardarModificarNombre = Button(self.menuConsultarUsuarios, 
                                                    command=lambda: self.esconderBotonesModificar(self.botonMostrarModificar,  
                                                    self.medidaCentroMenus_X + 280, self.medidaCentroMenus_Y + espacioY * 2, 
                                                    self.botonGuardarModificarNombre, self.botonCancelarGuardarModificarNombre, 
                                                    self.campoNombreCompleto)  
                                                    ,text = "Cancelar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        

         # Boton Modificar Contraseña

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


