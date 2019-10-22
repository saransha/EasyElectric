import pygame
pygame.init()
from pygamegame import PygameGame # taken from https://raw.githubusercontent.
#                         com/LBPeraza/Pygame-Asteroids/master/pygamegame.py 
from Piano import Piano 
from Synths1 import Synths1
from Synths2 import Synths2
#from pydub import AudioSegment

class Master(object):
    def __init__(self,i1,i2,i3):
        self.notes=i1.notes+i2.notes+i3.notes
        self.hscrollDX=0#i1.hscrollDX
        self.pianoGrid = i1.pianoGrid
        self.sx2,self.sx3=0,870
        #self.sx2,self.sx3=i1.sx2,i1.sx3
        self.scrollGrid=(self.sx2,0,self.sx3,350)

class Note(object):
    def __init__(self,x,y,inst,scroll,prevScroll,color=None,dx=0,relDX=0):
        self.x,self.relDX=x,relDX
        if(color==(255,0,0)):#self.y=(int((y-420)/15.2)*15.2)+420
            if((y/15.2)-int(y/15.2)<0.5):self.y=(int(y/15.2)*15.2)-2.5
            else:self.y=(int(y/15.2)*15.2)+13
        else:self.y=y # black notes snapping will be done later
        self.iX,self.iY=x,y
        self.inst=inst
        self.drawColor=color
        self.scrollCount=scroll
        self.prevScroll=prevScroll
        self.DNE=False
        self.dx=dx
        self.startTime=int(1000*((relDX+x-110)/36))
        self.length=int(1000*(dx/36)) # in ms
        if(x<=110):self.length=1000
        self.note=None
        self.identifyNote()
        if(self.note==None):self.DNE=True
        if(color==(0,0,255)):
            if((y/15.2)-int(y/15.2)<0.5):self.y=(int(y/15.2)*15.2)+5
            else:self.y=(int(y/15.2)*15.2)+7

    def __repr__(self):
        return "Note(%d,%d,%s,%d,%d,%s,%d,%d)" % (self.x,self.y,
            self.inst.__str__(),self.scrollCount,self.prevScroll,
            str(self.drawColor),self.dx,self.relDX)

    def intersectsWith(self,x,y):
        return (self.x<=x<=self.x+self.dx and self.y<=y<=self.y+11)

    def identifyNote(self):
        instr=self.inst
        whiteNotes=[instr.C8,instr.B7,instr.A7,instr.G7,instr.F7,instr.E7,
        instr.D7,instr.C7,instr.B6,instr.A6,instr.G6,instr.F6,instr.E6,
        instr.D6,instr.C6,instr.B5,instr.A5,instr.G5,instr.F5,instr.E5,
        instr.D5,instr.C5,instr.B4,instr.A4,instr.G4,instr.F4,instr.E4,
        instr.D4,instr.C4,instr.B3,instr.A3,instr.G3,instr.F3,instr.E3,
        instr.D3,instr.C3,instr.B2,instr.A2,instr.G2,instr.F2,instr.E2,
        instr.D2,instr.C2,instr.B1,instr.A1,instr.G1,instr.F1,instr.E1,
        instr.D1,instr.C1,instr.B0,instr.A0]
        blackNotes=[instr.Bb7,instr.Ab7,instr.Gb7,instr.Eb7,instr.Db7,
        instr.Bb6,instr.Ab6,instr.Gb6,instr.Eb6,instr.Db6,instr.Bb5,instr.Ab5,
        instr.Gb5,instr.Eb5,instr.Db5,instr.Bb4,instr.Ab4,instr.Gb4,instr.Eb4,
        instr.Db4,instr.Bb3,instr.Ab3,instr.Gb3,instr.Eb3,instr.Db3,instr.Bb2,
        instr.Ab2,instr.Gb2,instr.Eb2,instr.Db2,instr.Bb1,instr.Ab1,instr.Gb1,
        instr.Eb1,instr.Db1,instr.Bb0]
        if(self.scrollCount==0):
            whiteNotes=whiteNotes[:23]
            blackNotes=blackNotes[:15]
        elif(self.scrollCount==1 and self.prevScroll==0):
            whiteNotes=whiteNotes[16:39]
            blackNotes=blackNotes[11:27]
        elif(self.scrollCount==1 and self.prevScroll==2):
            whiteNotes=whiteNotes[13:36]
            blackNotes=blackNotes[9:25]
        else:
            whiteNotes=whiteNotes[29:]
            blackNotes=blackNotes[20:]
        note=-1
        ny=self.y-420
        if(self.x>20 and self.x<=85 or self.drawColor==(0,0,255)):
            if(self.scrollCount==0):
                if(ny>=24 and ny<=35):note=0
                elif(ny>=39 and ny<=50):note=1
                elif(ny>=54 and ny<=65):note=2
                elif(ny>=85 and ny<=96):note=3
                elif(ny>=100 and ny<=111):note=4
                elif(ny>=131 and ny<=142):note=5
                elif(ny>=146 and ny<=157):note=6
                elif(ny>=161 and ny<=172):note=7               
                elif(ny>=192 and ny<=203):note=8
                elif(ny>=207 and ny<=218):note=9
                elif(ny>=238 and ny<=249):note=10
                elif(ny>=253 and ny<=264):note=11
                elif(ny>=268 and ny<=279):note=12                
                elif(ny>=299 and ny<=310):note=13
                elif(ny>=314 and ny<=325):note=14
            elif(self.scrollCount==1 and self.prevScroll==0):
                if(ny>=9 and ny<=20):note=0
                elif(ny>=24 and ny<=35):note=1
                elif(ny>=55 and ny<=66):note=2
                elif(ny>=70 and ny<=81):note=3
                elif(ny>=101 and ny<=112):note=4
                elif(ny>=116 and ny<=127):note=5
                elif(ny>=131 and ny<=142):note=6
                elif(ny>=162 and ny<=173):note=7
                elif(ny>=177 and ny<=188):note=8
                elif(ny>=208 and ny<=219):note=9
                elif(ny>=223 and ny<=234):note=10
                elif(ny>=238 and ny<=249):note=11
                elif(ny>=269 and ny<=280):note=12
                elif(ny>=284 and ny<=295):note=13
                elif(ny>=315 and ny<=326):note=14
                elif(ny>=330 and ny<=341):note=15
            elif(self.scrollCount==1 and self.prevScroll==2):
                if(ny>=9 and ny<=20):note=0
                elif(ny>=40 and ny<=51):note=1
                elif(ny>=55 and ny<=66):note=2
                elif(ny>=70 and ny<=81):note=3
                elif(ny>=101 and ny<=112):note=4
                elif(ny>=116 and ny<=127):note=5
                elif(ny>=147 and ny<=158):note=6
                elif(ny>=162 and ny<=173):note=7
                elif(ny>=177 and ny<=188):note=8
                elif(ny>=208 and ny<=219):note=9
                elif(ny>=223 and ny<=234):note=10
                elif(ny>=254 and ny<=265):note=11
                elif(ny>=269 and ny<=280):note=12
                elif(ny>=284 and ny<=295):note=13
                elif(ny>=315 and ny<=326):note=14
                elif(ny>=330 and ny<=341):note=15
            else:
                if(ny>=9 and ny<=20):note=0
                elif(ny>=24 and ny<=35):note=1
                elif(ny>=39 and ny<=50):note=2
                elif(ny>=70 and ny<=81):note=3
                elif(ny>=85 and ny<=96):note=4
                elif(ny>=116 and ny<=127):note=5
                elif(ny>=131 and ny<=142):note=6
                elif(ny>=146 and ny<=157):note=7
                elif(ny>=177 and ny<=188):note=8
                elif(ny>=192 and ny<=203):note=9
                elif(ny>=223 and ny<=234):note=10
                elif(ny>=238 and ny<=249):note=11
                elif(ny>=253 and ny<=264):note=12
                elif(ny>=284 and ny<=295):note=13
                elif(ny>=299 and ny<=310):note=14
                elif(ny>=330 and ny<=341):note=15
        wnote=int(ny/15.2)
        if(self.drawColor==None):
            if(note==-1):self.note=whiteNotes[wnote]
            else:self.note=blackNotes[note]
        elif(self.drawColor==(255,0,0)):
            self.note=whiteNotes[wnote]
        elif(self.drawColor==(0,0,255) and note!=-1):
            self.note=blackNotes[note]

    def play(self):
        if(self.length==0):self.note.play()
        else:self.note.play(maxtime=self.length)

    def draw(self,screen):
        if(not self.DNE and self.x+self.dx>=110 and self.x<=980 and 
            self.y>=420 and self.y<=770):
            dx=min(self.dx,980-self.x)
            if(self.x<110):dx=dx-(110-self.x)
            pygame.draw.rect(screen,self.drawColor,
              pygame.Rect((max(111,self.x),self.y),(dx,11)),3)

