def ingresar(pUsuario, pClave):
    ## Codigo conexion a MySQL
    
    ##if command.execute("select 1 from Usuarios where nombreUsuario = '", pUsuario, "' and clave= '", pClave, "'"):
    ##   return True

    if pUsuario == "" and pClave == "":
        return True
    
    else:
        return False
    

def verificarUsuario(pUsuario):
    ## Codigo conexion a MySQL
    
    ##if command.execute("select 1 from Usuarios where nombreUsuario = '", pUsuario, "' and clave= '", pClave, "'"):
    ##   return True

    if pUsuario == 'vrdaavid':
        return False
    
    else: 
        return True
    
def agregarUsuario(pUsuario, pClave, pNombre, pRol):
    # Codigo conexion a MySQL
    
    ##command.execute("insert into Usuarios values (bla bla bla)")