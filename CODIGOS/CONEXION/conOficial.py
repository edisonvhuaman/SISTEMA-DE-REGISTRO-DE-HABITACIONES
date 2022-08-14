import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect (
            host = 'localhost', 
            user = 'root',
            password = 'edison',
            db = 'al3',
            port = 3334
        )

        self.cursor = self.connection.cursor()
        print('Conexion establecida exitosamente')

    def select_user(self, id):
        sql = 'SELECT * FROM CLIENTES WHERE id_cliente = "{}";'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print('ID: ', user[0])
            print('HABITACION: ', user[1])
            print('NOMBRE: ', user[2])

        except Exception as e:
            raise

database = Database()
database.select_user('C001')