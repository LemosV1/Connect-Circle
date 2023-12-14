from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import game
import time

pygame.init()
pygame.mixer.init()

def opcao():                          
    menu_more = Window(800,600)
    back = Sprite("./sprites./menu/back.png")
    fundo = GameImage("./sprites./menu/fundoST.png")
    mouse = menu_more.get_mouse()
    
    
    back.x = 8
    back.y = 10

    while(True):
        if mouse.is_over_area([back.x, back.y], [back.x + back.width, back.y + back.height]) and mouse.is_button_pressed(1):
            return


            
        fundo.draw()
        back.draw()
        menu_more.update()

def start_mods():
    mods_jan = Window(800,600)
    mouse_mods = mods_jan.get_mouse()
    mods_jan.set_title("Connect Circle: Modos de jogo")
    fundo = GameImage("./sprites./menu/fundoST.png")

    clock = pygame.time.Clock()
    teclado = mods_jan.get_keyboard()

    somInicia = pygame.mixer.Sound("./audio/inicia.mp3")
    normal = Sprite("./sprites./menu/normal_0.png")
    hard = Sprite("./sprites./menu/hard_0.png")

    normal.x = mods_jan.width/2 - normal.width/2
    normal.y = mods_jan.height/2 - normal.height

    hard.x = mods_jan.width/2 - hard.width/2
    hard.y = mods_jan.height/2 + normal.height/2
    timer = time.time()
    
    while(True):
        if teclado.key_pressed("ESC"):
            return
        
        timePass = time.time() - timer
        print(timePass)

        if mouse_mods.is_over_area([normal.x, normal.y], [normal.x + normal.width, normal.y + normal.height]) and mouse_mods.is_button_pressed(1):
            if timePass >= 0.5:
                somInicia.play()
                game.start_game4()

        if mouse_mods.is_over_area([hard.x, hard.y], [hard.x + hard.width, hard.y + hard.height]) and mouse_mods.is_button_pressed(1):
            if timePass >= 0.5:
                somInicia.play()
                game.start_game5()
        
        fundo.draw()
        normal.draw()
        hard.draw()
        mods_jan.update()

def vitoria(player):
    mods_jan = Window(800,600)
    mouse_mods = mods_jan.get_mouse()
    mods_jan.set_title("Connect Circle: Win")

    normal = Sprite("./sprites./menu/normal_0.png")
    sair = Sprite("./sprites./menu/sair.png.jpg")

    win = pygame.mixer.Sound("./audio/win.mp3")
    win.play()
    click = pygame.mixer.Sound("./audio/click.mp3")

    normal.x = mods_jan.width/2 - normal.width/2
    normal.y = mods_jan.height/2 - normal.height

    sair.x = mods_jan.width/2 - sair.width/2
    sair.y = mods_jan.height/2 + normal.height/2

    while(True):
        if mouse_mods.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse_mods.is_button_pressed(1):
            click.play()
            mods_jan.close()
        
        mods_jan.draw_text("Player {} venceu!".format(player),200, 100 , 45, (255,255,255), "comic sans", False, False)
        
        
        sair.draw()
        mods_jan.update()