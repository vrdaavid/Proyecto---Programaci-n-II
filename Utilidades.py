def ingresar(pUsuario, pClave):
    ## Codigo conexion a MySQL
    
    ##if command.execute("select 1 from Usuarios where nombreUsuario = '", pUsuario, "' and clave= '", pClave, "'"):
    ##   return True

    if pUsuario == "" and pClave == "":
        return True
    
    else:
        return False