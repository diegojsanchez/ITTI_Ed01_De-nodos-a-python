# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import ViewDuplicateOption
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def vistas_duplicado(vista,int,prefix,sufix):
	"""
	Uso:
	Duplica una vista.
 	Entradas: Vista a duplicar, número entero correspondiente
	a la opción de duplicado, siendo:
		0 = Duplicate
		1 = AsDependent
		2 = WithDetailing
	prefijo(string) y sufijo(string)
	Nota: Tanto el prefijo como el sufijo son opcionales.
 	"""
	#Opciones de duplicado
	if int == 0:
		opcion = ViewDuplicateOption.Duplicate
	elif int == 1:
		opcion = ViewDuplicateOption.AsDependent
	else:
		opcion = ViewDuplicateOption.WithDetailing
	
	TransactionManager.Instance.EnsureInTransaction(doc) 
	vistaDuplicada = doc.GetElement(vista.Duplicate(opcion))
	
	if bool(prefix) == False and bool(sufix) == False:
		vistaDuplicada.Name = vistaDuplicada.Name
	elif bool(prefix) == False:
		vistaDuplicada.Name = "" + str(vista.Name) + sufix
	elif bool(sufix) == False:
		vistaDuplicada.Name = prefix + str(vista.Name) + ""
	else:
		vistaDuplicada.Name = prefix + str(vista.Name) + sufix
	TransactionManager.Instance.TransactionTaskDone()
 
	return "La vista se ha duplicado correctamente"

#ENTRADAS
vista = UnwrapElement(IN[0]) #Para los elementos que vienen de Dynamo
int = IN[1] #Número entero de 0 a 2 según la opción de diseño
prefix = IN[2] #Opcional
sufix = IN[3]  #Opcional
#SALIDA
OUT = vistas_duplicado(vista,int,prefix,sufix)