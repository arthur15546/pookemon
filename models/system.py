from random import randint

class system():
    def caucular_dano(atacante, golpe, alvo):
        pass
    
    def efetivo(pkm1, pkm2):
        if "planta" in pkm1.tipos:
            if "agua" in pkm2:
                return 5

        elif "fogo" in pkm1.tipos:
            if "planta" in pkm2:
                return 5
        
        elif "agua" in pkm1.tipos:
            if "fogo" in pkm2:
                return 5
        
        else:
            return 0
    
    def critico():
        sort = randint(0, 100)
        if sort >= 75:
            return 5
        else:
            return 0
    
