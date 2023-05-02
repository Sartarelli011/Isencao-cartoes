class Cliente:
    def __init__(self, cliente_cpf, numero_cartao, bandeira_cartao, gasto_mensal):
        self.cliente_cpf = cliente_cpf
        self.numero_cartao = numero_cartao
        self.bandeira_cartao = bandeira_cartao
        self.gasto_mensal = gasto_mensal

    def show_all_information(self):
        return f'cliente_cpf:{self.cliente_cpf}, numero_cartao:{self.numero_cartao}, bandeira_cartao:{self.bandeira_cartao},gasto_mensal:{self.gasto_mensal}'

    def get_cpf(self):
        return self.cliente_cpf

    def get_numero_cartao(self):
        return self.numero_cartao

    def get_bandeira_cartao(self):
        return self.bandeira_cartao

    def get_gasto_mensal(self):
        return self.gasto_mensal
