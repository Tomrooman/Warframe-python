from tkinter import *
from math    import *
from helper  import Helper

class Planetes:
    
    picture = None
    helper  = None

    def __init__(self):
        self.helper = Helper()

    planetes = [
    'Cérès',
    'Epave orokin',
    'Eris',
    'Europe',
    'Forteresse kuva',
    'Jupiter',
    'Lua',
    'Mars',
    'Mercure',
    'Neant',
    'Neptune',
    'Phobos',
    'Pluton',
    'Saturne',
    'Sedna',
    'Terre',
    'Uranus',
    'Vénus'
    ]

    ressources = [
    ["Faction", "Grineer", "Niveaux", "12 - 25", "Plaque d'alliage", "Circuits", "Cellule orokin", "Ampoule de détonite"], #Cérès
    ["Faction", "Infesté", "Niveaux", "25 - 35", "Nano spores", "Echantillon mutagène", "Cellule orokin", "Neurodes"], #Epave
    ["Faction", "Infesté", "Niveaux", "34 - 45", "Nano spores", "Plastides", "Neurodes", "Echantillon mutagène"],  #Eris
    ["Faction", "Corpus", "Niveaux", "18 - 33", "Morphics", "Rubedo", "Echantillon de fieldron", "Module de contrôle"], #Europe
    ["Faction", "Grineer", "Niveaux", "28 - 37", "Récupération", "Circuits", "Capteurs neuronaux", "Ampoule de détonite"], #Forteresse kuva
    ["Faction", "Corpus", "Niveaux", "15 - 30", "Récupération", "Echantillon de fieldron", "Capteurs neuronaux", "Plaque d'alliage"],  #Jupiter
    ["Faction", "Corpus", "Niveaux", "25 - 30", "Ferrite", "Rubedo", "Neurodes", "Ampoule de détonite"], #Lua
    ["Faction", "Grineer", "Niveaux", "8 - 20", "Morphics", "Récupération", "Gallium", "Echantillon de fieldron"], #Mars
    ["Faction", "Infesté et Grineer", "Niveaux", "8 - 11", "Morphics", "Ferrite", "Pack polymère", "Ampoule de détonite"],  #Mercure
    ["Faction", "Orokin", "Niveaux", "10 - 50", "Ferrite", "Rubedo", "Cristal d'argon", "Module de contrôle"], #Neant
    ["Faction", "Corpus", "Niveaux", "28 - 40", "Nano spores", "Ferrite", "Module de contrôle", "Echantillon de fieldron"], #Neptune
    ["Faction", "Corpus", "Niveaux", "10 - 25", "Rubedo", "Plaque d'alliage", "Récupération", "Ampoule de détonite"],  #Phobos
    ["Faction", "Corpus", "Niveaux", "30 - 40", "Rubedo", "Morphics", "Plastides", "Plaque d'alliage"], #Pluton
    ["Faction", "Grineer", "Niveaux", "21 - 26", "Nano spores", "Plastides", "Cellule orokin", "Ampoule de détonite"], #Saturne
    ["Faction", "Grineer", "Niveaux", "30 - 40", "Rubedo", "Plaque d'alliage", "Récupération", "Ampoule de détonite"],  #Sedna
    ["Faction", "Grineer", 'Niveaux', "1 - 6", "Ferrite", "Rubedo", "Neurodes", "Ampoule de détonite" ], #Terre
    ["Faction", "Grineer", "Niveaux", "24 - 30", "Pack polymère", "Plastides", "Gallium", "Ampoule de détonite"], #Uranus
    ["Faction", "Corpus", "Niveaux", "3 - 11", "Plaque d'alliage", "Pack polymère", "Circuits", "Echantillon de fieldron"]   #Vénus
    ]

    def add_planetes(self, sous_menu, centerFrame):
        for i in range(0, len(self.planetes)):
            sous_menu.add_command (label = self.planetes[i], command = lambda i=i:self.show_ressources(self.planetes[i], centerFrame))

    def show_ressources(self, planete, centerFrame):
        self.helper.delete_frame(centerFrame)
        ressourceFrame = None
        infosFrame = None
        count = 0
        self.helper.render_label(centerFrame, planete.upper(), 'title')
        self.helper.render_label(centerFrame, '')
        for ressource in self.ressources[self.planetes.index(planete)]:
            count = count + 1
            if (count >= 5 ):
                if (count == 5):
                    self.helper.render_label(centerFrame, '')
                    if (self.helper.skin == 'night'):
                        
                        ressourceFrame = LabelFrame(centerFrame, text="RESSOURCES", font=self.helper.subtitleFont, padx=50, pady=20, background="#1F2C38", foreground="white", borderwidth="3")
                    else:
                        ressourceFrame = LabelFrame(centerFrame, text="RESSOURCES", font=self.helper.subtitleFont, padx=50, pady=20, borderwidth="3")
                    ressourceFrame.pack(fill="x")
                self.helper.render_label(ressourceFrame, ressource, False, True)
            else:
                if (count == 1):
                    if (self.helper.skin == 'night'):
                        infosFrame = LabelFrame(centerFrame, text="INFORMATIONS", font=self.helper.subtitleFont, padx=50, pady=20, background="#1F2C38", foreground="white", borderwidth="3")
                    else:
                        infosFrame = LabelFrame(centerFrame, text="INFORMATIONS", font=self.helper.subtitleFont, padx=50, pady=20, borderwidth="3")
                    infosFrame.pack(fill='x')
                if (count % 2 != 0):
                    self.helper.render_label(infosFrame, ressource + ' : ' + self.ressources[self.planetes.index(planete)][count], False, True)