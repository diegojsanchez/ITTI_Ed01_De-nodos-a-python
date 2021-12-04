# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def todos_elementos_por_categoria_en_vista(c,v):
	'''Uso: Obtiene todos los elementos de la categoría especificada \nen la vista del modelo indicada. . \nEntradas: categoria = IN[0], vista = IN[1]'''
	elementos = FilteredElementCollector(doc,v.Id).OfCategoryId(c.Id).ToElements()
	return elementos

#ENTRADAS
categoria = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
vista = UnwrapElement(IN[1]) #Para los elementos que vienen de Dynamo
#SALIDA
OUT = todos_elementos_por_categoria_en_vista(categoria,vista)