from modelos.avaliacao import Avaliacao 
from modelos.cardapio.item_cardapio import ItemCardapio 


class Restaurante:
    ''' Representa um restaurante e suas caracteristicas'''
    restaurantes = []

    def __init__(self,nome,categoria):
        ''' inicializa uma instancia de restaurante'''
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False 
        self._avaliacao = []
        self.item_cardapio = []

        Restaurante.restaurantes.append(self)

    def __str__(self):
        ''' retorna uma representacao em string do restaurante'''
        return f'{self._nome} | {self.categoria}'
     
    @classmethod
    def listar_restaurantes(cls):
        ''' Exibe uma lista formatada para todos os restaurantes'''
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)}  |  {restaurante.categoria.ljust(25)}  | {restaurante.media_avaliacoes} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        ''' retorna se o restaurante esta ativo ou nao'''
        return 'Verdadeiro' if self._ativo else 'Falso'

    def alternar_estado(self):
        '''Alterna o estado de ativo ou nao do restaurante'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Registra avaliacao do restaurante'''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        '''calcula e retorna a media das notas de avaliacao do restaurante'''
        if not self._avaliacao:
            return f'Nao avaliado ainda'.title()
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_de_notas = len(self._avaliacao)
            media = round(soma_das_notas / quantidade_de_notas, 1)
        
            return media

        
    def adicionar_no_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self.item_cardapio.append(item)

    
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self.item_cardapio, start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preco: R$ {item._preco} | Descricao: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preco: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            else:
                mensagem_sobremesa = f'{i}. Nome:{item._nome} | Preco: R$ {item._preco} | Tipo: {item._tipo} | Tamanho: {item._tamanho}'
                print(mensagem_sobremesa)


