# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector, ElementLevelFilter
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def todas_instancias_por_nivel(n):
	'''Uso: Colecta todos los elementos por nivel.'''
	filtro = ElementLevelFilter(n.Id)
	elementos = FilteredElementCollector(doc).WherePasses(filtro).WhereElementIsNotElementType().ToElements()
	return elementos

#ENTRADAS
nivel = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
#SALIDA
OUT = todos_elementos_por_nivel(nivel)
