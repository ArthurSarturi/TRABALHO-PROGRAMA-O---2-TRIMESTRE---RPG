### rpg com funcionalidade de cartas, as classes funcionaram como deques de cartas, voce pode começar
### escplhendo entre 3 deques de cartas.

###Cadastro de personagens (nome, classe, nível);
###Cada personagem terá um inventário com lista de itens (arma, poção, etc.);
###Sistema de adicionar/remover itens do inventário;
###Exibição do inventário completo;
###Simular o uso de poções (curam HP, por exemplo) ou
###troca de equipamentos;
###Simular um pequeno combate entre dois personagens;
###Controle de peso/capacidade do inventário.

### cartas basicas

import os ## importe do operational system, para uso de limpar o terminal.
import random

playerDeck = [] ## cria lista vazia do inventario de cartas do personagem
playerCoins = 10 ## cria os Coins do player 
playerHealth = 4

## cartas do jogo ##

## 1- Nome 2- Oque faz 3- preço ##

swordCard = ["Espada", "Vence Escudos e Adagas. Perde para Arco", 10]
shieldCard = ["Escudo", "Vence Adagas e Arcos. Perde para Espada", 10]
bowCard = ["Arco", "Vence Espadas e Adagas. Perde para Escudo", 10]

## lista de deck iniciais para o jogador ##

StarterDecks = [
    
    [swordCard, shieldCard],
    [shieldCard, swordCard],

]

## decks disponiveis pra compra na loja do jogo ##

StoreDecks = [
    bowCard,
    swordCard,
    shieldCard
]

Monster = ["Eis que leto:"]

def space(): ## função poggers de espaçamento ##

    print()
    print()

## Função inicial de criação de personagem e introdução ao jogo ##

def create_Character():
    space()

    print("|               | C A R D    R P G |               |")
    print("|       | BEM VINDO A SUA PROPRIA AVENTURA |       |")

    space() ## chama espaçamento ##

    while True: ## função de atributos base ##
        name = str(input("Insira um nome para seu Jogador: "))
         
        if not name.isdigit():
            print(name)
            break
        else:
            print("Nome inválido, tente novamente")
            continue  



def select_Deck(): ## função de seleção de decks iniciais ##
    print("Selecione um Deck para começar, Escolha através da numeração exibida para cada deck: ")
    print("|   CARTA   |   FUNÇÃO   |   PREÇO   | ")
    for indice, i in enumerate(StarterDecks, start=1): ## looping for que exibe e numera os itens dos decks iniciais :3 ##
        print(f"{indice} - {i}")

    while True: ## looping pra escolha do deck ##
        choice = str(input("Insira seu Deck: "))
        
        if choice.isdigit():
            
            if int(choice) > 0 and int(choice) <= len(StarterDecks):
                return StarterDecks[int(choice) - 1]
                break
            else:
                print("Escolha inválida, tente novamente")
                continue    
        else:                                                                                                                                                                                                                                                                                                                                                   
            print("Escolha inválida, tente novamente")
            continue
        
## gerenciador de deck, nele voce gerencia seu deck. (isso foi redundante pra caceta), podendo acessar
## a loja, discartar cartas e receber o preço delas de volta, e outras coisas como listar o inventario.
        
