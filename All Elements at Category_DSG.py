# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector, ElementLevelFilter
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def todos_elementos_por_categoria(c):
	'''Uso: Colecta todos los elementos por categoría.'''
	elementos = FilteredElementCollector(doc).OfCategory(c).ToElements()
	return elementos

#ENTRADAS
categoria = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
#SALIDA
OUT = todos_elementos_por_categoria(categoria)