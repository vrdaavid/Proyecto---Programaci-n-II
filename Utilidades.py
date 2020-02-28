import pymysql

def ingresar(pUsuario, pClave):

    db = pymysql.connect("localhost","root","1234","proyectoprogramacionii")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM Usuarios WHERE NombreUsuario ='{0}' AND CLAVE = '{1}'".format(pUsuario, pClave)
    
    try:
    # Execute the SQL command
        result = cursor.execute(sql)
        # Commit your changes in the database
        db.commit()

        if result == 1:
            return True
    
        else:
            return False
        
        
        # desconectar del servidor
        db.close()

    except:
        # Rollback in case there is any error
        db.rollback()



  
def verificarUsuario(pUsuario):
    if pUsuario == 'vrdaavid':  # Usuario ya existe
        return False
    
    else: 
        return True
    
def agregarUsuario(pUsuario, pClave, pNombre, pRol):
    # Codigo conexion a MySQL
    return None 
    #command.execute("insert into Usuarios values (bla bla bla)")