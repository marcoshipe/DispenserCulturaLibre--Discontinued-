#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
from string import rfind
from manejadorDispositivos import ManejadorDispositivos
from dispositivo import Dispositivo

class Usb(ManejadorDispositivos):
    
    def grabar(self, pathComun, datos,dev):
        pathDestino = dev.getPath()
        pD = pathDestino.replace(' ','\ ')
        pC = pathComun.replace(' ','\ ')
        for dato in datos:
            d = dato.replace(' ','\ ')
            if not os.path.isdir(os.path.dirname(pathDestino + dato)):
                os.makedirs(os.path.dirname(pathDestino + dato))
            os.system('cp ' + pC + d +' --target-directory=' + pD + d[0:rfind(d,'/')])
   
    def hayDispositivos(self):
        os.system('df -h -B 1 | grep .*sd[bc] > usb.db');
        fd = open ('usb.db', 'r')
        devs = fd.readlines()
        fd.close()        
        cant_lineas = len(devs)
        for i in range(cant_lineas):            
            devs[i] = devs[i].split(None,5)     
        
        if cant_lineas>0:            
            devs[0][5] = devs[0][5][:-1]
            return Dispositivo("USB",(int(devs[0][1])),(int(devs[0][2])),(int(devs[0][3])),devs[0][5])            
        return 0
