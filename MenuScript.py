from ListaEnlazadaScript import ListaEnlazada
from PisoScript import Piso
import re
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from PatronScript import Patron
class Menu:

    lista_pisos = ListaEnlazada()

    def menu(self):
        print("\n")
        print("1 Cargar Archivo")
        print("2 Mostrar Patron")
        print("3 Seleccionar Nuevo codigo")
        print("4 Mostrar instrucciones")
        print("5 Mostrar pisos cargados")
        print("6 Salir")
        entrada = input("Ingrese un numero 1-5" + "\n")
        patron = "[1-6]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.cargarArchivo()

                self.menu()
            elif entrada == "2":
               pass
            elif entrada == "3":
                self.cargarArchivo()
                self.menu()
            elif entrada == "4":
                pass
            elif entrada == "5":
                pass
            elif entrada == "6":
                raw_input("Presione una tecla" + "\n")
        else:
            self.menu()

    def subMenu1(self):
        pass

    def cargarArchivo(self):
        root = tk.Tk()
        root.withdraw()
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.xml"), ("todos", "*.*")))
        try:
            with open(nombre_archivo, "r", encoding="utf8") as archivo:
                arbol = ET.parse(nombre_archivo, parser = ET.XMLParser(encoding = 'iso-8859-5'))
                raiz = arbol.getroot()
                pisos = raiz.findall('piso')
                for piso in pisos:
                    patrones = ListaEnlazada()
                    nombre_piso = piso.attrib['nombre']
                    r = piso.find('R').text
                    c = piso.find('C').text
                    f = piso.find('F').text
                    s = piso.find('S').text
                    et_patrones = piso.find('patrones').findall('patron')
                    for patron in et_patrones:
                        codigo = patron.attrib['codigo']
                        patron = patron.text
                        patrones.append(Patron(codigo, patron))
                    self.lista_pisos.append(Piso(nombre_piso, r, c, f, s, patrones))
        except FileNotFoundError:
                print("archivo no encontrado")





