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

    def saca(self, valor):
        self.__saldo -= valor 

    def transfere(self, conta_destino, valor):
        self.saca(valor)
        conta_destino.deposita(valor)
        print(f"Transferencia de número: {self.__numero} e titular: {self.__titular} \n para conta de número: {conta_destino.get_numero()} e titular {conta_destino.get_titular()} \n no valor de {valor}")
    
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def get_limite (self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite 
