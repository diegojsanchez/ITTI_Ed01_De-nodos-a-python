# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector, Family
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def seleccion_por_nombre_familia(nombre):
	'''Uso: Selecciona la familia por nombre.\nEntrada: Un String.\nSalida: Familia.'''
	familias = FilteredElementCollector(doc).OfClass(Family).ToElements()
	for f in familias:
		if nombre == f.Name:
			return f

#ENTRADAS
nombre = "Sofa - Ottoman"
#SALIDA
OUT = seleccion_por_nombre_familia(nombre)