from conta import Conta

##Criando conta 1
conta = Conta(123,"Piettro",50, 100)

extrato = conta.extrato()
print(extrato)

conta.deposita(50)
extrato = conta.extrato()
print(extrato)

conta.saca(100)
extrato = conta.extrato()
print(extrato)

##Criando conta 2
conta2 = Conta(222,"Pedro",100, 200)

extrato2 = conta2.extrato()
print(extrato)

conta.deposita(70)
extrato2 = conta2.extrato()
print(extrato)

conta.saca(65.5)
extrato2 = conta2.extrato()
print(extrato)