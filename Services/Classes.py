from Services.Design import * # Import all design
from random import randint
# Classes
# ****************************** Players / Banquier ****************************** #
class newPlayer:
    def __init__(self,name):
        self.name = name
        self.cartes = {}
        self.n_cartes = 0

        self.credits = 145
        self.creditsColor = COLORS["white"]
        self.mise = 5
        self.miseColor = COLORS["white"]
        self.animationFrames = 0

        self.maxbet = 0
        self.misebet = 0
        self.score = 0
        self.betmode = "Add"
        self.status = self.name+"Bet"
        # Data to be saved
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.totalmoneywon = 0
        self.totalmoneylost = 0
        # Boutons
        self.buttons = {
            "stop": newButton(STOPBTN_DESIGN,self.stop_tour),
            "piocher": newButton(PIOCHERBTN_DESIGN,self.piocher),
            "regles": newButton(REGLESBTN_DESIGN,self.regles),
            "betmode": newButton(BETMODEBTN_DESIGN,self.change_bet),
            "concludebet": newButton(CONCLUDEBETBTN_DESIGN,self.conclude_bet),
        }

        # Coin buttons
        for i in COINBTN_DESIGN["places"].keys():
           self.buttons["coin_"+i] = newButton(COINBTN_DESIGN,self.add_bet,i)
    # ****************************** Button Fonctions ****************************** #
    def conclude_bet(self):
        self.status = self.name+"Game"
        self.piocher()
        self.piocher()
    def change_bet(self,btn):
        if self.betmode == "Add":
            self.betmode = "Remove"
            btn.text = "Retrait"
            btn.fillColors["normal"] = STOPBTN_DESIGN["font"]["fillcolors"]["normal"]
            btn.fillColors["hover"] = STOPBTN_DESIGN["font"]["fillcolors"]["hover"]
            btn.fillColors["pressed"] = STOPBTN_DESIGN["font"]["fillcolors"]["pressed"]
        else:
            self.betmode = "Add"
            btn.text = "Ajout"
            btn.fillColors["normal"] = PIOCHERBTN_DESIGN["font"]["fillcolors"]["normal"]
            btn.fillColors["hover"] = PIOCHERBTN_DESIGN["font"]["fillcolors"]["hover"]
            btn.fillColors["pressed"] = PIOCHERBTN_DESIGN["font"]["fillcolors"]["pressed"]
            print(btn.fillColors["hover"])
    def add_bet(self,chip_num):
        chip_num = int(chip_num)
        colors = "normal"
        if self.betmode == "Remove":
            colors = "inverted"
            chip_num = -chip_num

        # ****************************** Bet Validation/Animations ****************************** #
        Invalid = False

        if (self.mise + chip_num < 0):
            self.miseColor = COLORS["red"]
            Invalid = True
        elif (self.credits - chip_num < 0):
            self.creditsColor = COLORS["red"]
            Invalid = True
        elif (self.mise + chip_num > self.misemax):
            self.miseColor = COLORS["red"]
            general_colors["misemax"] = COLORS["red"]
            self.buttons["betmode"].fillColors["normal"] = COLORS["red"]
            Invalid = True
        elif (self.mise + chip_num < self.misemin and self.misemin < 100):
            self.miseColor = COLORS["red"]
            general_colors["misemin"] = COLORS["red"]
            self.buttons["betmode"].fillColors["normal"] = COLORS["green"]
            Invalid = True

        self.animationFrames = TEXTANIMATIONFRAMES

        # ****************************** Increase/Decrease of bet ****************************** #
        if Invalid == False:
            if colors == "inverted":
                self.miseColor = COLORS["red"]
                self.creditsColor = COLORS["green"]
            else:
                self.miseColor = COLORS["green"]
                self.creditsColor = COLORS["red"]

            general_colors["reward"] = self.miseColor

            self.mise += chip_num
            self.credits -= chip_num
        else:
            play_sound(WRONG_SOUND,"sound",0.4,0)
    def stop_tour(self):
        self.status = self.name+"Conclusion"
    def piocher(self):
        if self.score <= 21:
            carte = newCarte(self.n_cartes,self.name)
            self.n_cartes += 1
            self.score += carte.value
            self.cartes[len(self.cartes)] = carte
            play_sound(PIOCHE_SOUND,"sound",0.4,0)
        else:
            play_sound(WRONG_SOUND,"sound",0.4,0)
    def regles(self):
        pass
    # ****************************** Main Fonctions ****************************** #
    def lost(self):
        self.losses += 1
        self.credits += self.mise
        self.totalmoneylost += self.mise
    def won(self):
        self.wins += 1
        self.mise = 0
        self.totalmoneywon += self.mise
    def draw(self):
        self.draws += 1
        self.credits += self.mise/2
        self.totalmoneywon += self.mise/2
    def remise(self):
        self.losses += 1
        self.credits += self.mise
    # ****************************** UI Functions ****************************** #
    def interact(self):
        for i in self.buttons.keys():
            if self.status == self.name+"Bet":
                if "coin_" in i:
                    self.buttons[i].main_behaviour(i[5:])
                if i == "betmode" or i == "concludebet":
                    self.buttons[i].main_behaviour()
            elif self.status == self.name+"Game":
                if i == "stop" or i == "piocher":
                    self.buttons[i].main_behaviour()
            if i == "regles":
                self.buttons[i].main_behaviour()      
    def draw(self,screen):
        # ****************************** Background ****************************** #
        draw_text(screen,"Credits: "+str(self.credits)+"$", MAINFONT["size"], self.creditsColor, GENERAL_POSITIONS["credits"])
        draw_text(screen,"Mise: "+str(self.mise)+"$", MAINFONT["size"], self.miseColor, GENERAL_POSITIONS["mise"])

        if self.animationFrames != 0:
            self.animationFrames -= 1

            if (self.creditsColor != COLORS["white"] or general_colors["misemin"] or general_colors["misemax"]) and self.animationFrames == 0:
                self.creditsColor = COLORS["white"]
                self.miseColor = COLORS["white"]
                general_colors["reward"] = COLORS["white"]
                general_colors["misemin"] = COLORS["white"]
                general_colors["misemax"] = COLORS["white"]
                if self.betmode == "Add":
                    self.buttons["betmode"].fillColors["normal"] = COLORS["green"]
                else:
                    self.buttons["betmode"].fillColors["normal"] = COLORS["red"]
        # ****************************** Buttons ****************************** #
        if self.status == self.name+"Bet":
            for i in COINBTN_DESIGN["places"].keys():
               coin_btn = self.buttons["coin_"+i]
               draw_button(screen,coin_btn,False,coin_btn.img)

            draw_button(screen,self.buttons["betmode"])
            draw_button(screen,self.buttons["concludebet"])
        elif self.status == self.name+"Game":
            draw_button(screen,self.buttons["stop"])
            draw_button(screen,self.buttons["piocher"])
        
        draw_button(screen,self.buttons["regles"],False) 
        # ****************************** Cartes ****************************** #
        for i in self.cartes:
            carte = self.cartes[i]
            draw_button(screen,carte,False,carte.img)
