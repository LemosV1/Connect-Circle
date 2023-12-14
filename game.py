from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import menu

pygame.init()
pygame.mixer.init()

def start_game4():
    # Variaveis
    gamewindow = Window(1300, 800)
    raio = 26
    pos_x = []
    pos_y = []
    Linha = 7
    Coluna = 6
    player1_num = 1
    player2_num = 2
    current_player = player1_num  # Player 1 starts
    teclado = gamewindow.get_keyboard()
    fundoJogo = pygame.mixer.Sound("./audio/fundo.mp3")
    fichaCai = pygame.mixer.Sound("./audio/fichaCai.mp3")
    setaMov = pygame.mixer.Sound("./audio/setaMov.mp3")
    fundoJogo.set_volume(0.3)
    fundoJogo.play()

    # Criando a matriz de círculos
    matFichaP1 = [[Sprite("./sprites/bolaP.png") for _ in range(Coluna)] for _ in range(Linha)]
    matFichaP2 = [[Sprite("./sprites/bolaR.png") for _ in range(Coluna)] for _ in range(Linha)]



    # Mapear a posição dos círculos
    for i in range(0, Linha):
        pos_x.append(100 + i*(3*raio))
    for i in range(0, Coluna):
        pos_y.append(100 + i*(3*raio))
    for i in range(Coluna):
        for j in range(Linha):
            matFichaP1[j][i].set_position(pos_x[j], pos_y[i])
            matFichaP2[j][i].set_position(pos_x[j], pos_y[i])

    # Inicializando a matriz de espaços disponíveis
    espacos_disponiveis = [[0 for _ in range(Coluna)] for _ in range(Linha)]


    # Seta que indica a posição do jogador
    seta_ind = 0
    seta = Sprite("./sprites/seta.png")
    seta.set_position(pos_x[0], pos_y[0] - raio/2 - seta.height)

    #Controle do teclado
    keyP1 = {"RIGHT": False, "LEFT": False, "SPACE": False}

    gamewindow.set_title("Connect 4")
    while True:
        # Movimentação da seta
        if teclado.key_pressed("RIGHT") and not keyP1["RIGHT"] and seta.x < pos_x[-1]:
            setaMov.play()
            seta.set_position(seta.x + 3 * raio, pos_y[0] - raio/2 - seta.height)
            seta_ind += 1
            print(seta_ind)
        keyP1["RIGHT"] = teclado.key_pressed("RIGHT")

        if teclado.key_pressed("LEFT") and not keyP1["LEFT"] and seta.x > pos_x[0]:
            setaMov.play()
            seta.set_position(seta.x - 3 * raio, pos_y[0] - raio/2 - seta.height)
            seta_ind -= 1
            print(seta_ind)
        keyP1["LEFT"] = teclado.key_pressed("LEFT")
        
        
        # Mapeando espaços disponíveis
        if teclado.key_pressed("SPACE") and not keyP1["SPACE"]:
            fichaCai.play()
            for i in range(Coluna-1, -1, -1):
                if espacos_disponiveis[seta_ind][i] == 0:
                    espacos_disponiveis[seta_ind][i] = current_player
                    break
            # Switch to the other player for the next turn
            current_player = player1_num if current_player == player2_num else player2_num
        keyP1["SPACE"] = teclado.key_pressed("SPACE")
        
        # Checando se o jogo acabou
        if check_win4(espacos_disponiveis, player1_num):
            fundoJogo.stop()
            menu.vitoria(1)
        if check_win4(espacos_disponiveis, player2_num):
            fundoJogo.stop()
            menu.vitoria(2)
        gamewindow.set_background_color([255, 255, 255])
        seta.draw()
        
        # Desenhando os círculos nos espaços disponíveis
        for i in range(Coluna):
            for j in range(Linha):
                if espacos_disponiveis[j][i] == player1_num:
                    matFichaP1[j][i].draw()  
                elif espacos_disponiveis[j][i] == player2_num:
                    matFichaP2[j][i].draw()  
        
        gamewindow.update()
        gamewindow.update() 
        
