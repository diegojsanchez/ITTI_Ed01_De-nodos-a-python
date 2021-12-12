# -*- coding: utf-8 -*-

#BIBLIOTECAS
import clr 
clr.AddReference('RevitAPI') 
from Autodesk.Revit.DB import FilteredElementCollector, RevitLinkInstance
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument 

#FUNCIONES
def listado_vinculos_documentos_nombres_rutas():
	'''Uso: Obtener el listado completo de vinculos, sus documentos, sus nombres y sus rutas.\nEntrada: Sin argumentos.\nSalida: Lista con sublistas:instancias, documentos, nombres y rutas.'''
	vinculos = FilteredElementCollector(doc).OfClass(RevitLinkInstance).ToElements()
	documentos = [x.GetLinkDocument() for x in vinculos]
	nombres = [x.Name for x in vinculos]	
	rutas = [d.PathName for d in documentos]
	return {"Link Doc": documentos, "Link Nombres": nombres, "Link Instancias": vinculos, "Link Ruta": rutas}

#SALIDA
OUT = listado_vinculos_documentos_nombres_rutas()
