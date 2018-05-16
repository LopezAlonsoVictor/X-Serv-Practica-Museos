#!/usr/bin/python

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from xml.sax import SAXParseException
import sys
from urllib import request
from webapp.models import Museo


def normalize_whitespace(text):
    return string.join(string.split(text), ' ')



class myContentHandler(ContentHandler):

    def __init__ (self):
        self.atributo = ""
        self.inContent = False
        self.theContent = ""
        self.nombre = ""
        self.descripcion = ""
        self.accesibilidad = ""
        self.enlace = ""
        self.direccion = ""
        self.direccion_aux = ""
        self.barrio = ""
        self.distrito = ""
        self.telefono = ""
        self.fax = ""
        self.email = ""
        

    def startElement (self, name, attrs):
        if name == "atributo":
            self.atributo = attrs.get("nombre")
        if attrs.get("nombre") in ["NOMBRE","DESCRIPCION-ENTIDAD","ACCESIBILIDAD",
                                    "CONTENT-URL","NOMBRE-VIA","CLASE-VIAL",
                                    "LOCALIDAD","PROVINCICA","BARRIO",
                                    "DISTRITO","TELEFONO","FAX","EMAIL"]:
            self.inContent = True
            
    def endElement (self, name):
        if self.atributo == "NOMBRE":
            self.nombre = self.theContent
        elif self.atributo == "DESCRIPCION-ENTIDAD":
            self.descripcion = self.theContent
        elif self.atributo == "ACCESIBILIDAD":
            self.accesibilidad = self.theContent
        elif self.atributo == "CONTENT-URL":
            self.enlace = self.theContent
        elif self.atributo == "NOMBRE-VIA":
            self.direccion_aux = self.theContent
        elif self.atributo == "CLASE-VIAL":
            self.direccion = self.theContent + " " + self.direccion_aux
        elif self.atributo == "LOCALIDAD":
            self.direccion = self.direccion + "," + self.theContent
        elif self.atributo == "PROVINCICA":
            self.direccion = self.direccion + "," + self.theContent
        elif self.atributo == "BARRIO":
            self.barrio = self.theContent
        elif self.atributo == "DISTRITO":
            self.distrito = self.theContent
        elif self.atributo == "TELEFONO":
            self.telefono = self.theContent
        elif self.atributo == "FAX":
            self.fax = self.theContent
        elif self.atributo == "EMAIL":
            self.email = self.theContent
        self.inContent = False
        self.theContent = ""
        self.atributo = ""
        if name == "contenido":
            museo = Museo(nombre = self.nombre,descripcion = self.descripcion,
                            accesibilidad = self.accesibilidad,enlace = self.enlace,
                            direccion = self.direccion,barrio = self.barrio,
                            distrito = self.distrito,telefono = self.telefono,
                            fax = self.fax,email = self.email)
            museo.save()
            self.atributo = ""
            self.inContent = False
            self.theContent = ""
            self.nombre = ""
            self.descripcion = ""
            self.accesibilidad = ""
            self.enlace = ""
            self.direccion = ""
            self.direccion_aux = ""
            self.barrio = ""
            self.distrito = ""
            self.telefono = ""
            self.fax = ""
            self.email = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

def getrss():
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
    xmlFile = request.urlopen("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full")
    theParser.parse(xmlFile)