class Daw(PygameGame):
    def init(self):
        self.timeFont = pygame.font.Font(None, 15)
        self.bgColor=(0,0,0)
        self.pianoRoll = pygame.image.load('Piano.png').convert_alpha()
        #picture taken from- (http://www.adultpianolesson.com/wp-content/
        #uploads/2010/05/88-key-piano-keyboard-layout.jpg)
        self.pianoGridDX=pygame.image.load('Piano grid dx.png').convert_alpha()
        self.heading=pygame.image.load('Heading.png').convert_alpha()
        self.subHeading=pygame.image.load('subHeading.png').convert_alpha()
        self.instructions=pygame.image.load('Instructions.png').convert_alpha()
        self.dec=pygame.image.load('decoration.png').convert_alpha()
        self.dec2=pygame.image.load('dec2.png').convert_alpha()
        self.sx0,self.sy0,self.sx1,self.sy1=(0,0,150,350)
        self.scrollPiano=(self.sx0,self.sy0,self.sx1,self.sy1)
        self.piano=Piano()
        self.synth1=Synths1()
        self.synth2=Synths2()
        self.scrollCount=0
        self.prevScroll=0
        self.curInst=self.piano
        self.crX,self.crY,self.crDX=None,None,0
        self.curRect=False
        self.tickerX=110
        self.tickerTime=0
        self.play=False
        self.master=False
        self.curNote=None
        self.delMode=False
        self.repeat=False
        self.repeatCount=0
        self.repeat=False
        self.repNote,self.repeatInterval=None,None
        self.masterNotes=None
        self.saveString=""
        self.instruct=False

    @staticmethod
    def readFile(path):
        with open(path, "rt") as f:
            return f.read()

    @staticmethod
    def writeFile(path, contents):
        with open(path, "wt") as f:
            f.write(contents)

    def save(self):
        self.saveString=""
        for note in self.piano.notes:
            self.saveString+="\nself.piano.notes.append("+note.__repr__()+")"
        for note in self.synth1.notes:
            self.saveString+="\nself.synth1.notes.append("+note.__repr__()+")"
        for note in self.synth2.notes:
            self.saveString+="\nself.synth2.notes.append("+note.__repr__()+")"
        self.writeFile("savefile.txt",self.saveString)

    def load(self):
        #loads data from the foob
        loadString=self.readFile("savefile.txt")
        self.__init__(1000,800,60,"Easy Electric")
        self.piano.notes=[]
        self.synth1.notes=[]
        self.synth2.notes=[]
        loadString=loadString.strip()
        for line in loadString.splitlines():
            eval(line)
    #ditched for now coz cant convert Sound object back to wav
    """def export(self):
        self.masterFunc()
        output=AudioSegment.empty()
        master=sorted(self.masterNotes.notes,key=lambda time:time.startTime)
        prevNote=AudioSegment.empty()
        for note in master:
            n= AudioSegment.from_file()
            #n=AudioSegment(note.note,format="wav")
            if(note.length!=0):
                n=n[:note.length]
            output+=AudioSegment.silent(duration=note.startTime
                -prevNote.startTime)
            output+=n
            prevNote=note
        file_handle = output.export("output.mp3", format="mp3")"""

    def masterFunc(self):
        self.tickerX=110
        self.tickerTime=0
        w1=self.piano.pianoGrid.get_width()
        w2=self.synth1.pianoGrid.get_width()
        w3=self.synth1.pianoGrid.get_width()
        for inst in [self.piano,self.synth1,self.synth2]:
            for note in inst.notes:
                note.x+=inst.hscrollDX
            inst.hscrollDX=0
            inst.sx2,inst.sx3=0,870
        if(w1>w2 and w1>w3):
            self.masterNotes=Master(self.piano,self.synth1,self.synth2)
        elif(w2>w1 and w2>w3):
            self.masterNotes=Master(self.synth1,self.piano,self.synth2)
        else:self.masterNotes=Master(self.synth2,self.piano,self.synth1)
        self.curInst=self.masterNotes

    def mousePressed(self, x, y):
        note=None
        if(840<=x<=990):
            if(240<=y<=300):
                self.play=not self.play
                if(self.play):pygame.mixer.unpause()
                else:pygame.mixer.pause()
            elif(30<=y<=90):
                self.load()
            elif(100<=y<=160):
                self.save()
            elif(170<=y<=230):
                self.instruct=not self.instruct
        if(y>=340 and y<=400):
            if(20<=x<=170):
                self.master=False
                self.curInst=self.piano
            elif(180<=x<=330):
                self.master=False
                self.curInst=self.synth1
            elif(340<=x<=490):
                self.master=False
                self.curInst=self.synth2
            elif(520<=x<=670):
                self.delMode=not self.delMode
            elif(x>=680 and x<=830):
                self.repeat=not self.repeat
                self.repNote,self.repeatInterval=None,None
                self.repeatCount=0
            elif(840<=x<=990):
                self.master=True
                self.masterFunc()
        elif(x>=20 and x<=110 and y>=400 and y<=420):
            self.prevScroll=self.scrollCount
            self.scrollCount=max(0,self.scrollCount-1)
            if(self.sy0==450 or self.sy0==250):
                for note in self.curInst.notes:note.y+=250
            elif(self.sy0==200):
                for note in self.curInst.notes:note.y+=200
            self.sy0=max(0,self.sy0-250)
        elif(x>=20 and x<=110 and y>=770 and y<=790):
            self.prevScroll=self.scrollCount
            self.scrollCount=min(2,self.scrollCount+1)
            if(self.sy0==0 or self.sy0==200):
                for note in self.curInst.notes:note.y-=250
            elif(self.sy0==250):
                for note in self.curInst.notes:note.y-=200
            self.sy0=min(450,self.sy0+250)
        elif(x>=980 and x<=1000 and y>=420 and y<=770):
            if(self.repeat):pass
            self.rightScroll()
        elif(x>=0 and x<=19 and y>=420 and y<770):
            if(self.repeat):pass
            self.curInst.sx2=max(0,self.curInst.sx2-36)
            if(self.curInst.hscrollDX>0):
                self.tickerTime-=1000
            if(self.curInst.hscrollDX>0):
                for note in self.curInst.notes:note.x+=36
            self.curInst.hscrollDX=max(0,self.curInst.hscrollDX-36)
        elif(not self.master and x>=20 and x<=110 and y>=420 and y<=770):
            note=Note(x,y,self.curInst,self.scrollCount,self.prevScroll)  
            note.play()
        elif(x>=110 and x<=980 and y>=420 and y<=770 and not self.master):
            check=False
            self.remove=False
            if(self.delMode):
                for note in self.curInst.notes:
                    if(note.intersectsWith(x,y)):
                        check=True
                        self.curNote=note
                        break
            elif(self.isKeyPressed(306)):
                for note in self.curInst.notes:
                    if(note.intersectsWith(x,y)):
                        check=True
                        self.curNote=note
            if(not check and not self.delMode and not self.repeat):
                self.curRect=True
                self.crX,self.crY=x,y
        elif(x>=110 and x<=980 and y>=410 and y<420):
            pygame.mixer.stop()
            self.tickerX=x
            self.tickerTime=int(1000*((self.curInst.hscrollDX+
                self.tickerX-110)/36))
        self.scrollPiano=(self.sx0,self.sy0,self.sx1,self.sy1)
        self.curInst.scrollGrid=(self.curInst.sx2,self.sy0,
            self.curInst.sx3,self.sy1)
    
    def rightScroll(self,auto=False):
        self.curInst.sx2+=36
        if(not auto):self.tickerTime+=1000
        if(self.curInst.sx2+self.curInst.sx3>
             self.curInst.pianoGrid.get_width()):
            piano=pygame.Surface((self.curInst.pianoGrid.get_width()+36,
                                    self.curInst.pianoGrid.get_height()))
            piano.blit(self.curInst.pianoGrid,(0,0))
            piano.blit(self.pianoGridDX,(self.curInst.pianoGrid.get_width(),1))
            self.curInst.pianoGrid=piano
        for note in self.curInst.notes:note.x-=36
        self.curInst.hscrollDX+=36

    def mouseReleased(self, x, y):
        if(self.repeat and x>=110 and x<=980 and y>=420 and y<=790):
            if(self.repeatCount==0):
                for note in self.curInst.notes:
                    if(note.intersectsWith(x,y)):
                        self.repNote=note
                        self.repeatCount+=1
                        break
            elif(self.repeatCount==1):
                self.repeatInterval=x-self.repNote.x
                self.repeatCount+=1
            elif(self.repeatCount==2):
                for dx in range(self.repNote.x+self.repeatInterval,x,
                    self.repeatInterval):
                    self.curInst.notes.append(Note(dx,self.repNote.y,
                    self.repNote.inst,self.repNote.scrollCount,
                    self.repNote.prevScroll,self.repNote.drawColor,
                    self.repNote.dx,self.curInst.hscrollDX))
                self.repeat=False
                self.repNote,self.repeatInterval=None,None
                self.repeatCount=0
        elif(self.curNote!=None):
            if(self.delMode):
                self.curInst.notes.remove(self.curNote)
                self.delMode=False
            else:
                color,dx=self.curNote.drawColor,self.curNote.dx
                self.curNote.__init__(x,y,self.curInst,self.scrollCount,
                    self.prevScroll,color,dx,self.curInst.hscrollDX)
            self.curNote=None
        elif(x>=110 and x<=980 and y>=420 and y<=790 and not self.master and 
             not self.delMode):
            self.curRect=False
            color=(255,0,0)
            if(self.isKeyPressed(304) or self.isKeyPressed(303)):
                color=(0,0,255)
            if(self.crY!=None):
                note=Note(self.crX,self.crY,self.curInst,self.scrollCount,
                self.prevScroll,color,self.crDX,self.curInst.hscrollDX)
            if(not note.DNE):
                self.curInst.notes.append(note)
            self.crX,self.crY,self.crDX=None,None,0

    def mouseDrag(self, x, y):
        if(not self.delMode and not self.repeat):
            if(self.curRect):
                if(x>=110 and x<=980 and y>=420 and y<=790):
                    self.crDX=x-self.crX
            elif(self.curNote!=None):
                if(x>=110 and x<=980 and y>=420 and y<=790):
                    self.curNote.x,self.curNote.y=x,y
    
    def mouseMotion(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if(self.isKeyPressed(308)):
            self.delMode=not self.delMode
        if(keyCode==pygame.K_SPACE):
            self.play=not self.play
            if(self.play):pygame.mixer.unpause()
            else:pygame.mixer.pause()
        self.save()

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        if(self.play):
            self.tickerX+=dt*0.036
            self.tickerTime+=dt
            if(self.tickerX+self.curInst.hscrollDX-110>=
                self.curInst.pianoGrid.get_width()):
                self.play=not self.play
            elif(self.tickerX>=908 and 
                abs(self.curInst.pianoGrid.get_width()-(self.tickerX+
                    self.curInst.hscrollDX-110))>=72):
                self.rightScroll(True)
                self.rightScroll(True)
                self.tickerX-=72
            for note in self.curInst.notes:
                if(self.tickerTime-30<note.startTime<=self.tickerTime+30):
                    note.play()
                    continue

    def drawCurrentRect(self,screen):
        color=(255,255,0)
        if(self.isKeyPressed(304) or self.isKeyPressed(303)):#shifts pressed
            color=(0,255,0)
        pygame.draw.rect(screen,color,
            pygame.Rect((self.crX,self.crY),(self.crDX,11)))

    def redrawAll(self, screen):
        font=pygame.font.Font(None, 30)
        font2=pygame.font.Font(None, 20)
        screen.blit(self.heading,(10,10))
        screen.blit(self.subHeading,(25,150))
        screen.blit(self.dec,(190,110))
        screen.blit(self.dec2,(10,200))
        pygame.draw.rect(screen,(184,184,184),pygame.Rect((20,400),(90,15)))
        pygame.draw.polygon(screen,(255,127,127),[(30,414),(60,400),(90,414)])
        pygame.draw.rect(screen,(184,184,184),pygame.Rect((20,775),(90,15)))
        pygame.draw.polygon(screen,(255,127,127),[(30,776),(60,789),(90,776)])
        pygame.draw.rect(screen,(184,184,184),pygame.Rect((980,420),(15,350)))
        pygame.draw.polygon(screen,(255,127,127),[(980,520),
            (993,595),(980,670)])
        pygame.draw.rect(screen,(184,184,184),pygame.Rect((5,420),(13,350)))
        pygame.draw.polygon(screen,(255,127,127),[(17,520),(5,595),(17,670)])
        pygame.draw.rect(screen,(204,153,255),pygame.Rect((110,400),(990,15)))
        pygame.draw.rect(screen,(204,153,255),pygame.Rect((110,775),(990,15)))
        screen.blit(self.pianoRoll,(20,420),area=self.scrollPiano)
        screen.blit(self.curInst.pianoGrid,(112,420),
            area=self.curInst.scrollGrid)
        for note in self.curInst.notes:note.draw(screen)
        if(self.curRect):self.drawCurrentRect(screen)
        pygame.draw.rect(screen,(255,0,0),
            pygame.Rect((self.tickerX,415),(3,360)))
        if(self.curInst==self.piano):
            pygame.draw.rect(screen,(165,255,170),
                pygame.Rect((20,340),(150,60)))
        else:pygame.draw.rect(screen,(255,204,204),
            pygame.Rect((20,340),(150,60)))
        if(self.curInst==self.synth1):
            pygame.draw.rect(screen,(165,255,170),
                pygame.Rect((180,340),(150,60)))
        else:pygame.draw.rect(screen,(255,204,204),
            pygame.Rect((180,340),(150,60)))
        if(self.curInst==self.synth2):
            pygame.draw.rect(screen,(165,255,170),
                pygame.Rect((340,340),(150,60)))
        else:pygame.draw.rect(screen,(255,204,204),
            pygame.Rect((340,340),(150,60)))
        if(self.delMode):
            pygame.draw.rect(screen,(165,255,170),
                pygame.Rect((520,340),(150,60)))
        else:pygame.draw.rect(screen,(255,204,204),
            pygame.Rect((520,340),(150,60)))
        if(self.repeat):
            pygame.draw.rect(screen,(165,255,170),
                pygame.Rect((680,340),(150,60)))
        else:pygame.draw.rect(screen,(255,204,204),
            pygame.Rect((680,340),(150,60)))
        if(self.curInst==self.masterNotes):
            pygame.draw.rect(screen,(165,255,170),
                pygame.Rect((840,340),(150,60)))
        else:pygame.draw.rect(screen,(255,204,204),
            pygame.Rect((840,340),(150,60)))
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((20,340),(150,58)),2)
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((180,340),(150,58)),2)
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((340,340),(150,58)),2)
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((520,340),(150,58)),2)
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((680,340),(150,58)),2)
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((840,340),(150,58)),2)
        pygame.draw.rect(screen,(155,0,0),pygame.Rect((10,330),(990,5)))
        pygame.draw.rect(screen,(155,0,0),pygame.Rect((503,330),(7,67)))
        pygame.draw.rect(screen,(255,204,204),pygame.Rect((840,30),(150,60)))
        pygame.draw.rect(screen,(255,204,204),pygame.Rect((840,100),(150,60)))
        pygame.draw.rect(screen,(255,204,204),pygame.Rect((840,170),(150,60)))
        if(self.play):
            pygame.draw.rect(screen,(165,255,170),
                pygame.Rect((840,240),(150,60)))
        else:pygame.draw.rect(screen,(255,204,204),
            pygame.Rect((840,240),(150,60)))
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((840,30),(150,60)),2)
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((840,100),(150,60)),2)
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((840,170),(150,60)),2)
        pygame.draw.rect(screen,(0,0,200),pygame.Rect((840,240),(150,60)),2)
        name=font.render("Load", 1, (0,0,0))
        screen.blit(name, (890, 50))
        name=font.render("Save", 1, (0,0,0))
        screen.blit(name, (890, 120))
        name=font.render("Instructions", 1, (0,0,0))
        screen.blit(name, (860, 190))
        name=font.render("Play/Pause", 1, (0,0,0))
        screen.blit(name, (865, 250))
        name=font2.render("(Space)", 1, (0,0,0))
        screen.blit(name, (900, 275))
        time=1+self.curInst.hscrollDX//36
        name=font.render("Grand Piano", 1, (0,0,0))
        screen.blit(name, (35, 360))
        name=font.render("Synth Set 1", 1, (0,0,0))
        screen.blit(name, (200, 360))
        name=font.render("Synth Set 2", 1, (0,0,0))
        screen.blit(name, (360, 360))
        name=font.render("Delete Mode", 1, (0,0,0))
        screen.blit(name, (535, 350))
        name=font.render("Repeat Note", 1, (0,0,0))
        screen.blit(name, (695, 360))
        if(self.repeat):
            name=font2.render(str(self.repeatCount), 1, (0,0,0))
            screen.blit(name, (750, 378))
        name=font2.render("(Alt)", 1, (0,0,0))
        screen.blit(name, (585, 375))
        name=font.render("Master", 1, (0,0,0))
        screen.blit(name, (880, 360))
        for x in range(146,self.curInst.pianoGrid.get_width()+111,36):
            text = self.timeFont.render(str(time), 1, (0,0,0))
            screen.blit(text, (x, 401))
            screen.blit(text, (x, 776))
            time+=1
        if(self.instruct):screen.blit(self.instructions,(10,0))


d1=Daw(1000,800,60,"Easy Electric")
d1.run()

