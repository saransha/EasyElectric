import pygame
pygame.init()

class Synths2(object):
    def __init__(self):
        self.C8=pygame.mixer.Sound(file='Synths WAV/6/c1.wav')
        self.B7=pygame.mixer.Sound(file='Synths WAV/6/c2.wav')
        self.Bb7=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.A7=pygame.mixer.Sound(file='Synths WAV/6/c4.wav')
        self.Ab7=pygame.mixer.Sound(file='Synths WAV/6/e1.wav')
        self.G7=pygame.mixer.Sound(file='Synths WAV/6/e2.wav')
        self.Gb7=pygame.mixer.Sound(file='Synths WAV/6/e3.wav')
        self.F7=pygame.mixer.Sound(file='Synths WAV/6/g#1.wav')
        self.E7=pygame.mixer.Sound(file='Synths WAV/6/g#2.wav')
        self.Eb7=pygame.mixer.Sound(file='Synths WAV/6/g#3.wav')
        self.D7=pygame.mixer.Sound(file='Synths WAV/7/c1.wav')
        self.Db7=pygame.mixer.Sound(file='Synths WAV/7/c2.wav')
        self.C7=pygame.mixer.Sound(file='Synths WAV/7/c3.wav')
        self.B6=pygame.mixer.Sound(file='Synths WAV/7/c4.wav')
        self.Bb6=pygame.mixer.Sound(file='Synths WAV/7/e1.wav')
        self.A6=pygame.mixer.Sound(file='Synths WAV/7/e2.wav')
        self.Ab6=pygame.mixer.Sound(file='Synths WAV/7/e3.wav')
        self.G6=pygame.mixer.Sound(file='Synths WAV/7/g#1.wav')
        self.Gb6=pygame.mixer.Sound(file='Synths WAV/7/g#2.wav')
        self.F6=pygame.mixer.Sound(file='Synths WAV/7/g#3.wav')
        self.E6=pygame.mixer.Sound(file='Synths WAV/8/c1.wav')
        self.Eb6=pygame.mixer.Sound(file='Synths WAV/8/c2.wav')
        self.D6=pygame.mixer.Sound(file='Synths WAV/8/c3.wav')
        self.Db6=pygame.mixer.Sound(file='Synths WAV/8/c4.wav')
        self.C6=pygame.mixer.Sound(file='Synths WAV/8/c5.wav')
        self.B5=pygame.mixer.Sound(file='Synths WAV/8/e1.wav')
        self.Bb5=pygame.mixer.Sound(file='Synths WAV/8/e2.wav')
        self.A5=pygame.mixer.Sound(file='Synths WAV/8/e3.wav')
        self.Ab5=pygame.mixer.Sound(file='Synths WAV/8/e4.wav')
        self.G5=pygame.mixer.Sound(file='Synths WAV/8/g#1.wav')
        self.Gb5=pygame.mixer.Sound(file='Synths WAV/8/g#2.wav')
        self.F5=pygame.mixer.Sound(file='Synths WAV/8/g#3.wav')
        self.E5=pygame.mixer.Sound(file='Synths WAV/8/g#4.wav')
        self.Eb5=pygame.mixer.Sound(file='Synths WAV/9/c1.wav')
        self.D5=pygame.mixer.Sound(file='Synths WAV/9/c2.wav')
        self.Db5=pygame.mixer.Sound(file='Synths WAV/9/c3.wav')
        self.C5=pygame.mixer.Sound(file='Synths WAV/9/c4.wav')
        self.B4=pygame.mixer.Sound(file='Synths WAV/9/c5.wav')
        self.Bb4=pygame.mixer.Sound(file='Synths WAV/9/e1.wav')
        self.A4=pygame.mixer.Sound(file='Synths WAV/9/e2.wav')
        self.Ab4=pygame.mixer.Sound(file='Synths WAV/9/e3.wav')
        self.G4=pygame.mixer.Sound(file='Synths WAV/9/e4.wav')
        self.Gb4=pygame.mixer.Sound(file='Synths WAV/9/g#1.wav')
        self.F4=pygame.mixer.Sound(file='Synths WAV/9/g#2.wav')
        self.E4=pygame.mixer.Sound(file='Synths WAV/9/g#3.wav')
        self.Eb4=pygame.mixer.Sound(file='Synths WAV/9/g#4.wav')
        self.D4=pygame.mixer.Sound(file='Synths WAV/10/c1.wav')
        self.Db4=pygame.mixer.Sound(file='Synths WAV/10/c2.wav')
        self.C4=pygame.mixer.Sound(file='Synths WAV/10/c3.wav')
        self.B3=pygame.mixer.Sound(file='Synths WAV/10/c4.wav')
        self.Bb3=pygame.mixer.Sound(file='Synths WAV/10/c5.wav')
        self.A3=pygame.mixer.Sound(file='Synths WAV/10/e1.wav')
        self.Ab3=pygame.mixer.Sound(file='Synths WAV/10/e2.wav')
        self.G3=pygame.mixer.Sound(file='Synths WAV/10/e3.wav')
        self.Gb3=pygame.mixer.Sound(file='Synths WAV/10/e4.wav')
        self.F3=pygame.mixer.Sound(file='Synths WAV/10/g#1.wav')
        self.E3=pygame.mixer.Sound(file='Synths WAV/10/g#2.wav')
        self.Eb3=pygame.mixer.Sound(file='Synths WAV/10/g#3.wav')
        self.D3=pygame.mixer.Sound(file='Synths WAV/10/g#4.wav')
        self.Db3=pygame.mixer.Sound(file='Synths WAV/11/bd01.wav')
        self.C3=pygame.mixer.Sound(file='Synths WAV/11/cp01.wav')
        self.B2=pygame.mixer.Sound(file='Synths WAV/11/cr01.wav')
        self.Bb2=pygame.mixer.Sound(file='Synths WAV/11/hh01.wav')
        self.A2=pygame.mixer.Sound(file='Synths WAV/11/ht01.wav')
        self.Ab2=pygame.mixer.Sound(file='Synths WAV/11/lt01.wav')
        self.G2=pygame.mixer.Sound(file='Synths WAV/11/mt01.wav')
        self.Gb2=pygame.mixer.Sound(file='Synths WAV/11/oh01.wav')
        self.F2=pygame.mixer.Sound(file='Synths WAV/11/rd01.wav')
        self.E2=pygame.mixer.Sound(file='Synths WAV/11/rs01.wav')
        self.Eb2=pygame.mixer.Sound(file='Synths WAV/11/sd01.wav')
        self.D2=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.Db2=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.C2=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.B1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.Bb1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.A1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.Ab1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.G1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.Gb1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.F1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.E1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.Eb1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.D1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.Db1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.C1=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.B0=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.Bb0=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.A0=pygame.mixer.Sound(file='Synths WAV/blank.wav')
        self.notes=[]
        self.hscrollDX=0
        self.pianoGrid = pygame.image.load('Piano grid.png').convert_alpha()
        self.sx2,self.sx3=0,870
        self.scrollGrid=(self.sx2,0,self.sx3,350)

    def __str__(self):
            return "self.synth2"