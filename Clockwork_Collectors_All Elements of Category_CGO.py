# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr
import System
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import BuiltInCategory, FilteredElementCollector
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

#FUNCIONES
def todos_elementos_de_categoria_2(x, link):
	"""
	Uso: Obtiene todos las instancias de la categoría especificada dentro del documento.
	Nos pide dos argumentos: categoría (IN[0]) y RevitLinkInstance (IN[1]) en caso de actuar contra un modelo vinculado.
	La categoría puede ser seleccionada desde Dynamo, ser una BuiltInCategory o una BuiltInCategory como string.
	IMPORTANTE: Siempre hay que establecer dos inputs. En caso de actuar contra el documento actual dejar el IN[1] vacío.
	"""

	bics = System.Enum.GetValues(BuiltInCategory)
	bicn = map(lambda a: str(a), bics)
	salida = None

	if x.GetType().ToString() == "System.String":
		for n,c in zip(bicn,bics):
			if x == n:
				salida = c
	elif x.GetType().ToString() == "Revit.Elements.Category":
		salida = System.Enum.ToObject(BuiltInCategory, x.Id)
	elif x.GetType().ToString() == "Autodesk.Revit.DB.BuiltInCategory":
		salida = x
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

	return FilteredElementCollector(doc).OfCategory(salida).WhereElementIsNotElementType().ToElements()



#ENTRADAS
categoria = IN[0] #String(BuiltInCategory), BuiltInCategory o categoría del selector de categorias de Dynamo.
link = UnwrapElement(IN[1]) #RevitLinkInstance. Si se actua contra el documento actual dejar el input vacio. 
#SALIDA
OUT = todos_elementos_de_categoria_2(categoria, link)
