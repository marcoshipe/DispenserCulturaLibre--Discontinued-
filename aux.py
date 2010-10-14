# -*- coding: utf-8 -*-

class Aux:
    """
    aca van todos los metodos comunes usados por varias clases
    """
    
    @staticmethod
    def convertirTamanio(bytes):
        """
        Metodo que convierte un tamaño dado en bytes al que parece mas comodo: bytes, KiB, MiB o GiB
        """
        size=bytes
        if size>1073741824:
            size/=1073741824
            unidad='GiB'
        else:
            if size>1048576:
                size/=1048576
                unidad="MiB"
            else:
                if size>1024:
                    size/=1024
                    unidad="KiB"
                else:
                    unidad="bytes"
        return (size, unidad)
