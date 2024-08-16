class notaFiscal:
    def __init__(self, numero, notaFiscalServico, notaFiscalProduto):
        self.numero = numero
        self.notaFiscalServico = notaFiscalServico
        self.notaFiscalProduto = notaFiscalProduto

class notaFiscalProduto:
    def __init__(self, numero, data, serie, folha, chaveAcesso, inscricaoEstadual, naturezaOperacao, protocoloAutorizacaoUso, dadosAdicionais):
        self.numero = numero
        self.data = data
        self.serie = serie
        self.folha = folha
        self.chaveAcesso = chaveAcesso
        self.inscricaoEstadual = inscricaoEstadual
        self.naturezaOperacao = naturezaOperacao
        self.protocoloAutorizacaoUso = protocoloAutorizacaoUso
        self.dadosAdicionais = dadosAdicionais
        #Cálculos ISSQN
# arquivo pra produto

class notaFiscalServico:
    def __init__(self, numero, data, serie, folha, chaveAcesso, inscricaoEstadual, naturezaOperacao, protocoloAutorizacaoUso, dadosAdicionais):
        self.numero = numero
        self.data = data
        self.serie = serie
        self.folha = folha
        self.chaveAcesso = chaveAcesso
        self.inscricaoEstadual = inscricaoEstadual
        self.naturezaOperacao = naturezaOperacao
        self.protocoloAutorizacaoUso = protocoloAutorizacaoUso
        self.dadosAdicionais = dadosAdicionais
        #Cálculos ISSQN

class emitente:
    def __init__(self, numero, data, valorTotal, inscricaoEstadual, inscricaoMunicipal):
        self.numero = numero
        self.data = data
        self.valorTotal = valorTotal
        self.inscricaoEstadual = inscricaoEstadual
        self.inscricaoMunicipal = inscricaoMunicipal


class calculoISSQN:
    def __init__(self, valorTotalServicos, baseCalculoISSQN, valorTotalISSQN):
        self.valorTotalServicos = valorTotalServicos
        self.baseCalculoISSQN = baseCalculoISSQN
        self.valorTotalISSQN = valorTotalISSQN

class cliente:
    def __init__(self):


