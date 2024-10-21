import pygame
# ******************* Constants *******************
SCREEN_WIDTH=1080
SCREEN_HEIGHT=800
SCREEN_SIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)
SCREEN_CENTER=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
SCREEN_TOPLEFT = (0,0)
SCREEN_BOTTOMLEFT = (0,SCREEN_HEIGHT-50)
SCREEN_TOPRIGHT = (SCREEN_WIDTH-50,0)
SCREEN_BOTTOMRIGHT = (SCREEN_WIDTH-50,SCREEN_HEIGHT-50)

IMAGES_DIRECTORY = "Resources\\Images"
MUSIC_DIRECTORY = "Resources\\Music"
CARD_DIRECTORY = IMAGES_DIRECTORY+"\\cards"
CHIPS_DIRECTORY = IMAGES_DIRECTORY+"\\chips"

BACKGROUND_MUSIC = MUSIC_DIRECTORY+"\\background.mp3"   
CLICK_SOUND = MUSIC_DIRECTORY+"\\click.mp3"
MODE_SOUND = MUSIC_DIRECTORY+"\\mode.mp3"
LOSE_SOUND = MUSIC_DIRECTORY+"\\lost.mp3"
WIN_SOUND = MUSIC_DIRECTORY+"\\win.mp3"
PIOCHE_SOUND = MUSIC_DIRECTORY+"\\pioche.mp3"
WRONG_SOUND = MUSIC_DIRECTORY+"\\wrong.mp3"

TEXTANIMATIONFRAMES = 10
# Fonts
MAINFONT = {
    "source": "Resources\\Lemosty.otf",
    "size": 30,
}
# Colors
COLORS = {
    "black": (0,0,0),
    "white": (255,255,255),
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255),
}

inner_offset=7
offsetY = 30
offsetX = 12.5

# ******************* Positions *******************
GENERAL_POSITIONS = {
    "credits": (SCREEN_CENTER[0]-290,SCREEN_HEIGHT-50),
    "mise": (SCREEN_CENTER[0]+170,SCREEN_HEIGHT-50),
    "tour": (SCREEN_TOPLEFT[0]+offsetX,SCREEN_TOPLEFT[1]+inner_offset),
    "reward": (SCREEN_TOPLEFT[0]+offsetX,SCREEN_TOPLEFT[1]+offsetY+inner_offset),
    "misemin": (SCREEN_TOPLEFT[0]+offsetX,SCREEN_TOPLEFT[1]+offsetY*2+inner_offset),
    "misemax": (SCREEN_TOPLEFT[0]+offsetX,SCREEN_TOPLEFT[1]+offsetY*3+inner_offset),
    "bet_mode" : (SCREEN_CENTER[0]-290,SCREEN_HEIGHT-50),
    "name": (SCREEN_CENTER[0]-180,SCREEN_CENTER[1]-40),
    "mode_single": (SCREEN_CENTER[0]-70,SCREEN_CENTER[1]+65),
    "banquier": (SCREEN_CENTER[0]-70,SCREEN_CENTER[1]-190),
}
# ******************* Designs **********************

# *******************  Card  ***********************
CARD_DESIGN = {
    "Joueur 1": {
        "place": (SCREEN_CENTER[0]-60,SCREEN_CENTER[1]+110),
    },
    "Banque": {
        "place": (SCREEN_CENTER[0]-60,SCREEN_CENTER[1]-320),
    },
    "size": (70,120),
}

# *******************  Buttons  **********************
STOPBTN_DESIGN = {
    "place": (SCREEN_BOTTOMRIGHT[0]-100,SCREEN_BOTTOMRIGHT[1]-80),
    "size": (100,50),
    "text": "Stop",
    "font": {
        "size": 35,
        "color": COLORS["black"],
        "fillcolors": {
            "normal": "#F42124",
            "hover": "#B60E11",
            "pressed": "#750305",
        }
    }
}

PIOCHERBTN_DESIGN = {
    "place": (STOPBTN_DESIGN["place"][0],STOPBTN_DESIGN["place"][1]-80),
    "size": (100,50),
    "text": "Piocher",
    "font": {
        "size": 29,
        "color": COLORS["black"],
        "fillcolors": {
            "normal": "#7AFF16",
            "hover": "#5AC707",
            "pressed": "#439B02",
        }
    }
}

REGLESBTN_DESIGN = {
    "place": SCREEN_BOTTOMLEFT,
    "size": (30,75),
    "text": "?",
    "font": {
        "size": 40,
        "color": COLORS["black"],
        "fillcolors": {
            "normal": "#7AFF16",
            "hover": "#5AC707",
            "pressed": "#439B02",
        }
    }
}