def start_game5():
    # Variaveis
    gamewindow = Window(1300, 800)
    raio = 26
    pos_x = []
    pos_y = []
    Linha = 7
    Coluna = 6
    player1_num = 1
    player2_num = 2
    current_player = player1_num  # Player 1 starts
    teclado = gamewindow.get_keyboard()
    fundoJogo = pygame.mixer.Sound("./audio/fundo.mp3")
    fichaCai = pygame.mixer.Sound("./audio/fichaCai.mp3")
    setaMov = pygame.mixer.Sound("./audio/setaMov.mp3")
    fundoJogo.set_volume(0.3)
    fundoJogo.play()

    # Criando a matriz de círculos
    matFichaP1 = [[Sprite("./sprites/bolaP.png") for _ in range(Coluna)] for _ in range(Linha)]
    matFichaP2 = [[Sprite("./sprites/bolaR.png") for _ in range(Coluna)] for _ in range(Linha)]



    # Mapear a posição dos círculos
    for i in range(0, Linha):
        pos_x.append(100 + i*(3*raio))
    for i in range(0, Coluna):
        pos_y.append(100 + i*(3*raio))
    for i in range(Coluna):
        for j in range(Linha):
            matFichaP1[j][i].set_position(pos_x[j], pos_y[i])
            matFichaP2[j][i].set_position(pos_x[j], pos_y[i])

    # Inicializando a matriz de espaços disponíveis
    espacos_disponiveis = [[0 for _ in range(Coluna)] for _ in range(Linha)]


    # Seta que indica a posição do jogador
    seta_ind = 0
    seta = Sprite("./sprites/seta.png")
    seta.set_position(pos_x[0], pos_y[0] - raio/2 - seta.height)

    #Controle do teclado
    keyP1 = {"RIGHT": False, "LEFT": False, "SPACE": False}

    gamewindow.set_title("Connect 4")
    while True:
        # Movimentação da seta
        if teclado.key_pressed("RIGHT") and not keyP1["RIGHT"] and seta.x < pos_x[-1]:
            setaMov.play()
            seta.set_position(seta.x + 3 * raio, pos_y[0] - raio/2 - seta.height)
            seta_ind += 1
            print(seta_ind)
        keyP1["RIGHT"] = teclado.key_pressed("RIGHT")

        if teclado.key_pressed("LEFT") and not keyP1["LEFT"] and seta.x > pos_x[0]:
            setaMov.play()
            seta.set_position(seta.x - 3 * raio, pos_y[0] - raio/2 - seta.height)
            seta_ind -= 1
            print(seta_ind)
        keyP1["LEFT"] = teclado.key_pressed("LEFT")
        
        
        # Mapeando espaços disponíveis
        if teclado.key_pressed("SPACE") and not keyP1["SPACE"]:
            fichaCai.play()
            for i in range(Coluna-1, -1, -1):
                if espacos_disponiveis[seta_ind][i] == 0:
                    espacos_disponiveis[seta_ind][i] = current_player
                    break
            # Switch to the other player for the next turn
            current_player = player1_num if current_player == player2_num else player2_num
        keyP1["SPACE"] = teclado.key_pressed("SPACE")
        
        # Checando se o jogo acabou
        if check_win5(espacos_disponiveis, player1_num):
            fundoJogo.stop()
            menu.vitoria(1)
        if check_win5(espacos_disponiveis, player2_num):
            fundoJogo.stop()
            menu.vitoria(2)
        gamewindow.set_background_color([255, 255, 255])
        seta.draw()
        
        # Desenhando os círculos nos espaços disponíveis
        for i in range(Coluna):
            for j in range(Linha):
                if espacos_disponiveis[j][i] == player1_num:
                    matFichaP1[j][i].draw()  
                elif espacos_disponiveis[j][i] == player2_num:
                    matFichaP2[j][i].draw()  
        
        gamewindow.update()
        gamewindow.update() 

def check_win4(matrix, player_num):
    #Teste das linhas
    for row in matrix:
        for i in range(len(row) - 3):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == player_num:
                return True

    #Teste das colunas
    for j in range(len(matrix[0])):
        for i in range(len(matrix) - 3):
            if matrix[i][j] == matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 3][j] == player_num:
                return True

    #Teste das diagonais \
    for i in range(len(matrix) - 3):
        for j in range(len(matrix[i]) - 3):
            if matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][j + 3] == player_num:
                return True

    #Teste das diagonais /
    for i in range(len(matrix) - 3):
        for j in range(3, len(matrix[i])):
            if matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][j - 3] == player_num:
                return True

def check_win5(matrix, player_num):
    #Teste das linhas
    for row in matrix:
        for i in range(len(row) - 4):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == row[i + 4] == player_num:
                return True

    # Teste das colunas
    for j in range(len(matrix[0])):
        for i in range(len(matrix) - 4):
            if matrix[i][j] == matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 3][j] == matrix[i + 4][j] == player_num:
                return True

    # Teste das diagonais \
    for i in range(len(matrix) - 4):
        for j in range(len(matrix[i]) - 4):
            if matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][j + 3] == matrix[i + 4][j + 4] == player_num:
                return True

    # Teste das diagonais /
    for i in range(len(matrix) - 4):
        for j in range(4, len(matrix[i])):
            if matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][j - 3] == matrix[i + 4][j - 4] == player_num:
                return True