#Wanda Garbocz, 09.09.20
import sys
from playsound import playsound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QCheckBox
#from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from pydub import AudioSegment
from pydub.playback import play
import random

class App (QWidget):
    mode41=None
    mode31=None
    mode32=None
    mode33=None
    mode34=None
    mode21=None
    mode22=None
    mode23=None
    mode24=None
    mode25=None
    mode26=None
    mode11=None
    mode12=None
    mode13=None
    mode14=None
    loopnumber=None
    songnum2=None
    songnum3=None
    songnum4=None
    timefade=None
    mode00=None

    @pyqtSlot()


    def click(self): 
        button = self.sender() 
        self.textbox.setText(button.text()) 

    def productclick(self):
        if self.buttonplay.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 1
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00=0
        else:
            self.mode00=1

        if self.buttonplay1.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 1
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay2.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 1
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay3.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 1
            self.mode00 = 0
        if self.buttonplay.isChecked() and self.buttonplay1.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 1
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay.isChecked() and self.buttonplay2.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 1
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay.isChecked() and self.buttonplay3.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 1
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay1.isChecked() and self.buttonplay2.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 1
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay1.isChecked() and self.buttonplay3.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 1
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay2.isChecked() and self.buttonplay3.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 1
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode00 = 0
            self.mode14 = 0
        if self.buttonplay.isChecked() and self.buttonplay1.isChecked() and self.buttonplay2.isChecked():
            self.mode31 = 0
            self.mode32 =1
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay.isChecked() and self.buttonplay1.isChecked() and self.buttonplay3.isChecked():
            self.mode31 = 1
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0
        if self.buttonplay3.isChecked() and self.buttonplay1.isChecked() and self.buttonplay2.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 0
            self.mode34 = 1
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode00 = 0
            self.mode14 = 0
        if self.buttonplay.isChecked() and self.buttonplay3.isChecked() and self.buttonplay2.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=0
            self.mode33 = 1
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode00 = 0
            self.mode13 = 0
            self.mode14 = 0
        if self.buttonplay.isChecked() and self.buttonplay1.isChecked() and self.buttonplay2.isChecked() and self.buttonplay3.isChecked():
            self.mode31 = 0
            self.mode32 =0
            self.mode41=1
            self.mode33 = 0
            self.mode34 = 0
            self.mode21 = 0
            self.mode22 = 0
            self.mode23 = 0
            self.mode24 = 0
            self.mode25 = 0
            self.mode26 = 0
            self.mode11 = 0
            self.mode12 = 0
            self.mode13 = 0
            self.mode14 = 0
            self.mode00 = 0



    def loopclick(self):
        button=self.sender()
        self.textbox6.setText(button.text())
        if self.textbox6.text()=='2':
            self.loopnumber=2
        elif self.textbox6.text()=='3':
            self.loopnumber=3
        elif self.textbox6.text()=='4':
            self.loopnumber=4
        elif self.textbox6.text()=='5':
            self.loopnumber=5

    def songnumclick(self):
        button = self.sender()
        self.textbox8.setText(button.text())
        if self.textbox8.text()=='2':
            self.songnum2=1
            self.songnum3=0
            self.songnum4=0
            print('2')
        elif self.textbox8.text()=='3':
            self.songnum2 =0
            self.songnum3 = 1
            self.songnum4 = 0
        elif self.textbox8.text()=='4':
            self.songnum2 = 0
            print('4')
            self.songnum3 = 0
            self.songnum4 = 1

    def timeclick(self):
        button = self.sender()
        self.textbox10.setText(button.text())
        if self.textbox10.text()=='Krotki':
            self.timefade=0.2
        elif self.textbox10.text()=='Sredni':
            self.timefade=0.5
        elif self.textbox10.text()=='Dlugi':
            self.timefade=1

    def play(self):

        if self.mode00==1:
            if self.textbox.text()=='Miau':
                print("odtwarzaniee")
                playsound('meow.wav')
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                playsound('dzwonek.wav')
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                playsound('Drum_Roll.wav')
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                playsound('Sci_fi.wav')

        elif self.mode11==1: #petla
            if self.textbox.text()=='Miau':
                print("mode11")
                song5 = AudioSegment.from_wav('meow.wav')
                song20 = song5 * self.loopnumber
                play(song20)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                print(self.loopnumber)
                song5= AudioSegment.from_wav('dzwonek.wav')
                song20 = song5 * self.loopnumber
                play(song20)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('Drum_Roll.wav')
                song20 = song5 * self.loopnumber
                play(song20)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('Sci_fi.wav')
                song20 = song5 * self.loopnumber
                play(song20)

        elif self.mode12 == 1:  #od tylu
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                play(song22)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                play(song22)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song2 = song.reverse()
                play(song2)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song2 = song.reverse()
                play(song2)

        elif self.mode13==1 and self.songnum2==1: #wastwowanie
            liczba=random.randint(0,30)
            if self.textbox.text()=='Miau':
                print("odtwarzanie")
                song5=AudioSegment.from_wav('meow.wav')
                length=len(song5)
                if liczba<=10:
                    mesh=AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba>10 and liczba<=20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed=mesh[:length].overlay(song5)
                play(mixed)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('dzwonek.wav')
                length = len(song5)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song5)
                play(mixed)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(song5)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song5)
                play(mixed)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('Sci_fi.wav')
                length = len(song5)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('meow.wav')
                mixed = mesh[:length].overlay(song5)
                play(mixed)

        elif self.mode13==1 and self.songnum3==1: #wastwowanie
            liczba=random.randint(0,30)
            if self.textbox.text()=='Miau':
                print("odtwarzanie")
                song5=AudioSegment.from_wav('meow.wav')
                length=len(song5)
                if liczba<=10:
                    mesh1=AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba>10 and liczba<=20:
                    mesh1 = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh1 = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed=mesh1[:length].overlay(song5)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                play(mixed2)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('dzwonek.wav')
                length = len(song5)
                if liczba<=10:
                    mesh1=AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba>10 and liczba<=20:
                    mesh1 = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh1 = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                mixed=mesh1[:length].overlay(song5)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                play(mixed2)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(song5)
                if liczba<=10:
                    mesh1=AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba>10 and liczba<=20:
                    mesh1 = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh1 = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed=mesh1[:length].overlay(song5)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                play(mixed2)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('Sci_fi.wav')
                length = len(song5)
                if liczba<=10:
                    mesh1=AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                elif liczba>10 and liczba<=20:
                    mesh1 = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh1 = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed=mesh1[:length].overlay(song5)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                play(mixed2)

        elif self.mode13==1 and self.songnum4==1: #wastwowanie
            print("odtwarzanie")
            song5=AudioSegment.from_wav('Sci_fi.wav')
            length=len(song5)
            mesh1=AudioSegment.from_wav('dzwonek.wav')
            mixed=mesh1[:length].overlay(song5)
            length2=len(mixed)
            mesh2=AudioSegment.from_wav('Drum_Roll.wav')
            mixed2=mesh2[:length2].overlay(mixed)
            mesh3=AudioSegment.from_wav('meow.wav')
            length3=len(mixed2)
            mixed3=mesh3[:length3].overlay(mixed2)
            play(mixed3)

        elif self.mode14==1:
            if self.textbox.text()=='Miau':
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('meow.wav')
                length = len(loop2)
                fade_time = int(length * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('dzwonek.wav')
                length = len(loop2)
                fade_time = int(length * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(loop2)
                fade_time = int(length * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Sci_fi.wav')
                length = len(loop2)
                fade_time = int(length * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode26==1 and self.songnum2==1: #warstwowanie i gaszenie
            liczba = random.randint(0, 30)
            if self.textbox.text()=='Miau':
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('meow.wav')
                length = len(loop2)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(loop2)
                length2 = len(mixed)
                fade_time = int(length2 * self.timefade)
                faded = mixed.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('dzwonek.wav')
                length = len(loop2)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(loop2)
                length2 = len(mixed)
                fade_time = int(length2 * self.timefade)
                faded = mixed.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(loop2)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(loop2)
                length2 = len(mixed)
                fade_time = int(length2 * self.timefade)
                faded = mixed.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Sci_fi.wav')
                length = len(loop2)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('meow.wav')
                mixed = mesh[:length].overlay(loop2)
                length2 = len(mixed)
                fade_time = int(length2 * self.timefade)
                faded = mixed.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode26==1 and self.songnum3==1: #warstwowanie i gaszenie
            liczba = random.randint(0, 30)
            if self.textbox.text()=='Miau':
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('meow.wav')
                length = len(loop2)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(loop2)
                length2 = len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                length3=len(mixed2)
                fade_time = int(length3 * self.timefade)
                faded = mixed2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('dzwonek.wav')
                length = len(loop2)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2 = AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2 = AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2 = AudioSegment.from_wav('meow.wav')
                mixed = mesh[:length].overlay(loop2)
                length2 = len(mixed)
                mixed2 = mesh2[:length2].overlay(mixed)
                length3 = len(mixed2)
                fade_time = int(length3 * self.timefade)
                faded = mixed2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(loop2)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(loop2)
                length2 = len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                length3=len(mixed2)
                fade_time = int(length3 * self.timefade)
                faded = mixed2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Sci_fi.wav')
                length = len(loop2)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(loop2)
                length2 = len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                length3=len(mixed2)
                fade_time = int(length3 * self.timefade)
                faded = mixed2.fade_in(fade_time).fade_out(fade_time)
                play(faded)


        elif self.mode26==1 and self.songnum4==1: #warstwowanie i gaszenie
            print("odtwarzanie")
            loop2 = AudioSegment.from_wav('dzwonek.wav')
            length = len(loop2)
            mesh = AudioSegment.from_wav('Sci_fi.wav')
            mixed = mesh[:length].overlay(loop2)
            mesh2=AudioSegment.from_wav('Drum_Roll.wav')
            length2=len(mixed)
            mixed2=mesh2[:length2].overlay(mixed)
            mesh3=AudioSegment.from_wav('meow.wav')
            length3=len(mixed2)
            mixed3=mesh3[:length3].overlay(mixed2)
            length4=len(mixed3)
            fade_time = int(length4 * self.timefade)
            faded = mixed3.fade_in(fade_time).fade_out(fade_time)
            play(faded)

        elif self.mode24==1 and self.songnum2==1: #warstwowanie i od tylu
            liczba = random.randint(0, 30)
            if self.textbox.text()=='Miau':
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('meow.wav')
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                song2 = loop2.reverse()
                length = len(song2)
                mixed = mesh[:length].overlay(song2)
                play(mixed)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('dzwonek.wav')
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                song2 = loop2.reverse()
                length=len(song2)
                mixed = mesh[:length].overlay(song2)
                play(mixed)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Drum_Roll.wav')
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                song2 = loop2.reverse()
                length = len(song2)
                mixed = mesh[:length].overlay(song2)
                play(mixed)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Sci_fi.wav')
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('meow.wav')
                song2 = loop2.reverse()
                length = len(song2)
                mixed = mesh[:length].overlay(song2)
                play(mixed)

        elif self.mode24==1 and self.songnum3==1: #warstwowanie i od tylu
            liczba = random.randint(0, 30)
            if self.textbox.text()=='Miau':
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('meow.wav')
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                song2 = loop2.reverse()
                length = len(song2)
                mixed = mesh[:length].overlay(song2)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                play(mixed2)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('dzwonek.wav')
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                song2 = loop2.reverse()
                length = len(song2)
                mixed = mesh[:length].overlay(song2)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                play(mixed2)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Drum_Roll.wav')
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                song2 = loop2.reverse()
                length = len(song2)
                mixed = mesh[:length].overlay(song2)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                play(mixed2)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                loop2 = AudioSegment.from_wav('Sci_fi.wav')
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                song2 = loop2.reverse()
                length = len(song2)
                mixed = mesh[:length].overlay(song2)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                play(mixed2)

        elif self.mode25 == 1:  #od tylu i znikanie
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                length=len(song22)
                fade_time = int(length * self.timefade)
                faded = song22.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                length=len(song22)
                fade_time = int(length * self.timefade)
                faded = song22.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                length=len(song22)
                fade_time = int(length * self.timefade)
                faded = song22.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                length=len(song22)
                fade_time = int(length * self.timefade)
                faded = song22.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode24==1 and self.songnum4==1: #warstwowanie i od tylu
            print("odtwarzanie")
            loop2 = AudioSegment.from_wav('meow.wav')
            mesh = AudioSegment.from_wav('Sci_fi.wav')
            song2 = loop2.reverse()
            length = len(song2)
            mixed = mesh[:length].overlay(song2)
            mesh2=AudioSegment.from_wav('Drum_Roll.wav')
            length2=len(mixed)
            mixed2=mesh2[:length2].overlay(mixed)
            mesh3=AudioSegment.from_wav('dzwonek.wav')
            length3=len(mixed2)
            mixed3=mesh3[:length3].overlay(mixed2)
            play(mixed3)

        elif self.mode23==1: #petla i znikanie
            if self.textbox.text()=='Miau':
                print("mode11")
                song5 = AudioSegment.from_wav('meow.wav')
                song20 = song5 * self.loopnumber
                length = len(song20)
                fade_time = int(length * self.timefade)
                faded = song20.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song5= AudioSegment.from_wav('dzwonek.wav')
                song20 = song5 * self.loopnumber
                length = len(song20)
                fade_time = int(length * self.timefade)
                faded = song20.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('Drum_Roll.wav')
                song20 = song5 * self.loopnumber
                length = len(song20)
                fade_time = int(length * self.timefade)
                faded = song20.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song5 = AudioSegment.from_wav('Sci_fi.wav')
                song20 = song5 * self.loopnumber
                length = len(song20)
                fade_time = int(length * self.timefade)
                faded = song20.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode41 == 1 and self.songnum2==1:  #wszystko
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie41")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                length=len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                length2=len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie41")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie41")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie41")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode41 == 1 and self.songnum3==1:  #wszystko
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie41")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                length=len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(song22)
                length3=len(mixed)
                mixed2=mesh2[:length3].overlay(mixed)
                loop2=mixed2*self.loopnumber
                length2=len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie41")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                mixed = mesh[:length].overlay(song22)
                length3=len(mixed)
                mixed2=mesh2[:length3].overlay(mixed)
                loop2=mixed2*self.loopnumber
                length2=len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie41")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(song22)
                length3=len(mixed)
                mixed2=mesh2[:length3].overlay(mixed)
                loop2=mixed2*self.loopnumber
                length2=len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie41")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(song22)
                length3=len(mixed)
                mixed2=mesh2[:length3].overlay(mixed)
                loop2=mixed2*self.loopnumber
                length2=len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode41 == 1 and self.songnum4==1:  #wszystko
            print("odtwarzanie41")
            song20 = AudioSegment.from_wav('meow.wav')
            song22 = song20.reverse()
            length=len(song22)
            mesh = AudioSegment.from_wav('Sci_fi.wav')
            mixed = mesh[:length].overlay(song22)
            mesh2=AudioSegment.from_wav('Drum_Roll.wav')
            length2=len(mixed)
            mixed2=mesh2[:length2].overlay(mixed)
            length3=len(mixed2)
            mesh3=AudioSegment.from_wav('dzwonek.wav')
            mixed3=mesh3[:length3].overlay(mixed2)
            loop2=mixed3*self.loopnumber
            length4=len(loop2)
            fade_time = int(length4 * self.timefade)
            faded = loop2.fade_in(fade_time).fade_out(fade_time)
            play(faded)

        elif self.mode22 == 1 and self.songnum4 == 1:
            print("odtwarzanie")
            song20 = AudioSegment.from_wav('meow.wav')
            length = len(song20)
            mesh = AudioSegment.from_wav('Sci_fi.wav')
            mixed = mesh[:length].overlay(song20)
            mesh2 = AudioSegment.from_wav('Drum_Roll.wav')
            length2 = len(mixed)
            mixed2 = mesh2[:length2].overlay(mixed)
            length3 = len(mixed2)
            mesh3 = AudioSegment.from_wav('dzwonek.wav')
            mixed3 = mesh3[:length3].overlay(mixed2)
            loop2 = mixed3 * self.loopnumber
            play(loop2)

        elif self.mode22 == 1 and self.songnum2==1:  #petla i warstwowanie
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                length=len(song20)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song20)
                loop2 = mixed * self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                length = len(song20)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song20)
                loop2=mixed*self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song22 = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                length = len(song)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song)
                loop2=mixed*self.loopnumber
                play(loop2)

        elif self.mode22 == 1 and self.songnum3==1:  #petla i warstwowanie
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                length=len(song20)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(song20)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                loop2 = mixed2 * self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                length = len(song20)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                mixed = mesh[:length].overlay(song20)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                loop2 = mixed2 * self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song22 = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(song22)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                loop2 = mixed2 * self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                length = len(song)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(song)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                loop2 = mixed2 * self.loopnumber
                play(loop2)

        elif self.mode21 == 1:  #petla i od tylu
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                loop2=song22*self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                loop2=song22*self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                loop2=song22*self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                loop2=song22*self.loopnumber
                play(loop2)

        elif self.mode31 == 1:  #petla, od tylu, znikanie
            if self.textbox.text() == 'Miau':
                print("odtwarzanie31")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                loop2=song22*self.loopnumber
                length2=len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                loop2=song22*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                loop2=song22*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                loop2=song22*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode32 == 1 and self.songnum4 == 1:
            print("odtwarzanie")
            song20 = AudioSegment.from_wav('meow.wav')
            song22 = song20.reverse()
            length = len(song22)
            mesh = AudioSegment.from_wav('Sci_fi.wav')
            mixed = mesh[:length].overlay(song22)
            mesh2 = AudioSegment.from_wav('Drum_Roll.wav')
            length2 = len(mixed)
            mixed2 = mesh2[:length2].overlay(mixed)
            length3 = len(mixed2)
            mesh3 = AudioSegment.from_wav('dzwonek.wav')
            mixed3 = mesh3[:length3].overlay(mixed2)
            loop2 = mixed3 * self.loopnumber
            play(loop2)

        elif self.mode32 == 1 and self.songnum2==1:  #petla, od tylu, warstwowanie
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                length=len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song22)
                loop2=mixed*self.loopnumber
                play(loop2)

        elif self.mode32 == 1 and self.songnum3 == 1:  # petla, od tylu, warstwowanie
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song22)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                loop2 = mixed2 * self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song22)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                loop2 = mixed2 * self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                mixed = mesh[:length].overlay(song22)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                loop2 = mixed2 * self.loopnumber
                play(loop2)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                mixed = mesh[:length].overlay(song22)
                length2=len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                loop2 = mixed2 * self.loopnumber
                play(loop2)

        elif self.mode34 == 1 and self.songnum4 == 1:
            print("odtwarzanie")
            song20 = AudioSegment.from_wav('meow.wav')
            song22 = song20.reverse()
            length = len(song22)
            mesh = AudioSegment.from_wav('Sci_fi.wav')
            mixed = mesh[:length].overlay(song22)
            mesh2 = AudioSegment.from_wav('Drum_Roll.wav')
            length2 = len(mixed)
            mixed2 = mesh2[:length2].overlay(mixed)
            length3 = len(mixed2)
            mesh3 = AudioSegment.from_wav('dzwonek.wav')
            mixed3 = mesh3[:length3].overlay(mixed2)
            length2 = len(mixed3)
            fade_time = int(length2 * self.timefade)
            faded = mixed3.fade_in(fade_time).fade_out(fade_time)
            play(faded)

        elif self.mode34 == 1 and self.songnum2==1:  #znikanie, warstwowanie, tyl
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                length=len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                length2=len(mixed)
                fade_time = int(length2 * self.timefade)
                faded = mixed.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                length2 = len(mixed)
                fade_time = int(length2 * self.timefade)
                faded = mixed.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song22)
                length2 = len(mixed)
                fade_time = int(length2 * self.timefade)
                faded = mixed.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song22)
                length2 = len(mixed)
                fade_time = int(length2 * self.timefade)
                faded = mixed.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode34 == 1 and self.songnum3 == 1:  # znikanie, warstwowanie, tyl
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                song22 = song20.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song22)
                length2 = len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                length3=len(mixed2)
                fade_time = int(length3 * self.timefade)
                faded = mixed2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                song22 = song20.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song22)
                length2 = len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                length3=len(mixed2)
                fade_time = int(length3 * self.timefade)
                faded = mixed2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                mixed = mesh[:length].overlay(song22)
                length2 = len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                length3=len(mixed2)
                fade_time = int(length3 * self.timefade)
                faded = mixed2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                song22 = song.reverse()
                length = len(song22)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song22)
                length2 = len(mixed)
                mixed2=mesh2[:length2].overlay(mixed)
                length3=len(mixed2)
                fade_time = int(length3 * self.timefade)
                faded = mixed2.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode33 == 1 and self.songnum4 == 1:
            print("odtwarzanie")
            song20 = AudioSegment.from_wav('meow.wav')
            length = len(song20)
            mesh = AudioSegment.from_wav('Sci_fi.wav')
            mixed = mesh[:length].overlay(song20)
            mesh2 = AudioSegment.from_wav('Drum_Roll.wav')
            length2 = len(mixed)
            mixed2 = mesh2[:length2].overlay(mixed)
            length3 = len(mixed2)
            mesh3 = AudioSegment.from_wav('dzwonek.wav')
            mixed3 = mesh3[:length3].overlay(mixed2)
            loop2 = mixed3 * self.loopnumber
            length2 = len(loop2)
            fade_time = int(length2 * self.timefade)
            faded = loop2.fade_in(fade_time).fade_out(fade_time)
            play(faded)

        elif self.mode33 == 1 and self.songnum2==1:  #petla, warstwowanie, znikanie
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                length=len(song20)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song20)
                loop2=mixed*self.loopnumber
                length2=len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                length = len(song20)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song20)
                loop2=mixed*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(song)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                mixed = mesh[:length].overlay(song)
                loop2=mixed*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                length = len(song)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                else:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song)
                loop2=mixed*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)

        elif self.mode33 == 1 and self.songnum3==1:  #petla, warstwowanie, znikanie
            liczba = random.randint(0, 30)
            if self.textbox.text() == 'Miau':
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('meow.wav')
                length=len(song20)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song20)
                length3=len(mixed)
                mixed2=mesh2[:length3].overlay(mixed)
                loop2=mixed2*self.loopnumber
                length2=len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                song20 = AudioSegment.from_wav('dzwonek.wav')
                length = len(song20)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                mixed = mesh[:length].overlay(song20)
                length3=len(mixed)
                mixed2=mesh2[:length3].overlay(mixed)
                loop2=mixed2*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Drum_Roll.wav')
                length = len(song)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Sci_fi.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Sci_fi.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(song)
                length3=len(mixed)
                mixed2=mesh2[:length3].overlay(mixed)
                loop2=mixed2*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                song = AudioSegment.from_wav('Sci_fi.wav')
                length = len(song)
                if liczba <= 10:
                    mesh = AudioSegment.from_wav('meow.wav')
                    mesh2=AudioSegment.from_wav('Drum_Roll.wav')
                elif liczba > 10 and liczba <= 20:
                    mesh = AudioSegment.from_wav('dzwonek.wav')
                    mesh2=AudioSegment.from_wav('meow.wav')
                else:
                    mesh = AudioSegment.from_wav('Drum_Roll.wav')
                    mesh2=AudioSegment.from_wav('dzwonek.wav')
                mixed = mesh[:length].overlay(song)
                length3=len(mixed)
                mixed2=mesh2[:length3].overlay(mixed)
                loop2=mixed2*self.loopnumber
                length2 = len(loop2)
                fade_time = int(length2 * self.timefade)
                faded = loop2.fade_in(fade_time).fade_out(fade_time)
                play(faded)
        else:
            if self.textbox.text()=='Miau':
                print("odtwarzaniee")
                playsound('meow.wav')
            elif self.textbox.text() == "Dzwonek":
                print("odtwarzanie")
                playsound('dzwonek.wav')
            elif self.textbox.text() == "Beben":
                print("odtwarzanie")
                playsound('Drum_Roll.wav')
            elif self.textbox.text() == "Robot":
                print("odtwarzanie")
                playsound('Sci_fi.wav')

    def __init__(self): #tworzenie obiektu
        super().__init__() #odwołanie do konstruktora rodzica tej klasy
        self.title = "Odtwarzacz"
        self.left = 200
        self.top = 50
        self.width = 590
        self.height = 840
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: solid gray;")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox1=QLineEdit(self)
        self.textbox.move(20, 60) #przesuwam okinko
        self.textbox.resize(400, 40)
        self.textbox.setText('')
        self.textbox1.move(20, 20)  # przesuwam okinko
        self.textbox1.resize(400, 40)
        self.textbox1.setStyleSheet("background-color: solid gray;")
        self.textbox1.setText('Wybrany przez ciebie dzwiek:')
        self.textbox3=QLineEdit(self)
        self.textbox3.move(20, 170)
        self.textbox3.resize(400,40)
        self.textbox3.setText("Wybrany przez ciebie efekt/efekty:")
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(140, 240)
        self.textbox2.resize(400, 40)
        self.textbox2.setText("Wybrana przez ciebie ilosc obiegu petli: ")
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(140, 280)
        self.textbox6.resize(400, 40)
        self.textbox6.setText(" ")
        self.textbox7 = QLineEdit(self)
        self.textbox7.move(140, 400)
        self.textbox7.resize(400, 40)
        self.textbox7.setText("Wybrana przez ciebie ilosc warstwowanych ze soba piosenek: ")
        self.textbox8 = QLineEdit(self)
        self.textbox8.move(140, 440)
        self.textbox8.resize(400, 40)
        self.textbox8.setText(" ")
        self.textbox9 = QLineEdit(self)
        self.textbox9.move(140, 560)
        self.textbox9.resize(400, 40)
        self.textbox9.setText("Wybrany przez ciebie czas pojawiania sie i znikania:")
        self.textbox10 = QLineEdit(self)
        self.textbox10.move(140, 600)
        self.textbox10.resize(400, 40)
        self.textbox10.setText("")

        self.buttons1 = QPushButton('Miau', self)
        self.buttons1.move(20, 110)
        self.buttons1.setStyleSheet("background-color : magenta")
        self.buttons1.clicked.connect(self.click)

        self.buttons2 = QPushButton('Dzwonek', self)
        self.buttons2.move(120, 110)
        self.buttons2.setStyleSheet("background-color : magenta")
        self.buttons2.clicked.connect(self.click)

        self.buttons3 = QPushButton('Beben', self)
        self.buttons3.move(220, 110)
        self.buttons3.setStyleSheet("background-color : magenta")
        self.buttons3.clicked.connect(self.click)

        self.buttons4 = QPushButton('Robot', self)
        self.buttons4.move(320, 110)
        self.buttons4.setStyleSheet("background-color : magenta")
        self.buttons4.clicked.connect(self.click)

        self.buttonplay = QCheckBox('Petla', self)
        self.buttonplay.move(20, 240)
        self.buttonplay.setStyleSheet("background-color : pink")
        self.buttonplay.toggled.connect(self.productclick)

        self.buttonplay1 = QCheckBox('Od tylu', self)
        self.buttonplay1.move(20, 720)
        self.buttonplay1.setStyleSheet("background-color : pink")
        self.buttonplay1.toggled.connect(self.productclick)

        self.buttonplay2 = QCheckBox('Warstwowanie', self)
        self.buttonplay2.move(20, 400)
        self.buttonplay2.setStyleSheet("background-color : pink")
        self.buttonplay2.toggled.connect(self.productclick)


        self.buttonplay3 = QCheckBox('Znikanie', self)
        self.buttonplay3.move(20, 560)
        self.buttonplay3.setStyleSheet("background-color : pink")
        self.buttonplay3.toggled.connect(self.productclick)

        self.buttonkoniec=QPushButton('Graj', self)
        self.buttonkoniec.move(240, 750)
        self.buttonkoniec.resize(120,80)
        self.buttonkoniec.setStyleSheet("background-color : magenta")
        self.buttonkoniec.clicked.connect(self.play)

        self.buttonloop2=QPushButton('2', self)
        self.buttonloop2.move(140, 330)
        self.buttonloop2.setStyleSheet('background-color:cyan')
        self.buttonloop2.clicked.connect(self.loopclick)
        self.buttonloop3=QPushButton('3', self)
        self.buttonloop3.move(240, 330)
        self.buttonloop3.setStyleSheet('background-color:cyan')
        self.buttonloop3.clicked.connect(self.loopclick)
        self.buttonloop4=QPushButton('4', self)
        self.buttonloop4.move(340, 330)
        self.buttonloop4.setStyleSheet('background-color:cyan')
        self.buttonloop4.clicked.connect(self.loopclick)
        self.buttonloop5=QPushButton('5', self)
        self.buttonloop5.move(440, 330)
        self.buttonloop5.setStyleSheet('background-color:cyan')
        self.buttonloop5.clicked.connect(self.loopclick)

        self.buttonmesh2=QPushButton('2', self)
        self.buttonmesh2.move(140, 490)
        self.buttonmesh2.setStyleSheet('background-color:red')
        self.buttonmesh2.clicked.connect(self.songnumclick)
        self.buttonmesh3=QPushButton('3', self)
        self.buttonmesh3.move(240, 490)
        self.buttonmesh3.setStyleSheet('background-color:red')
        self.buttonmesh3.clicked.connect(self.songnumclick)
        self.buttonmesh4=QPushButton('4', self)
        self.buttonmesh4.move(340, 490)
        self.buttonmesh4.setStyleSheet('background-color:red')
        self.buttonmesh4.clicked.connect(self.songnumclick)

        self.buttonkrotka=QPushButton('Krotki', self)
        self.buttonkrotka.move(140, 650)
        self.buttonkrotka.setStyleSheet('background-color:yellow')
        self.buttonkrotka.clicked.connect(self.timeclick)
        self.buttonsrednia=QPushButton('Sredni', self)
        self.buttonsrednia.move(240, 650)
        self.buttonsrednia.setStyleSheet('background-color:yellow')
        self.buttonsrednia.clicked.connect(self.timeclick)
        self.buttondluga=QPushButton('Dlugi', self)
        self.buttondluga.move(340, 650)
        self.buttondluga.setStyleSheet('background-color:yellow')
        self.buttondluga.clicked.connect(self.timeclick)

        self.buttonplay.setToolTip('Wybierz efekt')
        self.buttonplay1.setToolTip('Wybierz efekt')
        self.buttonplay2.setToolTip('Wybierz efekt')
        self.buttonplay3.setToolTip('Wybierz efekt')

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
