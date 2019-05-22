from tkinter    import *

from planetes   import Planetes
from ressources import Ressources
from helper     import Helper
from craft      import Craft

class Warframe_teller:

    root            = None
    centerFrame     = None
    planetes        = None
    ressources      = None
    skin            = None
    helper          = None
    craft           = None

    def __init__(self):
        self.root = Tk()
        self.root.geometry('+100+100')
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.craft = Craft()
        self.planetes = Planetes()
        self.ressources = Ressources()
        self.helper = Helper()
        self.skin = self.helper.skin
        self.root.wm_title("Warframe teller")
        self.createCenterFrame()
        self.menu()

    def exit(self):
        if (self.craft.thread):
            self.craft.thread.cancel()
        sys.exit(0)

    def mainloop(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            if (self.craft.thread):
                self.craft.thread.cancel()
            sys.exit(0)
            

    def clickk(self, event):
        if (self.craft.thread):
            self.craft.thread.cancel()

    def menu(self):
        m = Menu(self.root)
        
        sm1 = Menu(self.root, tearoff=0)
        m.bind("<<MenuSelect>>", self.clickk)
        sm2 = Menu(self.root, tearoff=0)
        sm3 = Menu(self.root, tearoff=0)
        sm4 = Menu(self.root, tearoff=0)
        day = ''
        night = ''
        var = StringVar()
        if (self.skin == 'night'):
            night = '* '
        if (self.skin == 'day'):
            day = '* '
        m.add_cascade(label="Craft", menu=sm4)
        m.add_cascade (label = "Planetes", menu = sm1)
        m.add_cascade(label = 'Ressources', menu = sm2)
        m.add_cascade(label='Thème', menu=sm3)
        night = '* '
        day = ''
        if (self.helper.skin == 'day'):
            night = ''
            day = '* '
        sm3.add_radiobutton(label=day + "Jour", value="day", variable=var, command = lambda:self.helper.change_json('skin', 'day'))
        sm3.add_radiobutton(label=night + "Nuit", value="night", variable=var, command = lambda:self.helper.change_json('skin', 'night'))
        
        self.craft.add_craftList(sm4, self.centerFrame)
        self.planetes.add_planetes(sm1, self.centerFrame)
        self.ressources.add_ressources(sm2, self.centerFrame)
        self.root.config(menu = m, width = 300)
            
    def createCenterFrame(self):
        if (self.skin == 'day'):
            skin = "Jour"
            self.centerFrame = Frame(self.root, width=380, height = 300, padx=50, pady=25)
        else:
            skin = 'Nuit'
            self.centerFrame = Frame(self.root, width=380, height = 300, padx=50, pady=25, background="#1F2C38")
        self.centerFrame.pack()
        self.helper.render_label(self.centerFrame, "Bienvenue sur warframe teller", "title")
        self.helper.render_label(self.centerFrame, "")
        self.helper.render_label(self.centerFrame, "Thème : " + skin, "subtitle")

teller = Warframe_teller()
teller.mainloop()
