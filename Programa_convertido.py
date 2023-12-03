from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'mysql+pymysql://adminsgc:C0c41n4@localhost/sgc'

Base = declarative_base()

class Proveedor(Base):
    __tablename__ = 'proveedores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    ubicacion = Column(String(255), nullable=False)
    clasificacion = Column(String(255), nullable=False)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    tipo = Column(String(255), nullable=False)
    cantidad = Column(String(255), nullable=False)

class Distribuidor(Base):
    __tablename__ = 'distribuidores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    ubicacion = Column(String(255), nullable=False)
    clasificacion = Column(String(255), nullable=False)

# Crear motor y conectarse a la base de datos
engine = create_engine(DB_URL, echo=True)
Base.metadata.create_all(bind=engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("\n====SGC=====")
    print("1. Eliminar")
    print("2. Crear")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Salir")
#    print("0. Crear Base de Datos")
    print("999. PANICO")

    try:
        opcion = int(input("\nOpcion: "))
    except ValueError:
        opcion = 1000

    if opcion == 1:
        print("\nEliminar")
        while True:
            print("\n1. Eliminar producto")
            print("2. Eliminar proveedor")
            print("3. Eliminar distribuidor")
            print("4. Regresar al menu principal")
            try:
                opcion = int(input("\nOpcion: "))
            except ValueError:
                opcion = 0

            if opcion == 1:
                productos = session.query(Producto).all()
                for producto in productos:
                    print(f"{producto.id}. {producto.nombre}")
                try:
                    por_eliminar = int(input("Inserte ID del PRODUCTO a borrar... "))
                except ValueError:
                    por_eliminar = 999999
                producto = session.query(Producto).get(por_eliminar)
                if producto:
                    session.delete(producto)
                    session.commit()
                else:
                    print("ID de producto no válido.")
            elif opcion == 2:
                proveedores = session.query(Proveedor).all()
                for proveedor in proveedores:
                    print(f"{proveedor.id}. {proveedor.nombre}")
                try:
                    por_eliminar = int(input("Inserte ID del PROVEEDOR a borrar... "))
                except ValueError:
                    por_eliminar = 999999
                proveedor = session.query(Proveedor).get(por_eliminar)
                if proveedor:
                    session.delete(proveedor)
                    session.commit()
                else:
                    print("ID de proveedor no válido.")
            elif opcion == 3:
                distribuidores = session.query(Distribuidor).all()
                for distribuidor in distribuidores:
                    print(f"{distribuidor.id}. {distribuidor.nombre}")
                try:
                    por_eliminar = int(input("Inserte ID del DISTRIBUIDOR a borrar... "))
                except ValueError:
                    por_eliminar = 999999
                distribuidor = session.query(Distribuidor).get(por_eliminar)
                if distribuidor:
                    session.delete(distribuidor)
                    session.commit()
                else:
                    print("ID de distribuidor no válido.")
            elif opcion == 4:
                print("Regresando al menú principal🤷")
                break
            else:
                print("ERR::Opcion no valida")
    elif opcion == 2:
        print("\nCrear")
        while True:
            print("\n1. Crear producto")
            print("2. Crear proveedor")
            print("3. Crear distribuidor")
            print("4. Regresar al menu principal")
            try:
                opcion_creacion = int(input("\nOpcion: "))
            except ValueError:
                opcion_creacion = 0

            if opcion_creacion == 1:
                id_producto = input("ID del producto: ")
                nombre_producto = input("Nombre del producto: ")
                tipo_producto = input("Tipo del producto: ")
                cantidad_producto = input("Cantidad del producto: ")

                nuevo_producto = Producto(
                    id=int(id_producto),
                    nombre=nombre_producto,
                    tipo=tipo_producto,
                    cantidad=int(cantidad_producto)
                )

                session.add(nuevo_producto)
                session.commit()

            elif opcion_creacion == 2:
                id_proveedor = input("ID del proveedor: ")
                nombre_proveedor = input("Nombre del proveedor: ")
                ubicacion_proveedor = input("Ubicacion del proveedor: ")
                clasificacion_proveedor = input("Clasificacion del proveedor: ")

                nuevo_proveedor = Proveedor(
                    id=int(id_proveedor),
                    nombre=nombre_proveedor,
                    ubicacion=ubicacion_proveedor,
                    clasificacion=clasificacion_proveedor
                )

                session.add(nuevo_proveedor)
                session.commit()

            elif opcion_creacion == 3:
                # Lógica para crear un distribuidor (similar a la lógica de producto y proveedor)
                id_distribuidor = input("ID del distribuidor: ")
                nombre_distribuidor = input("Nombre del distribuidor: ")
                ubicacion_distribuidor = input("Ubicacion del distribuidor: ")
                clasificacion_distribuidor = input("Clasificacion del distribuidor: ")

                nuevo_distribuidor = distribuidor(
                    id=int(id_distribuidor),
                    nombre=nombre_distribuidor,
                    ubicacion=ubicacion_distribuidor,
                    clasificacion=clasificacion_distribuidor
                )

                session.add(nuevo_distribuidor)
                session.commit()
                
            elif opcion_creacion == 4:
                print("Regresando al menú principal🤷")
                break

            else:
                print("ERR::Opcion no valida")
    elif opcion == 3:
        print("\nBuscar")
        while True:
            print("\n1. Buscar producto")
            print("2. Buscar proveedor")
            print("3. Buscar distribuidor")
            print("4. Regresar al menu principal")
            try:
                opcion_busqueda = int(input("\nOpcion: "))
            except ValueError:
                opcion_busqueda = 0

            if opcion_busqueda == 1:
                productos = session.query(Producto).all()
                for producto in productos:
                    print(producto.nombre)

            elif opcion_busqueda == 2:
                proveedores = session.query(Proveedor).all()
                for proveedor in proveedores:
                    print(proveedor.nombre)

            elif opcion_busqueda == 3:
                distribuidores = session.query(Distribuidor).all()
                for distribuidor in distribuidores:
                    print(distribuidor.nombre)

            elif opcion_busqueda == 4:
                print("Regresando al menú principal🤷")
                break

            else:
                print("ERR::Opcion no valida")
    elif opcion == 4:
        print("\nActualizar")
        while True:
            print("\n1. Actualizar producto")
            print("2. Actualizar proveedor")
            print("3. Actualizar distribuidor")
            print("4. Regresar al menu principal")
            try:
                opcion_actualizacion = int(input("\nOpcion: "))
            except ValueError:
                opcion_actualizacion = 0

            if opcion_actualizacion == 1:
                productos = session.query(Producto).all()
                for producto in productos:
                    print(f"{producto.id}. {producto.nombre}")

                por_actualizar = input("Inserte ID del PRODUCTO por actualizar... ")
                nuevo_nombre = input("Inserte el nuevo nombre del PRODUCTO... ")

                producto = session.query(Producto).get(por_actualizar)
                if producto:
                    producto.nombre = nuevo_nombre
                    session.commit()
                else:
                    print("ID de producto no válido.")

            elif opcion_actualizacion == 2:
                proveedores = session.query(Proveedor).all()
                for proveedor in proveedores:
                    print(f"{proveedor.id}. {proveedor.nombre}")

                por_actualizar = input("Inserte ID del PROVEEDOR por actualizar... ")
                nuevo_nombre = input("Inserte el nuevo nombre del PROVEEDOR... ")

                proveedor = session.query(Proveedor).get(por_actualizar)
                if proveedor:
                    proveedor.nombre = nuevo_nombre
                    session.commit()
                else:
                    print("ID de proveedor no válido.")

            elif opcion_actualizacion == 3:
                distribuidores = session.query(Distribuidor).all()
                for distribuidor in distribuidores:
                    print(f"{distribuidor.id}. {distribuidor.nombre}")

                por_actualizar = input("Inserte ID del DISTRIBUIDOR por actualizar... ")
                nuevo_nombre = input("Inserte el nuevo nombre del DISTRIBUIDOR... ")

                distribuidor = session.query(Distribuidor).get(por_actualizar)
                if distribuidor:
                    distribuidor.nombre = nuevo_nombre
                    session.commit()
                else:
                    print("ID de distribuidor no válido.")

            elif opcion_actualizacion == 4:
                print("Regresando al menú principal🤷")
                break

            else:
                print("ERR::Opcion no valida")
    elif opcion == 5:
        break
    
    elif opcion == 999:
        secreto = "admin123"
        password = input("Password: ")
        if secreto == password:
            while True:
                opcion_panico = input("¿Estas seguro (S/N)?")
                if opcion_panico.upper() == "S":
                    print("BOOM!")
                    session.query(Producto).delete()
                    session.query(Proveedor).delete()
                    session.query(Distribuidor).delete()
                    session.commit()
                    break
                else:
                    print("Se fue la DEA")
                    break
        else:
            print("Dale de aqui, payaso!")
    else:
        print("ERR::Opcion no valida")