COINBTN_DESIGN = {
    "sources": {
        "5": CHIPS_DIRECTORY+"\\5",
        "10": CHIPS_DIRECTORY+"\\10",
        "50": CHIPS_DIRECTORY+"\\50",
        "100": CHIPS_DIRECTORY+"\\100",
    },

    "places":{
        "5": (SCREEN_CENTER[0]-165,SCREEN_CENTER[1]+240),
        "10": ( SCREEN_CENTER[0]-65,SCREEN_CENTER[1]+240),
        "50": ( SCREEN_CENTER[0]+35,SCREEN_CENTER[1]+240),
        "100": (SCREEN_CENTER[0]+135,SCREEN_CENTER[1]+240),
    },

    "size": (100,100),
    "text": "",
}

BETMODEBTN_DESIGN = {
    "place": PIOCHERBTN_DESIGN["place"],
    "size": (100,50),
    "text": "Ajout",
    "font": {
        "size": 29,
        "color": COLORS["black"],
        "fillcolors": {
            "normal": "#7AFF16",
            "hover": "#5AC707",
            "pressed": "#439B02",
        }
    }
}

CONCLUDEBETBTN_DESIGN = {
    "place": STOPBTN_DESIGN["place"],
    "size": (100,50),
    "text": "Valider",
    "font": {
        "size": 29,
        "color": COLORS["black"],
        "fillcolors": {
            "normal": "#7AFF16",
            "hover": "#5AC707",
            "pressed": "#439B02",
        }
    }
}

REMATCHBTN_DESIGN = {
    "place": PIOCHERBTN_DESIGN["place"],
    "size": PIOCHERBTN_DESIGN["size"],
    "text": "Continuer",
    "font": {
        "size": 45,
        "color": COLORS["black"],
        "fillcolors": {
            "normal": "#7AFF16",
            "hover": "#5AC707",
            "pressed": "#439B02",
        }
    }
}

SINGLEBTN_DESIGN = {
    "place": (SCREEN_CENTER[0]-150,SCREEN_CENTER[1]+50),
    "size": (300,100),
    "text": "Solo",
    "font": {
        "size": 60,
        "color": COLORS["black"],
        "fillcolors": {
            "normal": "#7AFF16",
            "hover": "#5AC707",
            "pressed": "#439B02",
        }
    }
}

MULTIBTN_DESIGN = {
    "place": (SCREEN_CENTER[0]-150,SCREEN_CENTER[1]+200),
    "size": (300,100),
    "text": "Multi",
    "font": {
        "size": 60,
        "color": COLORS["black"],
        "fillcolors": {
            "normal": "#7AFF16",
            "hover": "#5AC707",
            "pressed": "#439B02",
        }
    }
}

# ******************* Colors to be changed ************************
general_colors = {
    "credits": COLORS["white"],
    "mise": COLORS["white"],
    "tour": COLORS["white"],
    "reward": COLORS["white"],
    "misemin": COLORS["white"],
    "misemax": COLORS["white"],
    "bet_mode": COLORS["white"],
    "name": COLORS["white"],
    "mode_single": COLORS["white"],
    "banquier": COLORS["white"],
}

# ***************************** Images *****************************
screen = pygame.display.set_mode(SCREEN_SIZE)
background = pygame.image.load(IMAGES_DIRECTORY+"\\fond.png").convert()
menu_background = pygame.image.load(IMAGES_DIRECTORY+"\\menu.png").convert()
mon_icone = pygame.image.load(IMAGES_DIRECTORY+"\\icon.png").convert_alpha()

# ***************************** Fonctions utilitaires ********************
def create_window():
    pygame.display.set_caption("Blackjack")
   # pygame.display.set_icon(mon_icone)
    screen.blit(resize_img(background,SCREEN_SIZE),(0,0))
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    pygame.display.set_icon(mon_icone)
    return screen

def play_sound(sound,type,volume,loops):
    if type == "sound":
        pygame.mixer.Sound(sound).play()
    elif type == "music":
        pygame.mixer.music.load(sound)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops)

def get_font(size):
    return pygame.font.Font(MAINFONT["source"],size)

def resize_img(img,newScale):
    return pygame.transform.scale(img,newScale)

def refresh_background(screen,background):
    screen.blit(resize_img(background,(SCREEN_WIDTH,SCREEN_HEIGHT)),(0,0))

# ***************************** Draw Fonctions *****************************
def draw_text(screen,text, size, color, pos):
    font = get_font(size)

    shadow_surface = font.render(text, True, COLORS["black"])
    shadow_rect = shadow_surface.get_rect()
    shadow_rect.topleft = (pos[0]+1, pos[1]+1)
    screen.blit(shadow_surface, shadow_rect)

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (pos[0], pos[1])
    screen.blit(text_surface, text_rect)

def draw_button(screen,button,center=True,Image=None):
    if Image != None:
        screen.blit(Image,(button.x,button.y))
    elif button.text != "":   
        color = button.currentFillColor
        buttonFont = get_font(button.fontSize)
        pygame.draw.rect(screen, color, button.buttonRect)
        buttonSurf = buttonFont.render(button.text, True, button.fontcolor)
        Ypos = button.y
        Xpos = button.x

        if center:
            Ypos = button.y+button.height/2-button.fontSize/2
            Xpos = button.x

        screen.blit(buttonSurf,(Xpos,Ypos))