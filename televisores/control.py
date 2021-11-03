class Control:
    def __init__(self) :
        self._tv = None
        
    def turnOn(self):
        self._tv.estado = True
        
    def turnOff(self):
        self._tv.estado = False
        
    def canalUp(self):
        self._tv.canalUp()
        
    def canalDown(self):
        self._tv.canalDown()
        
    def volumenUp(self):
        self._tv.volumenUp()
        
    def volumenDown(self):
        self._tv.volumenDown()
        
    def setCanal(self, canal):
        if (self._tv.estado == True):
            if (canal >= 1 and canal <= 120):
                self._tv.setCanal(canal)
                
    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)
        
    def setTv(self, tv):
        self._tv = tv
        
    def getTv(self):
        return self._tv
        