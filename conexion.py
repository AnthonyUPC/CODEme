
import sqlite3

class Registro_datos():

    def __init__(self):
        self.conexion = sqlite3.connect(database ='base.db')


    def inserta_producto(self,codpro, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni):
        cur = self.conexion.cursor()
        sql='''INSERT INTO productos (CODPRO, DESCRIPCION, DETALLE, UNIDAD, CANTIDAD, FECPRO, LOTE, FECVEN, COSTOUNI) 
        VALUES('{}', '{}','{}', '{}','{}','{}','{}','{}','{}')'''.format(codpro, descripcion, detalle, unidad, cantidad,fecpro, lote, fecven, costouni)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    
    def inserta_movimiento(self, codpro, tipmov, nummov, fecmov, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni):
        cur = self.conexion.cursor()
        sql='''INSERT INTO movimiento (CODPRO,TIPMOV, NUMMOV, FECMOV, DESCRIPCION, DETALLE, UNIDAD, CANTIDAD, FECPRO, LOTE, FECVEN, COSTOUNI) 
        VALUES('{}', '{}','{}', '{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(codpro, tipmov, nummov, fecmov, descripcion, detalle, unidad, cantidad,fecpro, lote, fecven, costouni)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
    
    def mostrar_movimientos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM movimiento " 
        cursor.execute(sql)
        registros = cursor.fetchall()
        return registros
    
    def busca_producto(self, codpro_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE CODPRO = {}".format(codpro_producto)
        cur.execute(sql)
        codproX = cur.fetchall()
        cur.close()     
        return codproX 

    def actualiza_productos(self,Id, codpro, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni):
        cur = self.conexion.cursor()
        sql ='''UPDATE productos SET  CODPRO ='{}', DESCRIPCION = '{}' , DETALLE = '{}', UNIDAD = '{}', CANTIDAD = '{}', FECPRO = '{}', LOTE = '{}', FECVEN = '{}', COSTOUNI = '{}'
        WHERE ID = '{}' '''.format(codpro, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni, Id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a
    