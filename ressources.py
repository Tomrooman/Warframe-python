from planetes import Planetes 
from tkinter  import *
from math     import *
from helper   import Helper

class Ressources:
    
    picture  = None
    planetes = None
    helper   = None

    def __init__(self):
        self.planetes = Planetes()
        self.helper = Helper()

    ressources = [
        "Ampoule de détonite", 
        "Capteurs neuronaux", 
        "Cellule orokin", 
        "Circuits", 
        "Cristal d'argon", 
        "Echantillon de fieldron", 
        "Echantillon mutagène", 
        "Ferrite", 
        "Gallium", 
        "Module de contrôle", 
        "Morphics", 
        "Nano spores", 
        "Neurodes", 
        "Pack polymère",
        "Plaque d'alliage", 
        "Plastides", 
        "Récupération", 
        "Rubedo"
    ]
   
    def add_ressources(self, sous_menu, centerFrame):
        for i in range(0, len(self.ressources)):
            sous_menu.add_command (label = self.ressources[i], command = lambda i=i: self.show_planetes(self.ressources[i], centerFrame))

    def show_planetes(self, ressource, centerFrame):
        planetesFrame = None
        results = []
        count = 0
        self.helper.delete_frame(centerFrame)
        self.helper.render_label(centerFrame, ressource.upper(), 'title')
        self.helper.render_label(centerFrame, '', self.helper.skin)
        for array in self.planetes.ressources:
            for array_ressource in array:
                if (array_ressource == ressource):
                    results.append(count)
            count = count + 1
        count = 0
        if (self.helper.skin == 'night'):
            planetesFrame = LabelFrame(centerFrame, text="PLANETES", font=self.helper.subtitleFont, padx=50, pady=20, background="#1F2C38", foreground="white", borderwidth="3")
        else:
            planetesFrame = LabelFrame(centerFrame, text="PLANETES", font=self.helper.subtitleFont, padx=50, pady=20, borderwidth="3")
        planetesFrame.pack(fill="x")
        for index in results:
            self.helper.render_label(planetesFrame, self.planetes.planetes[index], False, True)
            count = count + 1
        self.helper.render_label(centerFrame, '')
