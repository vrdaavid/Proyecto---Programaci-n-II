import pymysql

def ingresar(pUsuario, pClave):

    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM Usuarios WHERE NombreUsuario ='{0}' AND CLAVE = '{1}'".format(pUsuario, pClave)
    
    try:
        
        # Ejecutar el comando SQL 
        result = cursor.execute(sql)

        # Guardar cambios
        db.commit()
        
        # desconectar del servidor
        db.close()

        
        if result == 1: # Si es 1, es porque el select trajo datos
            return True
    
        else:
            return False
        

    except:
        # Rollback in case there is any error
        db.rollback()
        return False

  
def verificarUsuario(pUsuario):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM Usuarios WHERE NombreUsuario ='{0}'".format(pUsuario)
    
    try:
        
        # Ejecutar el comando SQL 
        result = cursor.execute(sql)

        # Guardar cambios
        db.commit()
            
        # desconectar del servidor
        db.close()

        if result == 1: # Si es 1, es porque el select trajo datos
            return True
    
        else:
            return False

    except:
        # Rollback in case there is any error
        db.rollback()
        return False
    
def agregarUsuario(pNombre, pUsuario, pClave, pRol):

    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO Usuarios (NombreCompleto,NombreUsuario, Clave) values ('{0}', '{1}', '{2}')".format(pNombre, pUsuario ,pClave)
    
    try:
        
        # Ejecutar el comando SQL 
        cursor.execute(sql)

        # Guardar cambios
        db.commit()
 
        # desconectar del servidor
        db.close()
        
        return True


    except:
        # Rollback in case there is any error
        db.rollback()
        return False

def obtenerInformacionUsuario(pUsuario):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT NombreUsuario, NombreCompleto, Clave  FROM Usuarios WHERE NombreUsuario ='{0}'".format(pUsuario)
    
    try:
        
        result = cursor.execute(sql)

        # Ejecutar el comando SQL 
        results = cursor.fetchall()

        # Guardar cambios
        db.commit()
            
        # desconectar del servidor
        db.close()

        if result == 1: # Si es 1, es porque el select trajo datos
            return results
    
        else:
            return []

    except:
        # Rollback in case there is any error
        db.rollback()
        return []

def actualizarInformacionUsuario(pUsuario, pColumna, nuevoDato):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "UPDATE Usuarios SET {0} = '{1}' WHERE NombreUsuario = '{2}'".format(pColumna, nuevoDato, pUsuario)   
    try:
        
        # Ejecutar el comando SQL 
        cursor.execute(sql)

        # Guardar cambios
        db.commit()
 
        # desconectar del servidor
        db.close()
        
        return True


    except:
        # Rollback in case there is any error
        db.rollback()
        return False

