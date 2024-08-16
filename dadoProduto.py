class dadoProduto:
    def __init__(self, codigo, descricao, NCMeSH, Cst, Cfop, quantidade, valorUnitario, valorDesconto, valorLiquido, baseCalculoICMS, valorICMS, valorIPI, aliquota):
        self.codigo = codigo
        self.descricao = descricao
        self.NCMeSH = NCMeSH
        self.Cst = Cst
        self.Cfop = Cfop
        self.quantidade = quantidade
        self.valorUnitario = valorUnitario
        self.valorDesconto = valorDesconto
        self.valorLiquido = valorLiquido
        self.baseCalculoICMS = baseCalculoICMS
        self.valorICMS = valorICMS
        self.valorIPI = valorIPI
        self.aliquota = aliquota