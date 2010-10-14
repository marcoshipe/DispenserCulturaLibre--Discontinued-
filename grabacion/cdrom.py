#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
from string import rfind
from manejadorDispositivos import ManejadorDispositivos
from dispositivo import Dispositivo

class CdRom(ManejadorDispositivos):
    
    def grabar(self, pathComun, datos,dev):
        tempDir = os.getcwd() + '/temp'
        print tempDir
        for dato in datos:
            if not os.path.isdir(os.path.dirname(tempDir + dato)):
                os.makedirs(os.path.dirname(tempDir + dato))
            os.symlink(pathComun + dato,tempDir + dato)
        os.system('mkisofs -f -r -l -o temp.iso ' + tempDir)
        os.system('./pywodim.py --iso temp.iso')
        os.system('rm -Rf temp.iso temp')

    def hayDispositivos(self):
        os.system('udisks --show-info /dev/sr0 | egrep "block size|  media" > cdrom0.db');
        fd = open ('cdrom0.db', 'r')
        devs = fd.readlines()
        fd.close()
	#Si no hay lectora de cd/dvd (creo) o no hay ningun dispositivo de cd/dvd, retorno 0	
	if len(devs)==0 or len(devs[1].split())<=1:
            return 0
        else:
            szbloque = devs[0].split()[2]
            tipo =  devs[1].split()[1].upper()
            if tipo.find('CD') >= 0:
                os.system('cdrdao disk-info | grep Capacity > cdrom1.db')
                fd = open ('cdrom1.db', 'r')
                devs = fd.readlines()
                fd.close()        
                bloques = devs[len(devs)-1].split()[4].lstrip('(')
                bloques = int (bloques)
                szbloque = int (szbloque)
                tamanio = bloques * szbloque
                return Dispositivo(tipo,tamanio,0,tamanio,"sr0")
            else:
                os.system('dvd+rw-mediainfo /dev/sr0  | grep "Free Blocks" > cdrom2.db')
                fd = open ('cdrom2.db', 'r')
                devs = fd.readlines()
                fd.close()
                bloques = devs[len(devs)-1].split()[2][:-4]
                bloques = int (bloques)
                szbloque = int (szbloque)
                tamanio = bloques * szbloque
                return Dispositivo(tipo,tamanio,0,tamanio,"sr0")




