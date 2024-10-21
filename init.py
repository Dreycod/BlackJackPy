import pygame
from Services.Classes import * # Import all classes
from Services.Design import * # Import all design
# load the text from data.txt
data = open("data.txt","r")
data = data.read()
data = data.split("\n")


# **************** Fonctions ****************
def KeyEvents():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # Gestion des inputs
            if event.key == pygame.K_ESCAPE:
                return False
        elif event.type == pygame.QUIT:
            return False

def main():
    screen = create_window()
    running = True 
    main_status = "menu"
    # add music

    play_sound(BACKGROUND_MUSIC,"music",0.4,-1)

    menu = newMenu()
    match = newMatch()
    n_players = 1

    match.initalizePlayers(n_players)

    while running:
        Events = KeyEvents()

        if Events == False:
            running = False

        if main_status == "menu":
            refresh_background(screen,menu_background)
            menu.draw(screen)
            menu.interact()
            if menu.mode == "single":
                main_status = "game"
                match.mode = "single"
        else:
            refresh_background(screen,background)

            if match.mode == "single":
                match.singlePlayer(screen)
            elif match.mode == "multi":
                match.multiPlayer(screen)

            match.draw_background_info(screen)
        
        pygame.display.flip()
    # ****************** Save data ******************
    data = open("data.txt","w")
    data.write(str(match.tour)+" parties jouées en "+str(match.mode)+"\n")
    for i in range(len(match.players)):
        if i == range(len(match.players))[-1]:
            continue
        data.write(str(match.players[i].name)+" Data"+"\n")
        data.write("Parties gagnées: "+str(match.players[i].wins)+"\n")
        data.write("Parties perdues: "+str(match.players[i].losses)+"\n")
        data.write("Parties en égalité: "+str(match.players[i].draws)+"\n")
        data.write("Quantité d'argent gagnée: "+str(match.players[i].totalmoneywon)+"\n")
        data.write("Quantité d'argent perdu: "+str(match.players[i].totalmoneylost)+"\n")

    pygame.quit()
# **************** Fin Fonctions ****************
    
# **************** Main ****************
pygame.init()
main()