class newBanquier:
    def __init__(self):
        self.name = "Banque"
        self.cartes = {}
        self.credits = 10000
        self.n_cartes = 0
        self.mise = 0
        self.score = 0
        self.pioche = False
        self.conclusion = False
    # ****************************** Button Fonctions ****************************** #
    def LogiqueCartes(self):
        """
        Choisi le n_cartes à être pioché à partir du score banquier

        Parameters: 
        ----------
        score: int

        Returns: 
        int
        Quantité de cartes à être pioché
        """
        n_cartes = 0

        if self.score == 0: 
            n_cartes = randint(2,5)
        elif self.score < 18: 
            n_cartes = randint(1,3)
        elif self.score <= 18: 
            n_cartes = 1

        return n_cartes
    def piocher(self,n_cartes=1):
        for i in range(n_cartes):
            if self.score < 21:
                carte = newCarte(self.n_cartes,self.name)
                self.n_cartes += 1
                self.score += carte.value
                self.cartes[len(self.cartes)] = carte
    # ****************************** Main Fonctions ****************************** #
    def draw(self,screen):
        for i in self.cartes:
            carte = self.cartes[i]
            image = carte.img
            if i == 0 and self.conclusion == False:
                image = pygame.image.load(CARD_DIRECTORY+"\\Dos.png").convert_alpha()
                image = resize_img(image,(carte.width,carte.height))
            draw_button(screen,carte,False,image)
