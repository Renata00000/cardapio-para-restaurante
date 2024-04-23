from modelo.avaliacao import Avaliacao

class Restaurante:
    
    restaurantes =[]
    def __init__(self, nome, _categoria):
        self._nome = nome.title()
        self._categoria = _categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    
    @classmethod
    def lista_restaurantes(cls):
        print(f'{'nome do restaurante.'.ljust(25)} | {'categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
           print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} |{restaurante.ativo}')

            
    @property
    def ativo(self) :
        return '⌧' if self._ativo else '☐'   
    
    def alterar_estado(self):
        self._ativo = not self._ativo    
  
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
             avaliacao = Avaliacao(cliente,nota)
             self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
      if not self._avaliacao:
          return '-'
      somada_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
      quantidade_de_notas = len(self._avaliacao)
      media = round(somada_das_notas/ quantidade_de_notas,1)
      return media