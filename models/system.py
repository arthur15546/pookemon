from random import randint

class system():
    def caucular_dano(self, atacante, golpe, alvo):
        dano = self.descobrir_dano(golpe)
        critico = self.critico()
        efetivo = self.efetivo()
        return dano + critico + efetivo
    
    def efetivo(pkm1, pkm2):
        if "planta" in pkm1.tipos:
            if "agua" in pkm2.tipos:
                return 5

        elif "fogo" in pkm1.tipos:
            if "planta" in pkm2.tipos:
                return 5
        
        elif "agua" in pkm1.tipos:
            if "fogo" in pkm2.tipos:
                return 5
        
        else:
            return 0
    
    def critico():
        sort = randint(0, 100)
        if sort >= 75:
            return 5
        else:
            return 0
    
    def descobrir_dano(golpe):
        return golpe["poder"]
    
    def mais_rapido(pkm1, pkm2):
        if pkm1.velocidade > pkm2.velocidade:
            return pkm1, pkm2
        else:
            return pkm2, pkm1
        