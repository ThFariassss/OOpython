class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        
        self._saldo += valor

    def sacar(self, valor):
        
        self._saldo += valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0001",100)
conta.depositar(100)
print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo)

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
  
    def get_nome(self):
        return self.get_nome
    
    def get_idade(self):
        return 2024 - self._ano_nascimento
    
pessoa = Pessoa("Thiago", 2002)
print(f"Nome: {pessoa.nome}\t Idade:{pessoa.idade}")
print(f"Nome {pessoa.get_nome}\t Idade: {pessoa.get_idade}")
    
