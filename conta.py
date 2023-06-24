class Conta ():
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel_saque = self.__saldo + self.__limite

        if  valor_disponivel_saque <= valor:
            return True
        else:
            return False

    def saca(self, valor):
        if (self.pode_sacar()):
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso!")
        else:
            print("O valor para saque é maior que o limite mais o saldo")

    def transfere(self, conta_destino, valor):
        self.saca(valor)
        conta_destino.deposita(valor)
        print(f"Transferencia de número: {self.__numero} e titular: {self.__titular} \n para conta de número: {conta_destino.get_numero()} e titular {conta_destino.get_titular()} \n no valor de {valor}")
    
    @property
    def get_numero(self):
        return self.__numero
    
    @property
    def get_titular(self):
        return self.__titular
    
    @property
    def get_limite (self):
        return self.__limite
    
    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite 

    @staticmethod
    def codigo_banco():
        return {"BB":"001","Caixa":"104","Bradesco":"237"}