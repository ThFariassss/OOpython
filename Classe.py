#Classe:
class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    def latir(self):
        print("Auau")
    def dormir(self):
        self.acordado = True
        print("Zzzzz...")
#OBJETO
cao_1 = Cachorro("Mel","Preto e branco", False)
cao_2 = Cachorro("Bela","Branca")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)