def manage_Deck():

    global playerCoins ## pega a variavel global dos coins do player (sem o global tudo explode e eu fico triste.)

    while True:

        print("Selecione uma opção para gerenciar seu Deck (Discartar, Loja, Listar, Sair): ")

        choice = str(input("Insira sua escolha: ")).upper()
        if choice == "DISCARTAR" or choice == "LOJA" or choice == "LISTAR" or  choice == "SAIR":
            
            
            if choice == "SAIR":
                os.system('cls')

                print("Voce parou de gerenciar seu Deck")
                break
            
            
            elif choice == "LISTAR":
                print(playerDeck)
            
            
            elif choice == "DISCARTAR":
                
                print("Qual carta do seu deck voce deseja discartar?")
                
                while True:
                    for indice, i in enumerate(playerDeck, start=1):
                        print(f"{indice} - {i}")

                    choice = str(input("Insira o numero da carta: "))

                    if choice.isdigit():
                        print(f"você ganhou: {playerDeck[int(choice) - 1][2]}")
                        playerDeck.pop(int(choice) - 1)
                        break
                        
            elif choice == "LOJA":
                os.system('cls')
                print("Voce acessou a loja de cartas")
                space()        
                print(f"voce tem: {playerCoins} Coins")
            
                print("Aqui estao os itens da loja: ")  
                space()
                print("|   CARTA   |   FUNÇÃO   |   PREÇO   | ")

                while True:
                            
                    for indice, i in enumerate(StoreDecks, start=1):
                        print(f"{indice} - {i}")
                    
                    space()
                    choice = str(input("Escolha sua carta, ou Digite (Sair) para voltar: ")).upper() 
                
                    if choice == "SAIR":
                        os.system('cls')
                        break
                            
                    elif choice.isdigit():
                    
                        if StoreDecks[int(choice) - 1][2] <= playerCoins:
                            print(f"Voce comprou a {StoreDecks[int(choice) - 1]} e gastou {StoreDecks[int(choice) - 1][2]}")
                            playerDeck.append(StoreDecks[int(choice) - 1])
                            playerCoins -= StoreDecks[int(choice) - 1][2]

                            ### printa o deck atual do jogador
                            space()

                            print("Seu deck atual é:")
                            print(playerDeck)

                        else:
                            print("Nao foi possivel comprar a carta.")
                    else:
                        print("Escolha inválida. Tente novamente")

        else:
            print("Escolha inválida. Tente novamente")
            continue


def combat_Scene(enemy, deck, health, recompensa): ## funçao de combate
    global playerHealth
    global playerDeck

    enemyLife = health    
    playerLife = playerHealth
        
    print("|        |  VOCE ENTROU EM COMBATE! |        | ")
    print( )
    print(f"Seu inimigo é {enemy}")


    def show_Scene(life1, life2, act1, act2):
        os.system('cls')
        print(f"|          SUA VIDA          |   |       VIDA DO INIMIGO       |")
        print(f"|             {life1}              |   |             {life2}              |")
        print(f"|         SUA ESCOLHA         |   |     ESCOLHA DO INIMIGO     |")
        print(f"|            {act1}           |   |           {act2}           |")
    
    def enemyChoice(deck):
        return deck[random.choice(range(0, len(deck)))][0]

    def playeChoice():
        while True:
            for indice, i in enumerate(playerDeck, start=1):
                print(f"{indice} - {i}")

            choice = str(input("Insira o numero da carta: "))

            if choice.isdigit():
                if int(choice) > len(playerDeck):
                    print("Escolha inválida. Tente novamente")
                    continue
                else:
                    return playerDeck[int(choice) - 1][0]
        
            else:
                print("ESCREVE DIREITO FILHA DA PUTA")
                continue

    def calculate(action1, action2):    
        nonlocal enemyLife
        nonlocal playerLife

        show_Scene(playerLife, enemyLife, action1, action2)

        if action1 == "Espada" and action2 == "Escudo":
            enemyLife -= 1
            print(f"Voce venceu essa rodada. a vida do seu inimigo é {enemyLife}")

        elif action1 == "Escudo" and action2 == "Espada":
            playerLife -= 1
            print(f"Voce perdeu essa rodada. a sua vida é {playerLife}")
        
        elif action1 == action2:
            print("Nenhum dos dois obteve sucesso.")


    while True:           

        if enemyLife <= 0:
            print("O inimigo morreu!")
            break
        elif playerLife <= 0:
            print("Voce morreu!")
            break

        else:

            playerAction = "none"
            enemyAction = "none"

            playerAction = playeChoice()

            enemyAction = enemyChoice(deck)
    
            print(playerAction, enemyAction)
            calculate(playerAction, enemyAction)

    
create_Character()

playerDeck = select_Deck()

manage_Deck()                                                                 

combat_Scene("Ex Queleto", StarterDecks[1], 3, 100)