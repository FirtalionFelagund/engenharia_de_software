import requests

class ContaBancaria:
    def __init__(self, saldo, numero, titular):
        self.saldo = saldo
        self.numero = numero
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def __str__(self):
        str = (f'Conta: {self.numero}\n' +
               f'Titular: {self.titular}\n' +
               f'Saldo: {self.saldo}'
               )
        return str


class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        str = f'Nome: {self.nome}\n' + f'CPF: {self.cpf}'
        return str


pessoa = Pessoa("Fulano", "01010101")
conta = ContaBancaria(1000.0, 1, pessoa)

pessoa1 = Pessoa("Ciclano", "03234234")
conta1 = ContaBancaria(2000.0, 2, pessoa1)

conta.depositar(100)

print(conta, conta1)