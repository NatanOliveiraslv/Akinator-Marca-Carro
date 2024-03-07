#"Ferrari","Mercedez","BMW","Lamborghini","Fiat","Ford","Chevrolet"
 
class JogoAdivinhacaoCarros:
    def __init__(self):
        # Conjunto de carros
        self.carros = ['Civic', 'Corolla', 'Gol', 'Fusca', 'Mustang']

        # Mapa de soluções fictício
        self.mapa_solucoes = {
            'Civic': ['É um carro japonês?', 'É conhecido por sua economia de combustível?', 'Possui um modelo híbrido?', 'É um sedã?', 'Está associado à confiabilidade?', 'Tem uma versão esportiva?'],
            'Corolla': ['É um carro japonês?', 'É um dos carros mais vendidos do mundo?', 'É um sedã?', 'Tem uma reputação de confiabilidade?', 'Possui uma versão híbrida?', 'É frequentemente utilizado como carro de frota?'],
            'Gol': ['É um carro brasileiro?', 'É conhecido por ser compacto?', 'É frequentemente utilizado como carro de entrada?', 'É fabricado por uma empresa alemã?', 'Tem uma versão esportiva?', 'Está associado a um animal?'],
            'Fusca': ['É um carro clássico?', 'Foi originalmente produzido na Alemanha?', 'Possui um design arredondado?', 'É frequentemente associado à cultura hippie?', 'Foi produzido por muitos anos?', 'Tem motor traseiro?'],
            'Mustang': ['É um carro esportivo?', 'É um ícone da indústria automotiva americana?', 'Possui um design muscular?', 'É frequentemente associado a filmes de ação?', 'Tem uma versão conversível?', 'Tem um cavalo no logotipo?']
        }

    def jogar(self):
        print("Bem-vindo ao Jogo de Adivinhação de Carros!")
        print("Pense em um carro da lista e responda com 'sim' ou 'não'.")

        carro_adivinhado = self.adivinhar_carro()

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
    
            if all(resposta == 'sim' for resposta in respostas):
                return carro

        return "Não consegui adivinhar o carro."

# Criando e jogando o jogo
jogo_carros = JogoAdivinhacaoCarros()
jogo_carros.jogar()