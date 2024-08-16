class DeclaracaoImpostoFisica:
    def __init__(self, anoCalendarioFisico, rendimentos, despesasDedutiveis, impostoRetiradoFonte, impostoDevido, investimentos):
        self.anoCalendarioFisico = anoCalendarioFisico
        self.rendimentos = rendimentos
        self.despesasDedutiveis = despesasDedutiveis
        self.impostoRetiradoFonte = impostoRetiradoFonte
        self.impostoDevido = impostoDevido
        self.investimentos = investimentos


class DeclaracaoImpostoJuridica:
    def __init__(self, pagamentosRealizados, baseCalculo, aliquotas, impostoDevido, regimeTributario, codigoEmpresa, anoCalendarioJuridico, despesas, lucros, prejuizos, receitas):
        self.pagamentosRealizados= pagamentosRealizados
        self.baseCalculo = baseCalculo
        self.aliquotas = aliquotas
        self.impostoDevido = impostoDevido
        self.regimeTributario = regimeTributario
        self.codigoEmpresa = codigoEmpresa
        self.anoCalendarioJuridico = anoCalendarioJuridico
        self.despesas = despesas
        self.lucros = lucros 
        self.prejuizos =prejuizos
        self.receitas = receitas
        