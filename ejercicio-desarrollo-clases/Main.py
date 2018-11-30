from paquete_archivos.Archivos import MiArchivo, MiArchivoEscribir#importamos las clases para leer y escribir archivos
from paquete_modelo.Alumno import Alumno#importar la clase alumno

m = MiArchivo()#iniciamos el lector de archivo con nombre m
m2= MiArchivoEscribir()#iniciamos la escritura del archivo con nnombre m2

lista = m.obtener_informacion()#agregamso al informacion del archivo a la lista
lista = [l.split("|") for l in lista]# por cada posicion de la lista realizamos un split con el carater especial
lista=lista[1:]#Eliminamos la primera linea que corresponde al emcabezado

print("%15s\t\t%18s"%("ALUMNO","PROMEDIO"))#Imprimimos el emcabezado

for o in lista:#recorremos cada posicion de la lista
    a=Alumno(o[0], o[1], o[2], o[3])# pro cada posicon y con su informacion creamos un objeto ALUMNO
    print(a)#imprimimos el objeto alumno
    m2.agregar_informacion(a)#Agregamso la informaicon resumida al otro archivo
m.cerrar_archivo()# cerramso el archivo de lectura
m2.cerrar_archivo()# cerramos el archivo de escritura