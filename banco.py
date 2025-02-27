class Pessoa:
    def __init__(self, nome, cpf, id_banco, valor_liberado, emprestimo, transferencias):  # colocar os atributos padrão
        self.nome = nome
        self.cpf = cpf
        self.id_banco = id_banco
        self.valor_liberado = valor_liberado
        self.emprestimo = emprestimo
        self.transferencias = transferencias

    def apresentar(self):
        print(f'Bem - Vinda: {self.nome}',
            f'Seu cpf: {self.cpf}',
            f'Id do banco: {self.id_banco}',
            f'Valor do liberado: {self.valor_liberado}',
            f'Emprestimo: {self.emprestimo}',
            f'Transferencias: {self.transferencias}',)

p1 = Pessoa('Lorena', '31013704851', '2lc', '2200,30', '400,00','220,00')
p1.apresentar()

