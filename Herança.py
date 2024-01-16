#Herda as características e comportamentos da classe pai(base)
#HERANÇA SIMPLES: Herda apenas um comportamento da classe Base, exemplo:
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o Motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' 
        for chave, valor in self.__dict__.items()])}"
           



class MotoCicleta(Veiculo):
    pass
class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas,carregado):
        #self.cor = cor
        #self.placa = placa
        #self.numero_rodas = numero_rodas
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
    
    

moto = MotoCicleta("vermelho", "ABC1234", 2)
carro = Carro("Branco","xde-5598",4)
caminhao = Caminhao("Cinza", "gtc-5168", 8, True)

print(moto)
print(carro)
print(caminhao)

#HERANÇA MULTIPLA
class Animal:
    def __init__(self, nro_patas,):
        self.nro_patas = nro_patas

    def __str__(self):
           return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.
           __dict__.items()])}"

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    
    #def __str__(self):
    #    return 'ave 42'



class Mamifero(Animal):
    def __init__(self,  cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Gato(Mamifero):
    pass

class Cachorro(Mamifero):
    pass

class Leao(Mamifero):
    pass



class Ornintorrinco(Mamifero, Ave):
    def __init__(self,cor_bico, cor_pelo, nro_patas):
        print(Ornintorrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo, cor_bico = cor_bico, nro_patas=nro_patas)

gato = Gato(nro_patas=4, cor_pelo ="Branco")
print(gato)

ornitorrinco = Ornintorrinco(nro_patas=2,cor_pelo= "Preto", cor_bico ="Laranja")
print(ornitorrinco)