# Rhythm_Collector_ElementsOfTypeInDocument_ACC
# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr
import System
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

#FUNCIONES
def todos_elementos_del_tipo_en_doc_o_link(clase, doc):
	"""
	Uso: Obtiene todos las instancias del Element Types\n especificado dentro de un documento,\n este puede ser el documento actual o un link.\n
	Nos pide dos argumentos: Element Types (IN[0])\n y Document (IN[1]), este puede ser un RevitLinkInstance,\n si se actua en el documento actual se puede dejar vacío.  
	La categoría puede ser seleccionada desde Dynamo,\n ser una BuiltInCategory o una BuiltInCategory como string.
	"""

	doc = UnwrapElement(IN[1])
	if not doc: 
		doc = DocumentManager.Instance.CurrentDBDocument 
	elif doc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": 
		doc = doc.GetLinkDocument()
	else:
		pass
	return FilteredElementCollector(doc).OfClass(clase).ToElements()


#ENTRADAS
clase = IN[0] # Element Types
doc = UnwrapElement(IN[1]) #RevitLinkInstance. Si se actua contra el documento actual se puede dejar el input vacio. 
#SALIDA
OUT = todos_elementos_del_tipo_en_doc_o_link(clase, doc)