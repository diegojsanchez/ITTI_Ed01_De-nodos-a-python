# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import CategoryType, FilteredElementCollector
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def todos_elementos_por_categoria_de_modelo(cat):
	"""
    Uso: Obtiene todas las instancias de la categoría de modelo especificada (solo categorías de modelo)
    Entrada: categoria = IN[0]
    """
	categorias = doc.Settings.Categories
	model_cat = []
	for c in categorias:
		if c.CategoryType == CategoryType.Model:
			model_cat.append(c)

	cat_name = map(lambda c: c.Name, model_cat)
	if cat.Name in cat_name:
		elementos = FilteredElementCollector(doc).OfCategoryId(cat.Id).WhereElementIsNotElementType().ToElements()
	else:
		raise TypeError("Solo categorías de modelo")
	
	return elementos
    
#ENTRADAS
categoria = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
#SALIDA
OUT = todos_elementos_por_categoria_de_modelo(categoria)