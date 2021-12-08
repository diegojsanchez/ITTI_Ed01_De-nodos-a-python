# Rhythm_Collector_Elements Of Category In Document_ACC
# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr
import System
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import BuiltInCategory, FilteredElementCollector
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

#FUNCIONES
def todos_elementos_de_categoria_en_documento(cat, link):
	"""
	Uso: Obtiene todos las instancias de la categoría especificada dentro del documento.
	Nos pide dos argumentos: categoría (IN[0]) y documento (IN[1]), este puede ser el documento actual o un modelo vinculado, en ese caso vincular directamente el linkInstance.
	La categoría puede ser seleccionada desde Dynamo, ser una BuiltInCategory o una BuiltInCategory como string.
	IMPORTANTE: Siempre hay que establecer dos inputs. En caso de actuar contra el documento actual dejar el IN[1] vacío.
	"""

	bics = System.Enum.GetValues(BuiltInCategory)
	bicn = map(lambda a: str(a), bics)
	salida = None

	if cat.GetType().ToString() == "System.String":
		for n,c in zip(bicn,bics):
			if cat == n:
				salida = c
	elif cat.GetType().ToString() == "Revit.Elements.Category":
		salida = System.Enum.ToObject(BuiltInCategory, cat.Id)
	elif cat.GetType().ToString() == "Autodesk.Revit.DB.BuiltInCategory":
		salida = cat
	else: 
		pass

	link = UnwrapElement(IN[1])
	if not link: 
		doc = DocumentManager.Instance.CurrentDBDocument 
	elif link.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": 
		doc = link.GetLinkDocument()
	elif link.GetType().ToString() == "Autodesk.Revit.DB.Document": 
		doc = DocumentManager.Instance.CurrentDBDocument 
	else: 
		doc = DocumentManager.Instance.CurrentDBDocument 

	return FilteredElementCollector(doc).OfCategory(salida).ToElements()



#ENTRADAS
cat = IN[0] #String(BuiltInCategory), BuiltInCategory o categoría del selector de categorias de Dynamo.
link = UnwrapElement(IN[1]) #RevitLinkInstance. Si se actua contra el documento actual dejar el input vacio. 
#SALIDA
OUT = todos_elementos_de_categoria_en_documento(cat, link)
