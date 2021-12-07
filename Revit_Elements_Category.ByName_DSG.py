# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr
clr.AddReference("RevitNodes") 
from Revit import Elements

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def seleccion_por_nombre_categoria(nombre):
	'''Uso: Selecciona la categoria por nombre.\nEntrada: Un String.\nSalida: Categoria.'''
	categorias = doc.Settings.Categories
	for c in categorias:
		if nombre == c.Name:
			return Elements.Category.ById(c.Id.IntegerValue)

#ENTRADAS
nombre = "Muros"
#SALIDA
OUT = seleccion_por_nombre_categoria(nombre)