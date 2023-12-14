from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import menu
import pygame

pygame.init()
pygame.mixer.init()

fundo_game = GameImage("./sprites./menu/fundo.png")
menu_jan = Window(800,600)
mouse = menu_jan.get_mouse()
menu_jan.set_title("Connect Circle")

play = Sprite("./sprites./menu/play.png")
more = Sprite("./sprites./menu/aumenta_som.png")
   

click = pygame.mixer.Sound("./audio/click.mp3")
fundo = pygame.mixer.Sound("./audio/fundoMenuIni.mp3")
fundo.set_volume(0.35)
fundo.play()




play.x = menu_jan.width/2 - play.width/2    
play.y = menu_jan.height/2 + 100    

more.x = menu_jan.width/2 - more.width/2    
more.y = play.y + more.height + 25    


while(True):
    
    if mouse.is_over_area([play.x, play.y], [play.x + play.width, play.y + play.height]) and mouse.is_button_pressed(1):
        fundo.stop()
        click.play()
        menu.start_mods()
        
      

    if mouse.is_over_area([more.x, more.y], [more.x + more.width, more.y + more.height]) and mouse.is_button_pressed(1):
        fundo.stop()
        click.play()
        menu.opcao()
        
    
    fundo_game.draw()
    play.draw()
    more.draw()
    menu_jan.update()

