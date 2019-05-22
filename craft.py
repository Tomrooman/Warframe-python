from helper import Helper
from tkinter import Button, Entry, Frame
import json, datetime
import threading

class Craft:

    craft   = None
    helper  = None
    min     = None
    h       = None
    thread  = None

    def __init__(self):
        self.helper = Helper()
        with open('warframe.json') as f:
            self.craft = json.load(f)['craft']
            self.craft.sort(key=lambda craft: craft["finished"])

    def add_craftList(self, sous_menu, centerFrame):
        sous_menu.add_command (label = "En cours", command = lambda:self.show_craft('inprogress', centerFrame))
        sous_menu.add_command (label = "Rajouter", command = lambda:self.add_craft(centerFrame))
    
    def show_craft(self, mode, frame):
        if (mode == "inprogress"):
            if (self.thread):
                self.thread.cancel()
            self.helper.delete_frame(frame)
            self.helper.render_label(frame, 'Craft en cours', 'title')
            self.helper.render_label(frame, '')
            for i in range(0, len(self.craft)):
                self.helper.render_frame_event(frame, self.craft[i], self.choice)
            self.update_countdown(frame)

    def update_countdown(self, frame, choice = False):
        count = 0
        with open('warframe.json') as f:
            craft = json.load(f)['craft']
            craft.sort(key=lambda craft: craft["finished"])
        for widget in frame.winfo_children():
            for label in widget.winfo_children():
                if (str(label)[-1:] == "2"):
                    if (choice):
                        difference = self.helper.take_difference_date(choice['finished'])
                    else:
                        difference = self.helper.take_difference_date(self.craft[count]['finished'])
                    difference = self.helper.render_count_down(difference)
                    if (difference):
                        label.configure(text="Temps restant --> " + difference)
                    else:
                        label.configure(text="Va récupérer ton item !")
                    count = count + 1
        self.thread = threading.Timer(1, lambda: self.update_countdown(frame, choice))
        self.thread.start()

    def add_craft(self, frame):
        self.helper.delete_frame(frame)
        self.helper.render_label(frame, 'Rajouter un craft', 'title')
        self.helper.render_label(frame, '')
        self.helper.render_label(frame, "Nom", False, True)
        name = Entry(frame, width=20)
        name.pack(fill="x")
        self.helper.render_label(frame, '')
        self.helper.render_label(frame, 'Heures', False, True)
        heures = Entry(frame, width=7)
        heures.pack(fill="x")
        self.helper.render_label(frame, '')
        self.helper.render_label(frame, "Minutes", False, True)
        minutes = Entry(frame, width=7)
        minutes.pack(fill="x")
        self.helper.render_label(frame, '')
        button = Button(frame, text='Confirmer', command = lambda:self.confirm_add_craft(name.get(), heures.get(), minutes.get(), frame))
        if (self.helper.skin == "night"):
            button = Button(frame, text='Confirmer', command = lambda:self.confirm_add_craft(name.get(), heures.get(), minutes.get(), frame), background="#1F2C38", foreground="white")
        button.pack()

    def confirm_add_craft(self, name, heures, minutes, frame):
        if (name and heures or name and minutes):
            duration = 0
            if (heures):
                try:
                    int(heures)
                    duration = int(heures) * 60
                except:
                    return
            if (minutes):
                try:
                    int(minutes)
                    duration += int(minutes)
                except:
                    return
            added = datetime.datetime.now()
            finished =  added + datetime.timedelta(minutes=duration)
            self.craft.append({
                'title': name,
                'finished': finished.strftime("%d-%m-%Y %H:%M:%S"),
                "added" : added.strftime("%d-%m-%Y %H:%M:%S")
            })
            self.helper.change_json('craft', self.craft)
            self.show_craft('inprogress', frame)

    def choice(self, infos, frame, e):
        self.helper.delete_frame(frame)
        if (self.thread):
            self.thread.cancel()
        self.helper.render_label(frame, 'Supprimer', 'title')
        self.helper.render_label(frame, '')
        self.helper.render_frame_event(frame, infos, self.choice)
        if (self.helper.skin == 'night'):
            Button(frame, text='Oui', command = lambda:self.delete_choice(infos, frame), width=15, background="#1F2C38", foreground="white").pack(side="left")
            Button(frame, text='Non', command = lambda:self.show_craft('inprogress', frame), width=15, bg="#1F2C38", fg="white").pack(side="right")
        else:
            Button(frame, text='Oui', command = lambda:self.delete_choice(infos, frame), width=15).pack()
            Button(frame, text='Non', command = lambda:self.show_craft('inprogress', frame), width=15).pack()
        self.update_countdown(frame, infos)

    def delete_choice(self, infos, frame):
        self.craft.remove(infos)
        self.helper.change_json('craft', self.craft)
        self.show_craft('inprogress', frame)