# ****************************** UI Components ****************************** #
class newButton:
    def __init__(self, preset_design,config_function=None,chip_num = None):
        self.width = preset_design["size"][0]
        self.height = preset_design["size"][1]
        self.text = preset_design["text"]
        self.config_function = config_function
        self.alreadyPressed = False
        self.hovered = False
        if chip_num != None:
            self.source = preset_design["sources"][chip_num]
            self.img = pygame.image.load(self.source+"\\chip.png").convert_alpha()
            self.chip_num = chip_num
            self.x = preset_design["places"][chip_num][0]
            self.y = preset_design["places"][chip_num][1]
        else:
            self.x = preset_design["place"][0]
            self.y = preset_design["place"][1]
            self.fontSize = preset_design["font"]["size"]
            self.fontcolor = preset_design["font"]["color"]
            self.fillColors = preset_design["font"]["fillcolors"]
            self.currentFillColor = self.fillColors["normal"]

        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

    def main_behaviour(self,chip_num=None):
        state = "normal"
        if self.buttonRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.alreadyPressed and self.hovered:
                state = "pressed"
                self.alreadyPressed = True
                if chip_num != None:
                    self.config_function(chip_num)
                elif self.text == "Ajout" or self.text == "Retrait":
                    self.config_function(self)
                else: 
                    self.config_function()

                # if the button is solo or multi
                if self.text == "Solo" or self.text == "Multi":
                    play_sound(MODE_SOUND,"sound",0.4,0)
                elif self.text == "Piocher":
                    pass
                else:
                    play_sound(CLICK_SOUND,"sound",0.4,0)
                

            elif not pygame.mouse.get_pressed()[0]:
                state = "hover"
                self.hovered = True
                if self.alreadyPressed:
                    self.alreadyPressed = False
        else:
            self.hovered = False
        
        
        if chip_num != None:
            if state == "hover":
                self.img = pygame.image.load(self.source+"\\fade.png").convert_alpha()
            else:
                self.img = pygame.image.load(self.source+"\\chip.png").convert_alpha()
        else: 
            self.currentFillColor = self.fillColors[state]
class newCarte:
    def __init__(self,n_card=1,name="Joueur 1"):
        value_table = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]

        self.name = value_table[randint(0,12)]
        self.width = CARD_DESIGN["size"][0] 
        self.height = CARD_DESIGN["size"][1]
        self.x = CARD_DESIGN[name]["place"][0]+25*n_card
        self.y = CARD_DESIGN[name]["place"][1]
        self.img = pygame.image.load(CARD_DIRECTORY+"\\"+self.name+"\\"+str(randint(1,4))+".png").convert_alpha()
        self.img = resize_img(self.img,(self.width,self.height))
        if self.name == "As":
            self.value = 11
        elif self.name == "Valet" or self.name == "Dame" or self.name == "Roi":
            self.value = 10
        else:
            self.value = int(self.name)
