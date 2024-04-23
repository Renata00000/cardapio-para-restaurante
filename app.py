
from modelo.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Renata',10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)
# restaurante_mexicano = Restaurante('Mexicano', 'Mexicano')
# restaurante_japones = Restaurante('Japonês', 'Japonês')

# restaurante_mexicano.alterar_estado()

def main():
    Restaurante.lista_restaurantes()

if __name__ == '__main__':
    main()
