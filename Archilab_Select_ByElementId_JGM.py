
#BIBLIOTECAS
import clr #CommonLanguage Runtime
from System.Collections.Generic import * 

clr.AddReference('RevitAPI') #Agrega las clases que se encuentran en el archivo dll de la API de Revit.
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices') #Permitirá manejar los documentos y modificarles a través del DocumentManager y el TransactionManager.
import RevitServices
from RevitServices.Persistence import DocumentManager


#Identificadores: Identificador es el nombre empleado para identificar una variable, una función, una clase, un módulo u otro objeto en Python.
doc = DocumentManager.Instance.CurrentDBDocument #Identificador del documento actual de Revit.


#FUNCIONES

def selec_by_elementId(i):
	'''Selecciona elementos a partir de una lista de id'''
	elements = []
	for id in i:
		element = doc.GetElement(ElementId(int(id)))
		elements.append(element)
	return elements

#ENTRADAS
listaId = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo


#CÓDIGO


#SALIDA
OUT = selec_by_elementId(listaId)

