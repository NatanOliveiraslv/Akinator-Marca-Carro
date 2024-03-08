#"Ferrari","Mercedez","BMW","Lamborghini","Fiat","Ford","Chevrolet"
 
class JogoAdivinhacaoCarros:
    def __init__(self):
        # Conjunto de carros
        self.carros = ['Civic', 'Corolla', 'Gol', 'Fusca', 'Mustang', 'BMW','Toyota' ,'Ford' ,'Mercedes-Benz' ,'Chevrolet']

        # Mapa de soluções fictício
        self.mapa_solucoes = {
    'Civic': [
        'É um carro japonês?',
        'Possui tecnologia avançada?',
        'Possui um modelo híbrido?',
        'É um sedã?',
        'Está associado à confiabilidade?',
        'Tem uma versão esportiva?'
    ],
    'Corolla': [
        'É um carro japonês?',
        'É um dos carros mais vendidos do mundo?',
        'É um sedã?',
        'Tem uma reputação de confiabilidade?',
        'Possui uma versão híbrida?',
        'É frequentemente utilizado como carro de frota?'
    ],
    'Gol': [
        'É um carro brasileiro?',
        'É conhecido por ser compacto?',
        'É frequentemente utilizado como carro de entrada?',
        'É fabricado por uma empresa alemã?',
        'Tem uma versão esportiva?',
        'Está associado a um animal?'
    ],
    'Fusca': [
        'É um carro clássico?',
        'Foi originalmente produzido na Alemanha?',
        'Possui um design arredondado?',
        'É frequentemente associado à cultura hippie?',
        'Foi produzido por muitos anos?',
        'Tem motor traseiro?'
    ],
    'Mustang': [
        'É um carro esportivo?',
        'É um ícone da indústria automotiva americana?',
        'É um carro veloz?',
        'Possui tecnologia avançada?',
        'Tem uma versão conversível?',
        'Tem um cavalo no logotipo?'
    ],
    'BMW': [
        'É uma marca de carro alemã?',
        'É conhecida por seu desempenho?',
        'Possui uma linha de veículos elétricos?',
        'Tem uma imagem de luxo?',
        'É frequentemente associada à inovação tecnológica?',
        'Tem uma versão SUV?'
    ],
    'Toyota': [
        'É uma marca de carro japonesa?',
        'É conhecida por sua confiabilidade?',
        'Possui uma grande variedade de veículos?',
        'É uma das maiores montadoras do mundo?',
        'É frequentemente associada à eficiência energética?',
        'Tem uma versão pickup?'
    ],
    'Ford': [
        'É uma montadora americana?',
        'É uma das mais antigas fabricantes de automóveis do mundo?',
        'É conhecida por seus carros esportivos?',
        'Tem uma linha de veículos elétricos?',
        'Foi pioneira na produção em massa de automóveis?',
        'Tem uma versão pickup?'
    ],
    'Mercedes-Benz': [
        'É uma marca de carro de luxo?',
        'É conhecida por sua qualidade e sofisticação?',
        'É um carro veloz?',
        'Possui uma linha de veículos elétricos?',
        'É frequentemente associada à elegância e prestígio?',
        'Tem uma versão SUV?'
    ],
    'Chevrolet': [
        'É uma marca americana?',
        'Tem uma presença global?',
        'É conhecida por oferecer uma ampla gama de veículos?',
        'É uma das marcas mais antigas do mundo?',
        'É frequentemente associada à inovação?',
        'Tem uma versão pickup?'
    ]
}
        #'Mustang', 'BMW','Toyota' ,'Ford' ,'Mercedes-Benz' ,'Chevrolet'
    def jogar(self):
        print(f"----LISTA DE CARROS!!----\n\nCivic, Corolla, Gol, Fusca, Mustang, Toyota, Ford, Mercedes-Benz, chevrolet\n")
        print("Bem-vindo ao Jogo de Adivinhacao de Carros!")
        print("Pense em um carro da lista e responda com 'sim' ou 'nao'.")

        carro_adivinhado = self.adivinhar_carro()

        if carro_adivinhado == 0: 
            print("Não consegui adivinhar o carro")
        else:
            print(f"Eu acho que o carro que você pensou é: {carro_adivinhado}")

    def adivinhar_carro(self):
        perguntas_realizadas = []
        perguntas_realizadas_nao = []

        for carro in self.carros:
            respostas = []
            for pergunta in self.mapa_solucoes[carro]:
                if pergunta not in perguntas_realizadas:
                    resposta = input(pergunta + " ").lower()
                    respostas.append(resposta)
                    perguntas_realizadas.append(pergunta)

                    #Se resposta for igual a nao, irá adicionar no array perguntas_realizadas_nao
                    #isto foi feito, pois repostas "nao" impede que a marca do carro seja encontrada, se fosse resposta sim, nao iria fazer sentido 
                    
                    if resposta != "sim":
                        perguntas_realizadas_nao.append(pergunta)
                if pergunta in perguntas_realizadas_nao:
                    respostas.append("nao")

            # se apargunta estiver no array perguntas_realizadas_nao, atribui em repostas a string nao 
            if all(resposta == 'sim' for resposta in respostas):
                return carro
    
        return  0

# Criando e jogando o jogo
jogo_carros = JogoAdivinhacaoCarros()
jogo_carros.jogar()