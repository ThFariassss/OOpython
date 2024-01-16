#Metodo construtor = __Init__
#Metodo destrutor = __del__
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro = 18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Plim plim...")
    
    def parar(self):
        print("Paranbo a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm...") 

   
    
    #def __str__(self):
    #   return f"Bicicleta:cor ={self.cor},modelo ={self.modelo},ano={self.ano},valor= {self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
b1 = Bicicleta("Vermelha", "Cloi", 2024, 800)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Preta", "Zard", 2000, 200)
print(b2)




