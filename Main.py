from tkinter import *
import tkinter.font as TkFont
from Utilidades import * 

class Inicio:
    # atributos de la clase Inicio, acá se colocan todas las variables globales dentro del código para poder parametrizar tamaños, colores, etc
    colorPanel = "#273c75"
    colorError = "#d63031"
    pantallas = []
    medidaCentroMenus_X = 260
    medidaCentroMenus_Y = 100

    def __init__(self, master = None):

        ## Inicializar aplicación padre de Tkinter, raíz será la aplicación donde se colocarán todos los canvas (ventanas)
        self.raiz = Tk()

        # Tamaños estándar de letra para ser usados en los labels
        self.estiloBoton = TkFont.Font(self.raiz, family='Helvetica', size=12, weight="bold")
        self.estiloLabel = TkFont.Font(self.raiz, family='Helvetica', size=16, weight="bold")
        self.estiloError = TkFont.Font(self.raiz, family='Helvetica', size=10, weight="bold")

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
            self.errorLogin = Label(self.pantallaLogin, text="Usuario / Contraseña incorrecta", fg = self.colorError, font = self.estiloError)
            self.errorLogin.place(x = 450, y = 450)

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

        self.botonMenuUsuarios2 = Button(self.barraLateral, command = self.mostrarMenuCrearUsuarios ,text = "Eliminar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuUsuarios2.place(x = 40, y = 180)

        self.botonMenuUsuarios3 = Button(self.barraLateral, command = self.mostrarMenuCrearUsuarios ,text = "Modificar",  bg = self.colorPanel, fg = "white",  relief = "flat", font = ('Helvetica' , 8))
        self.botonMenuUsuarios3.place(x = 40, y = 200)


        ####
        self.boton2 = Button(self.barraLateral, text = "prueba",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
        self.boton2.place(x = 40, y = 240)

        self.boton3 = Button(self.barraLateral, text = "prueba",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
        self.boton3.place(x = 40, y = 340)

        self.boton3 = Button(self.barraLateral, text = "prueba",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
        self.boton3.place(x = 40, y = 440)

        self.boton4 = Button(self.barraLateral, command = self.salirMenuPrincipal, text = "Salir",  bg = self.colorPanel,  fg = "white",   relief = "flat", font = self.estiloBoton)
        self.boton4.place(x = 40, y = 540)


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

        encabezadosUsuario = ["Nombre Completo", "Usuario", "Contraseña: "]

        espacioY = 80
        id = 1
        for campo in encabezadosUsuario:
            self.label1 = Label(self.menuCrearUsuarios, text=campo, name = "campoLabel " + str(id), font = ('Helvetica' , 10, "bold"))
            self.campoUsuario = Entry(self.menuCrearUsuarios, justify="left", name = "campoEntry " + str(id), font = ('Helvetica' , 10, "bold"))

            self.label1.place(x = self.medidaCentroMenus_X  - 100, y = self.medidaCentroMenus_Y + espacioY)
            self.campoUsuario.place(x = self.medidaCentroMenus_X  + 100, y = self.medidaCentroMenus_Y + espacioY)
            
            # Asignar dinamicamente eventos a cada label creado
            ##self.label1.bind("<Button-1>", lambda event, label = self.label1 : print(label)
            #       
            espacioY += 70
            id += 1
          
        self.botonCrearUsuario = Button(self.menuCrearUsuarios, command=self.hola ,text = "Crear",  bg = self.colorPanel, fg = "white",  relief = "flat", font = self.estiloBoton)
        self.botonCrearUsuario.place(x = self.medidaCentroMenus_X, y = self.medidaCentroMenus_Y + espacioY)
    
    def hola(self):
        print("jeje")

Inicio()


