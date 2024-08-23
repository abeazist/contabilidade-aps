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
        self.baseCalculo = None
        self.valorInformado = valorInformado
        self.pagamentosRealizados = None


# VALIDACOES IMPOSTO DE RENDA JURIDICA

    def setPagamentosRealizados(self, pagamentosRealizados)
        if self.pagamentosRealizados > 0 and self.pagamentosRealizados == valorInformado

            self.__pagamentosRealizados = pagamentosRealizados

        else:
            raise "Os pagamentos realizados não podem ser negativos e tambem devem ser iguais aos valores informados nas notas fiscais ou recibos"


    def setBaseCalculo(self, baseCalculo)
        if self.baseCalculo >= 0 and self.baseCalculo == baseCalculoEsperada

        else:
            raise "A base de calculos nao pode possuir um valor negativo e tambem devem ter o valor igual a base de calculo esperada"

    def setAliquotas(self, aliquotas)
        