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
    
def verificarMiembro(pCedula):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM Miembros WHERE Cedula ='{0}'".format(pCedula)
    
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
    sql = "INSERT INTO Usuarios (NombreCompleto,NombreUsuario, Clave, Rol) values ('{0}', '{1}', '{2}', '{3}')".format(pNombre, pUsuario ,pClave, pRol)
    
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

def agregarMiembro(pNombre, pCedula,  pFechaNacimiento, pID, pColaboracion, pTipo, pCategoriaApadrinado):

    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.

    sql = "INSERT INTO Miembros values ('{0}', '{1}', STR_TO_DATE('{2}', '%Y-%m-%d'), '{3}', {4}, '{5}', '{6}')".format(pNombre, pCedula,  pFechaNacimiento, pID, pColaboracion, pTipo, pCategoriaApadrinado)
    
    try:
        
        # Ejecutar el comando SQL 
        cursor.execute(sql)

        # Guardar cambios
        db.commit()
 
        # desconectar del servidor
        db.close()
        
        return True


    except Exception as e:
        # Rollback in case there is any error
        db.rollback()
        print(e)
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

def obtenerInformacionMiembro(pCedula):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT Cedula, NombreCompleto, FechaNacimiento, ID, Colaboracion, TipoMiembro, TipoApadrinado  FROM Miembros WHERE Cedula ='{0}'".format(pCedula)
    
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

def actualizarInformacionMiembro(pCedula, pColumna, nuevoDato):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "UPDATE Miembros SET {0} = '{1}' WHERE Cedula = '{2}'".format(pColumna, nuevoDato, pCedula)   
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

def actualizarFechaMiembro(pCedula, pColumna, nuevoDato):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "UPDATE Miembros SET {0} = STR_TO_DATE('{1}', '%Y-%m-%d') WHERE Cedula = '{2}'".format(pColumna, nuevoDato, pCedula)  
  
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

def borrarUsuario(pUsuario):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "DELETE FROM Usuarios WHERE NombreUsuario = '{0}'".format(pUsuario)  
  
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

def obtenerCumpleanos(pMes, pDia):
    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.


    sql = "SELECT NombreCompleto, FechaNacimiento, Cedula, TipoMiembro FROM Miembros WHERE DAY(FechaNacimiento) = {0} AND MONTH(FechaNacimiento) = {1}".format(pDia, pMes)

    try:
        
        result = cursor.execute(sql)

        # Ejecutar el comando SQL 
        results = cursor.fetchall()

        # Guardar cambios
        db.commit()
            
        # desconectar del servidor
        db.close()

        if result != 0: # Si es 1, es porque el select trajo datos
            return results
    
        else:
            return []

    except:
        # Rollback in case there is any error
        db.rollback()
        return []
