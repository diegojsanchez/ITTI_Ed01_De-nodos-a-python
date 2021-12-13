# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import ElementMulticategoryFilter, FilteredElementCollector, ElementId
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 
import System
from System.Collections.Generic import List


#FUNCIONES
def todos_elementos_de_categoria_en_vista(v,cats):
	"""
    Uso: Obtiene todas los elementos de las categorías seleccionadas en la vista seleccionada
    Entradas: vista = IN[0], categoria(s) = IN[1]

    """
	cats = IN[1]
	if isinstance(cats,list):
		cats = UnwrapElement(IN[1])
	else:
		cats = [UnwrapElement(IN[1])]
	
	catId = [x.Id for x in cats]

	catsIds = List[ElementId](catId)
	filtro = ElementMulticategoryFilter(catsIds)
 
	elementos = FilteredElementCollector(doc,v.Id).WherePasses(filtro).ToElements()
	
	return elementos

 #ENTRADAS
vista = UnwrapElement(IN[0]) #Para vistas procedentes de Dynamo
categorias = IN[1]
#SALIDA
OUT = todos_elementos_de_categoria_en_vista(vista,categorias)