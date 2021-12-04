# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def todos_elementos_por_categoria(c):
	'''Uso: Obtiene todas las instancias de la categoría especificada en el modelo. \nEntrada: categoria = IN[0]'''
	elementos = FilteredElementCollector(doc).OfCategoryId(c.Id).WhereElementIsNotElementType().ToElements()
	return elementos

#ENTRADAS
categoria = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
#SALIDA
OUT = todos_elementos_por_categoria(categoria)