class newMenu:
    def __init__(self):
        self.buttons = {
            "single": newButton(SINGLEBTN_DESIGN,self.singlePlayer),
            "multi": newButton(MULTIBTN_DESIGN,self.multiPlayer),
            "regles": newButton(REGLESBTN_DESIGN,self.regles),
        }
        self.mode = None 
    def singlePlayer(self):
        self.mode = "single"
    def multiPlayer(self):
        self.mode = "multi"
    def regles(self):
        self.mode = "regles"
    def draw(self,screen):
        draw_text(screen,"Blackjack", MAINFONT["size"]*3, general_colors["name"], (GENERAL_POSITIONS["name"][0],GENERAL_POSITIONS["name"][1]-200))
        # Create an equal text but with a black color to make a shadow
        for i in self.buttons:
            draw_button(screen,self.buttons[i],True)
    def interact(self):
        for i in self.buttons:
            self.buttons[i].main_behaviour()
# ****************************** Main Logic ****************************** #
class newMatch: 
    # ****************************** Constructor ****************************** #
    def __init__(self,mode="single",scores=None):
        self.players = {}
        self.tour = 1
        self.reward = 0
        self.minbet = 5
        self.maxbet = 100
        self.mode = mode
        self.status = "Bet"
        self.scores = scores
        self.actor = "Joueur 1"
        self.message = "Choisissez votre mise"
        self.matchconclusion = False
        self.conclusion_btn = newButton(REMATCHBTN_DESIGN,self.nextMatch)
    # ****************************** Utility Functions ****************************** #
    def addPlayer(self,player):
        self.players[player.name] = player   
    def initalizePlayers(self,n_players):
        Banque = newBanquier()
        if self.mode == "single":
            n_players = 1
            
        for i in range(n_players):
            player = newPlayer("Joueur "+str(i+1))
            self.addPlayer(player)
            player.misemax = self.maxbet
            player.misemin = self.minbet

        self.addPlayer(Banque)     
    # ****************************** UI Functions ****************************** #  
    def draw_background_info(self,screen):
        # ****************************** Background ****************************** #
        draw_text(screen,"Tour: "+str(self.tour), MAINFONT["size"], general_colors["tour"], GENERAL_POSITIONS["tour"])
        draw_text(screen,"Récompense: "+str(self.reward)+"$", MAINFONT["size"], general_colors["reward"], GENERAL_POSITIONS["reward"])
        draw_text(screen,"Mise Min: "+str(self.minbet)+"$", MAINFONT["size"], general_colors["misemin"], GENERAL_POSITIONS["misemin"])
        draw_text(screen,"Mise Max: "+str(self.maxbet)+"$", MAINFONT["size"],general_colors["misemax"], GENERAL_POSITIONS["misemax"])
        # ****************************** Conditional Elements ****************************** #
        banque = self.players["Banque"]
        if banque.conclusion == True and self.conclusion_btn.alreadyPressed == False:
            draw_button(screen,self.conclusion_btn,True)
            self.conclusion_btn.main_behaviour()
        message = self.message
        messagePos = (GENERAL_POSITIONS["name"][0]-90,GENERAL_POSITIONS["name"][1])
        banque_text = "Banque: "+str(self.scores["Banque"])

        if self.status == self.actor+"Game":
            message = "Tour du "+self.actor
            messagePos = (messagePos[0]+60,messagePos[1])
        elif "Perdu" in self.message:
            messagePos = (messagePos[0]+70,messagePos[1])
        elif "Égalité" in self.message:
            messagePos = (messagePos[0]-20,messagePos[1])
        if "Game" in self.status:
            banque_text = "Banque: ??"

        draw_text(screen,message, MAINFONT["size"]*2, general_colors["name"], messagePos)
        draw_text(screen,banque_text,MAINFONT["size"], general_colors["banquier"], GENERAL_POSITIONS["banquier"])

        # ****************************** Mode ****************************** #
        if self.mode=="single":
            draw_text(screen,"Joueur 1: "+str(self.scores["Joueur 1"]), MAINFONT["size"], general_colors["mode_single"], GENERAL_POSITIONS["mode_single"])   
    # ****************************** Main Logic ****************************** #
    def Conclusion(self):
        # ****************************** Variables ****************************** #
        winner_table = {}
        equality = False
        conclusion = "personne"
        # ****************************** Score Recuperation ****************************** #
        for i in self.players:
            player = self.players[i]
            if player.score > 21:
                continue

            if len(winner_table) == 0:
                winner_table = [player.score,player.n_cartes,i]
            elif winner_table[0] < player.score and winner_table[1] < player.n_cartes:
                winner_table = [player.score,player.n_cartes,i]
            elif winner_table[0] == player.score and winner_table[1] == player.n_cartes:
                winner_table.append(player.score) 
                winner_table.append(player.n_cartes)
                winner_table.append(i)
                equality = True
        # ****************************** Score Validation ****************************** #
        if len(winner_table) == 0 or winner_table[0] > 21:
            self.message = "Personne n'a gagné :("
            conclusion = "personne"
        elif equality == True:
            self.message = "Égalité entre "+winner_table[2]+" et "+winner_table[3]
            conclusion = "egalite"
        else:
            self.message = winner_table[2]+" a gagné!! :D"
            conclusion = winner_table[2]
            
        # ****************************** SFX ****************************** #
        if len(winner_table) > 0 and winner_table[1] != "Banque":
            play_sound(WIN_SOUND,"sound",0.4,0)
        else:
            play_sound(LOSE_SOUND,"sound",0.4,0)    

        
        for i in self.players:
            player = self.players[i]
            if i == "Banque":
                continue
            
            if conclusion == "personne":
                player.remise()
            elif conclusion == "egalite":
                if player == self.players[winner_table[2]] or player == self.players[winner_table[6]]:
                    player.draw()
                else:
                    player.lost()
            else: 
                if player == self.players[conclusion]:
                    player.won()
                else:
                    player.lost()

    # ****************************** Reset ****************************** #   
    def nextMatch(self):
        # ****************************** Reset ****************************** #
        for i in self.players:
            player = self.players[i]
            player.cartes = {}
            player.n_cartes = 0
            player.score = 0
            player.status = player.name+"Bet"
            if player.name == "Banque": 
                player.pioche = False
                player.conclusion = False
            else:
                if player.credits > self.maxbet:
                    self.maxbet = player.credits
                    self.minbet = self.maxbet/20

                player.misemin = self.minbet    
                player.misemax = self.maxbet
                player.mise = 5
                player.credits -= 5
        self.status = "Bet"
        self.message = "Choisissez votre mise"
        self.tour += 1
        self.matchconclusion = False
        self.conclusion_btn.alreadyPressed = False
    # ****************************** Modes ****************************** #
    def singlePlayer(self,screen):
        player1 = self.players["Joueur 1"]
        banque = self.players["Banque"]

        if player1.credits < 0 or (player1.credits == 0 and player1.mise == 0):
            self.status = "GameOver"
            self.message = "Vous avez perdu"
            self.tour = 0
            self.reward = 0
            self.scores = {
                "Joueur 1": player1.score,
                "Banque": banque.score
            }

            player1.interact()
            player1.draw(screen)
            banque.draw(screen)
            return
        
        self.reward = player1.mise * 2
        self.status = player1.status
        self.scores = {
            "Joueur 1": player1.score,
            "Banque": banque.score
        }
        
        if self.status == player1.name+"Game" and banque.pioche == False:
            banque.pioche = True
            banque.piocher(2)
            
        elif self.status == player1.name+"Conclusion" and banque.conclusion == False:
            banque.conclusion = True
            n_cartes = banque.LogiqueCartes()
            banque.piocher(n_cartes)
        elif banque.conclusion == True and self.matchconclusion == False:
            self.matchconclusion = True
            print(self.Conclusion())

        player1.interact()
        player1.draw(screen)
        banque.draw(screen)
    def multiPlayers(self,screen):
        pass