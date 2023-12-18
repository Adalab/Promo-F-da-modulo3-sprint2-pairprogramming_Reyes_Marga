query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `pair_12`;"

query_tabla_ventas = """
                        CREATE TABLE IF NOT EXISTS `pair_12`.`Ventas` (
                        `ID_Venta` INT NOT NULL AUTO_INCREMENT,
                        `ID_Cliente` VARCHAR(100) NOT NULL,
                        `ID_Producto` VARCHAR(100) NOT NULL,
                        `Fecha_Venta` DATETIME NOT NULL,
                        `Cantidad` INT NOT NULL,
                        `Total` FLOAT NOT NULL,
                        PRIMARY KEY (`ID_Venta`))
                                                     """
query_insertar_ventas = "INSERT INTO Ventas (ID_Cliente, ID_Producto,Fecha_Venta,Cantidad,Total) VALUES (%s, %s, %s, %s, %s)"
