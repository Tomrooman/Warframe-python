from tkinter    import *
from math import *
import os, json, datetime

class Helper:

    titleFont       = ('Georgia', 20)
    subtitleFont    = ('Georgia', 16)
    textFont        = ('Georgia', 13)
    skin            = None

    def __init__(self):
        with open('warframe.json') as f:
            self.skin = json.load(f)['skin']

    def change_json(self, toreplace, value):
        jsonFile = open("warframe.json", "r")
        data = json.load(jsonFile)
        data[toreplace] = value

        jsonFile = open('warframe.json', 'w')
        jsonFile.write(json.dumps(data))
        jsonFile.close()
        if (toreplace == 'skin'):
            os.execl(sys.executable, sys.executable, *sys.argv)

    def delete_frame(self, frame, thrad = False):
        for widget in frame.winfo_children():
            widget.destroy()

    def render_label(self, frame, text, font = False, anchor = False):
        if (font == 'title'):
            fontPolice = self.titleFont
        elif (font == "subtitle"):
            fontPolice = self.subtitleFont
        else:
            fontPolice = self.textFont
        if (self.skin == 'night'):
            if (anchor):
                Label(frame, text=text, background="#1F2C38", foreground="white", font=fontPolice).pack(anchor="w")
            else:
                Label(frame, text=text, background="#1F2C38", foreground="white", font=fontPolice).pack()
        else:
            if (anchor):
                Label(frame, text=text, font=fontPolice).pack(anchor="w")
            else:  
                Label(frame, text=text, font=fontPolice).pack()
    
    def take_difference_date(self, date):
        jour = int(date[:2])
        mois = int(date[3:-14])
        annee = int(date[6:-9])
        heure = int(date[11:-6])
        minutes = int(date[14:-3])
        secondes = int(date[-2:])
        now = datetime.datetime.now()
        time = datetime.datetime(annee, mois, jour, heure, minutes, secondes)
        diff = time.timestamp() - now.timestamp()
        if (str(diff)[:1] == "-"):
            return False
        else:
            diff = time - now
            days = diff.days
            seconds = diff.seconds
            hours = floor(seconds/3600)
            seconds -= hours * 3600
            minutes = floor(seconds / 60)
            seconds -= minutes * 60
            return {
                'days' : days,
                'hours' : hours,
                'minutes' : minutes,
                'seconds' : seconds
            }
    
    def render_count_down(self, difference):
        if (difference):
            countdown = ''
            if (difference["days"] > 0):
                countdown = str(difference["days"]) + ":"
            if (difference["hours"] > 0):
                countdown += str(difference["hours"]) + ":"
            if (difference["minutes"] > 0):
                countdown += str(difference["minutes"]) + ":"
                countdown += str(difference["seconds"])
            return countdown
        else:
            return False

    def render_frame_event(self, frame, craft, command):
        finished = craft['finished'].split(' ')
        difference = self.take_difference_date(craft['finished'])
        show_time = self.render_count_down(difference)
        if (self.skin == 'day'):
            newFrame = LabelFrame(frame, text=craft['title'], font=self.subtitleFont, padx=50, pady=20, borderwidth="3")
            label = Label(newFrame, text="Terminer le : " +finished[0] + " à " + finished[1][:-3])
            if (show_time):
                temps = Label(newFrame, text="Temps restant --> " + show_time, fg="#FF5B57")
            else:
                temps = Label(newFrame, text="Va récupérer ton item !", fg="#7DFF85")
        else:
            newFrame = LabelFrame(frame, text=craft['title'], font=self.subtitleFont, padx=50, pady=20, background="#1F2C38", foreground="white", borderwidth="3")
            label = Label(newFrame, text="Terminer le : " +finished[0] + " à " + finished[1][:-3], background="#1F2C38", foreground="white")
            if (show_time):
                temps = Label(newFrame, text="Temps restant --> " + show_time, background="#1F2C38", foreground="#FF5B57")
            else:
                temps = Label(newFrame, text="Va récupérer ton item !", background="#1F2C38", foreground="#7DFF85")
        newFrame.pack()
        label.pack()
        temps.pack()
        self.render_label(frame, '')
        newFrame.bind("<1>", lambda event: command(craft, frame, event))
        label.bind("<1>", lambda event: command(craft, frame, event))
        temps.bind("<1>", lambda event: command(craft, frame, event))