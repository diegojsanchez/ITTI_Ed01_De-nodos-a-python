# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr
import System
from System.Collections.Generic import List
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import CategoryType, ElementId, FilteredElementCollector, ElementMulticategoryFilter
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 


#FUNCIONES
def todos_elementos_en_vista_activa():
	"""
 	Uso: Obtiene todos los elementos de categoría de tipo modelo pertenecientes a la vista activa.
 	Entrada: Family Type = IN[0]
  	"""
	categorias = doc.Settings.Categories
	catModelId = [x.Id for x in categorias if x.CategoryType == CategoryType.Model]
	catId = List[ElementId](catModelId)
	filtro = ElementMulticategoryFilter(catId)
	elementos = FilteredElementCollector(doc,doc.ActiveView.Id). WherePasses(filtro).ToElements()
	return elementos

#ENTRADAS

#SALIDA
OUT = todos_elementos_en_vista_activa()