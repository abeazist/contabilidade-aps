# cadastra uma empresa existente no sistema
class Empresa:
    def __init__(self, razaoSocial, cnpj, telefone, tipoEmpresa, dataFundacao):
        self.razaoSocial = razaoSocial
        self.cnpj = cnpj
        self.telefone = telefone
        self.tipoEmpresa = tipoEmpresa
        self.dataFundacao = dataFundacao
        

class Endereco:
    def __init__(self, cep, logradouro, numero, rua, bairro, cidade, estado, complemento):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.complemento = complemento


class funcionario:
    def __init__(self, nome, rg, cpf, telefone, email, senha):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha