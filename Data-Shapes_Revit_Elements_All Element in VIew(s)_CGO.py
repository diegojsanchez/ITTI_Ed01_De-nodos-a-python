# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def todos_elementos_en_vista(v):
	"""
    Uso: Obtiene todas los elementos de una vista o conjunto de vistas
    Entrada: vista(s) = IN[0]
    """
	vistas = IN[0]
	if isinstance(vistas,list):
		vistas = UnwrapElement(IN[0])
	else:
		vistas = [UnwrapElement(IN[0])]
  
	elementos = [FilteredElementCollector(doc, v.Id). ToElements() for v in vistas]   
	
	return elementos
    
#ENTRADAS
vistas = IN[0] #No es necesario Unwrap
#SALIDA
OUT = todos_elementos_en_vista(vistas)