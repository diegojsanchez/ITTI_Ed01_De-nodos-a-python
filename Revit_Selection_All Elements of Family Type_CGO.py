# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector, FamilyInstanceFilter
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def todos_elementos_de_tipo_de_familia(t):
	'''Uso: Obtiene todos los elementos del tipo de familia especificado en el modelo. \nEntrada: Family Type = IN[0]'''
	filtro = FamilyInstanceFilter(doc, t.Id)
	elementos = FilteredElementCollector(doc).WherePasses(filtro).ToElements()
	return elementos

#ENTRADAS
tipo = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
#SALIDA
OUT = todos_elementos_de_tipo_de_familia(tipo)