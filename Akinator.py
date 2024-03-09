import json

class JogoAdivinhacaoCarros:
    def __init__(self):
        #self.carros = ['Civic', 'Corolla', 'Gol', 'Fusca', 'Mustang', 'BMW','Toyota' ,'Ford' ,'Mercedes-Benz' ,'Chevrolet']
        
        with open('perguntas.json', 'r', encoding='utf-8') as arquivo:
            self.mapa_solucoes = json.load(arquivo)
            
        # Conjunto de carros
        self.carros = list(self.mapa_solucoes.keys())

    def jogar(self):
        #print(f"\n\n------------------------------- LISTA DE CARROS ------------------------------- \n\n Civic, Corolla, Gol, Fusca, Mustang, BMW, Toyota, Ford, Mercedes-Benz, Chevrolet\n")
        print(f"\n\n------------------------------- LISTA DE CARROS ------------------------------- \n\n{', '.join(self.carros)}\n")
        print("Bem-vindo ao Jogo de Adivinhacao de Carros!")
        print("Pense em um carro da lista e responda com 'sim' ou 'nao'.\n")

        carro_adivinhado = self.adivinhar_carro()

        if carro_adivinhado == 0: 
            print("\nNão consegui adivinhar o carro\n")
        else:
            print(f"\nEu acho que o carro que você pensou é: {carro_adivinhado}\n")

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
                        break # Este break serve para que nao seja realizado mais perguntas do carro, pois como a resposta foi nao, 
                              # nao há necessídade de realizar as perguntas do carro
                    
                if pergunta in perguntas_realizadas_nao:
                    respostas.append("nao")

            # se apargunta estiver no array perguntas_realizadas_nao, atribui em repostas a string nao 
            if all(resposta == 'sim' for resposta in respostas):
                return carro
        return  0

# Criando e jogando o jogo
jogo_carros = JogoAdivinhacaoCarros()
jogo_carros.jogar()