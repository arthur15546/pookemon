
class Pokemon():
    def __init__(self, id, nome, hp,  tipo1, tipo2, velocidade, golpes):
        self._id = id
        self._nome = nome
        self._hp = hp
        self._max_hp = hp
        self._tipo1 = tipo1
        self._tipo2 = tipo2
        self._velocidade = velocidade
        self.golpes = golpes
        
    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def hp(self):
        return self._hp
    
    @property
    def max_hp(self):
        return self._max_hp
    
    @property
    def tipos(self):
        return [self._tipo1, self._tipo2]
    
    @property
    def velocidade(self):
        return self._velocidade
    
    @id.setter
    def id(self, valor):
        if valor <= 0:
            self._id = 1
        else:
            self._id = valor
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    @hp.setter
    def hp(self, valor):
        self._hp = valor
    
    @velocidade.setter
    def velocidade(self, valor):
        if valor < 0:
            self._velocidade = 0
        else:
            self._velocidade = valor

    def esta_vivo(self):
        if self.hp >= 0:
            return True
        else:
            return False
    
    def atacar(self, golpe, alvo, battle_system):
        dano = battle_system.caucular_dano(self, golpe, alvo)
        alvo.receber_dano(dano)
    
    def receber_dano(self, dano):
        self.hp -= dano

    def __str__(self):
        return f"{self._nome} | HP: {self._hp} | Tipos: {self._tipo1}, {self._tipo2}"
    
    def curar(self, cura):
        self.hp += cura
        if self.hp > self.max_hp:
            self.hp = self.max_hp