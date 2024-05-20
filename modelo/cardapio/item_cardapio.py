
from abc import ABC, abstractclassmethod

class ItemCArdapio(ABC):
    def __init__(self, nome,preco):
        self._nome = nome
        self._preco = preco
        
    @abstractclassmethod
    def aplicar_desconto(self):
        pass    