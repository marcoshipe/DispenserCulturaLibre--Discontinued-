#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
from manejadorDispositivos import ManejadorDispositivos

class Dispositivo:
       
    tamanio = 0
    usado = 0    
    libre = 0
    path = ""
    tipo = ""
    
    def __init__(self,tipo,tamanio,usado,libre,path):
        self.tipo = tipo
        self.tamanio = tamanio
        self.libre = libre
        self.usado = usado
        self.path = path

    def getTamanio(self):
        return self.tamanio
    
    def getLibre(self):
        return self.libre

    def getUsado(self):
        return self.usado

    def getPath(self):
        return self.path
        
    def getTipo(self):
        return self.tipo
