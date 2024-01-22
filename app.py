from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa 
restaurante_praca = Restaurante('praca', 'GOurmet')
bebida_suco = Bebida('Suco de Melancia', 5.00 , 'grande' )
prato_pao = Prato('Pao', 2.00, 'O melhor pao da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
sobremesa_sagu = Sobremesa('Sagu', 12.00 ,'Sagu feito no sul','medio')
restaurante_praca.adicionar_no_cardapio(sobremesa_sagu)
sobremesa_sagu.aplicar_desconto()


def main():
    restaurante_praca.exibir_cardapio
    

if __name__ == '__main__':
    main()
