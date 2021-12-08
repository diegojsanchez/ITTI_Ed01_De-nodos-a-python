# Rhythm_Selection_All Elements of Model Category_ACC
# -*- coding: utf-8 -*-


#BIBLIOTECAS
import clr
import System
clr.AddReference('RevitNodes') 
import Revit
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import *
#BuiltInCategory, FilteredElementCollector, CategoryType
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

#FUNCIONES
def todos_elementos_de_model_category(x):
	"""
	Uso: Obtiene todos las instancias de la categoría\n de tipo 'Model' especificada dentro del documento.\n Categoría (IN[0])
	La categoría puede ser seleccionada desde Dynamo,\n ser una BuiltInCategory o una BuiltInCategory como string.\n
	Si la categoría no es de tipo 'Model'\n arroja el mensaje:\n 'La categoría seleccionada no es de tipo 'Model' '.
	"""

	bics = System.Enum.GetValues(BuiltInCategory)
	bicn = map(lambda a: str(a), bics)
	catBic = None
	
	# 
	catString = x.GetType().ToString()
	if catString == "System.String":
		for n,c in zip(bicn,bics):
			if x == n:
				catBic = c
	elif catString == "Revit.Elements.Category":
		catBic = System.Enum.ToObject(BuiltInCategory, x.Id)
	elif catString == "Autodesk.Revit.DB.BuiltInCategory":
		catBic = x
	else: 
		pass
	
	# Categorias y Tipo de Categorias
	categories = doc.Settings.Categories
	catType = [x.CategoryType for x in categories]
	catName = [x.Name for x in categories] # String
	diccCategories = {}
	for cn, ct in zip(catName, catType):
		diccCategories[cn] = ct	
	
	# Categorias y BuiltInCategory
	diccBuilt = {}
	for i in bics:
		try:
			catId = Revit.Elements.Category.ById(ElementId(i).IntegerValue)
			diccBuilt[str(i)] = str(catId)
		except:
			pass
	
	# Entrado por catBic en diccBuilt, entramos despues diccCategories
	resultado = []
	try:
		valorCat = diccBuilt[str(catBic)]
		valorType = diccCategories[valorCat]
		if str(valorType) == "Model":
			resultado = FilteredElementCollector(doc).OfCategory(catBic).WhereElementIsNotElementType().ToElements()
		else:
			pass
	except:
		resultado.append("La categoría seleccionada no es de tipo 'Model'.")
	return resultado
	


#ENTRADAS
cat = IN[0] #String(BuiltInCategory), BuiltInCategory o categoría del selector de categorias de Dynamo.
#SALIDA
OUT = todos_elementos_de_model_category(cat)