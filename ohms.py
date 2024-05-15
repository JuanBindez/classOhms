class OhmsCalc:
    """calculadores de ohms

    args:
        U (int): é a Voltagem
        I (int): é a Corrente em Amperes
        R (int): é a resistencia eletrica
    """


    def __init__(self, 
                 U: int = None, 
                 I: int = None, 
                 R: int = None, 
                 IP: str = None
                 ):
        
        self.U = U
        self.I = I
        self.R = R
        self.IP = IP

    def voltagem(self) -> int:
        self.U = self.I*self.R
        return self.U
    
    def corrente(self) -> int:
        self.I = self.U/self.R
        return self.I
    
    def resistencia(self) -> int:
        self.R = self.U/self.I
        return self.R
