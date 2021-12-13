# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector, FamilyInstanceFilter
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager


#FUNCIONES
def todos_elementos_de_tipo_de_familia(t,link):
	"""
	Uso: Obtiene todos las instancias del tipo de familia especificado dentro del documento.
	Nos pide dos argumentos: Family Type (IN[0]) y RevitLinkInstance (IN[1]) en caso de actuar contra un modelo vinculado.
	La Family Type debe ser obtenida del selector de Dynamo.
	IMPORTANTE: Siempre hay que establecer dos inputs. En caso de actuar contra el documento actual dejar el IN[1] vacío.
	"""

	link = UnwrapElement(IN[1])
	if not link: 
		doc = DocumentManager.Instance.CurrentDBDocument 
	elif link.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": 
		doc = link.GetLinkDocument()
	elif link.GetType().ToString() == "Autodesk.Revit.DB.Document": 
		doc = DocumentManager.Instance.CurrentDBDocument 
	else: 
		doc = DocumentManager.Instance.CurrentDBDocument 

	filtro = FamilyInstanceFilter(doc, t.Id)
	return FilteredElementCollector(doc).WherePasses(filtro).ToElements()

#ENTRADAS
tipo = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
link = (IN[1]) #RevitLinkInstance. Si se actua contra el documento actual dejar el input vacio. 
#SALIDA
OUT = todos_elementos_de_tipo_de_familia(tipo, link)