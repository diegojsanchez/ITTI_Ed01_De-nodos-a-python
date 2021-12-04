# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def todos_elementos_de_tipo(x):
	'''Uso: Obtiene todos los elementos del documento activo de un tipo determinado. \nEntrada: Element Type = IN[0]'''
	elementos = FilteredElementCollector(doc).OfClass(x).ToElements()
	return elementos

#ENTRADAS
elementType = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
#SALIDA
OUT = todos_elementos_de_tipo(elementType)