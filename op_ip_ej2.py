class Coche:
    puertas=0
    extras=0
    def __init__(self,puertas,extras):
        self.puertas=int(puertas)
        self.extras=int(extras)
        
        
    def agregarPuertas(self):
        total_puertas=self.puertas +sSANMelf.extras
        print(f'las puertas actuales son {total_puertas}')
        
coche1=Coche(2,6)

coche1.agregarPuertas()