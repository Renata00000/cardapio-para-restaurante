
from modelo.restaurante import Restaurante
from modelo.cardapio.bebida import Bebida 
from modelo.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'omelhor paozinho da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_noCardapio(bebida_suco)
restaurante_praca.adicionar_noCardapio(prato_paozinho)

# restaurante_praca.receber_avaliacao('Renata',10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 2)
# restaurante_mexicano = Restaurante('Mexicano', 'Mexicano')
# restaurante_japones = Restaurante('Japonês', 'Japonês')

# restaurante_mexicano.alterar_estado()

def main():
    restaurante_praca.exibir_cardapio
    # print(bebida_suco)
    # print(prato_paozinho)
    # Restaurante.lista_restaurantes()

if __name__ == '__main__':
    main()
