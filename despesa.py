class despesa:
    def __init__(self,dedutivel, naoDedutivel, dataDespesa, numeroDespesa, valorTotal, tipoDespesa, taxa):
        self.dedutivel = dedutivel
        self.naoDedutivel = naoDedutivel
        self.dataDespesa = dataDespesa
        self.numeroDespesa = numeroDespesa
        self.valorTotal = valorTotal
        self.tipoDespesa = tipoDespesa
        self.taxa = taxa


class itemDespesa:
    def __init__(self, valor, quantidade):
        self.valor = valor
        self.quantidade = quantidade


class tipoItemDespesa:
    def __init__(self, tipoNome):
        self.tipoNome = tipoNome