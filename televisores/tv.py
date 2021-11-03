from televisores.control import Control

class TV:
    _numTV = 0
    
    def __init__(self, marca, estado):
        self._marca = marca
        self.estado = estado
        self._control = Control()
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        TV._numTV += 1
        
    def setMarca(self, marca):
        self._marca = marca
        
    def getMarca(self):
        return self._marca
    
    def setControl(self, control):
        self._control = control
        
    def getControl(self):
        return self._control
    
    def setVolumen(self, volumen):
        if (self.estado == True):
            if (volumen >= 1 and volumen <= 7):
                self._volumen = volumen
                
    def getVolumen(self):
        return self._volumen
    
    def setPrecio(self, precio):
        self._precio = precio
        
    def getPrecio(self):
        return self._precio
    
    def setCanal(self, canal):
        if (self.estado == True):
            if (canal >= 1 and canal <= 120):
                self._canal = canal
                
    def getCanal(self):
        return self._canal
    
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV
        
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    def turnOn(self):
        self.estado = True
        
    def turnOff(self):
        self.estado = False
        
    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if (self.estado == True):
            if (self._canal < 120):
                self._canal += 1

    def canalDown(self):
        if (self.estado == True):
            if (self._canal > 1):
                self._canal -= 1
                
    def volumenlUp(self):
        if (self.estado == True):
            if (self._volumen < 7):
                self._volumen += 1

    def volumenDown(self):
        if (self.estado == True):
            if (self._volumen > 1):
                self._volumen -= 1
    
        
        