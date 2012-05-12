from panda3d.core import *
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from panda3d.core import Vec3
from direct.gui.OnscreenText import OnscreenText
from pandac.PandaModules import TextNode
import random
from panda3d.core import *
from pandac.PandaModules import *
from direct.gui.OnscreenText import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.ShowBase import ShowBase
from commands import *

cx = 1
class UserInterfaceEnv(ShowBase):
    def __init__(self, cmnd_Object):
        self.cmnd = cmnd_Object
        self.n = 0
        cmnd = ""
        self.commandBox = ""
        self.store = ["","","",""]
        ShowBase.__init__(self)
        self.title1 = self.AddTitle(-0.65, "Type your commands here:")
        self.title2 = self.AddTitle(0.90, "You have entered:")
        self.instArea = self.AddInstructions(0.82, cmnd)
        self.cmndArea = self.AddArea()
        base.setFrameRateMeter(True)
        base.setBackgroundColor(0,0,0)
        self.model = False
        self.text = False
        self.link = False
        self.person = True
        self.balls = {}
        

         # cam
        self.cam.setPos(15, -30, 22)
        light = PointLight('light')
        self.render.setLight(self.cam.attachNewNode(light))
        self.cam.lookAt(0,0,0)

    # Function to put instructions on the screen.
    def AddInstructions(self, pos, msg):
        return OnscreenText(text=msg , style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

    # Function to put title on the screen.
    def AddTitle(self, pos, text):
        return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                   pos=(-1.3, pos), align=TextNode.ALeft, scale = .08)

        # Function to add command line are
    def AddArea(self):
        # Username textbox where you type in your username
        p = Vec3(-1.3, 0.0, -0.75)
        self.commandBox = DirectEntry(text = "" , width = 40,  pos = p, scale=.07, command=self.SetText,
                        extraArgs=[self], focus=1, numLines = 3)

    #callback function to set  text
    def SetText(self, textEntered, dummy):
        self.commandBox.enterText('')
        self.commandBox.setFocus()
        oldText = self.instArea.getText()
        self.cmnd.Parse(textEntered)
        if self.person == False:
            self.instArea.setText(oldText + textEntered +" does not exist.\n- - - - - - - - - - - - - - - - - - - - - -\n" )
        if self.person == True:
            self.instArea.setText(oldText + textEntered +"\n- - - - - - - - - - - - - - - - - - - - - -\n" )
        self.store[self.n] = textEntered
        self.n += self.n
        self.commandBox.accept('arrow_up', self.GetHistory, [-1] )

    #function to maintain history
    def GetHistory(self, a):
            self.commandBox.enterText(self.store[self.n])
            self.n -= self.n
        
    def center(self, prsn_name):
        if self.model == True and self.text == True:
            self.sphere.remove()
            self.newTextNodePath1.remove()
        X = "textures/"+prsn_name + '.jpeg'
        tex = loader.loadTexture(X)
        self.sphere = loader.loadModel("models/ball1.egg")
        self.sphere.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
        self.sphere.setTexture(tex, 1)
        self.sphere.reparentTo(render)
        self.sphere.setPos(1, 1, 1)
        self.sphere.setScale(2.5)
        text = prsn_name
        newTextNode = TextNode('text') # Create a new TextNode
        newTextNode.setText(text) # Set the TextNode text
        newTextNode.setAlign(TextNode.ACenter) # Set the text align
        newTextNode.setWordwrap(6.0) # Set the word wrap
        text_generate = newTextNode.generate() # Generate a NodePath
        self.newTextNodePath1 = render.attachNewNode(text_generate) # Attach the NodePath to the render tree
        self.newTextNodePath1.setPos(1, 1, 2)
        self.newTextNodePath1.setColor(255, 0, 0,1)
        self.newTextNodePath1.setScale(.8)

    def addball(self, NUM):
        #pos = Vec3(random.uniform(-7, 7), random.uniform(-7, 7), random.uniform(-7, 7))
        if self.model == True and self.text == True:
            self.f.remove()
            self.newTextNodePath2.remove()
        a = random.uniform(-7, 7)
        b = random.uniform(-7, 7)
        c = random.uniform(-7, 7)
        pos = Vec3(a,b,c)
        tex = loader.loadTexture("textures/e.jpeg")
        self.f = loader.loadModel("models/ball1.egg")
        self.f.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
        self.f.setTexture(tex, 1)
        self.f.setPos(pos)
        self.f.setScale(1.5)
        self.f.reparentTo(render)
        self.f.setCollideMask(0)
        text = NUM
        newTextNode = TextNode('text') # Create a new TextNode
        newTextNode.setText(text) # Set the TextNode text
        newTextNode.setAlign(TextNode.ACenter) # Set the text align
        newTextNode.setWordwrap(6.0) # Set the word wrap
        text_generate = newTextNode.generate() # Generate a NodePath
        self.newTextNodePath2 = render.attachNewNode(text_generate) # Attach the NodePath to the render tree
        self.newTextNodePath2.setPos(a,b,(c + 0.3))
        self.newTextNodePath2.setColor(255, 0, 0,1)
        self.newTextNodePath2.setScale(.6)
        return pos

    def drawLine(self,startPoint,endPoint,color,thickness):
        #if color is None: color = (100,100,100,100)
        #if thickness is None: thickness = .4
        if self.link == True:
            self.nodePath.remove()    
        linesegs = LineSegs("lines")
        linesegs.setColor(color)
        linesegs.setThickness(thickness)
        linesegs.moveTo(startPoint)
        linesegs.drawTo(endPoint)
        node = linesegs.create(False)
        self.nodePath = render.attachNewNode(node)
        #self.nodePath.setShader()


    def separate_in (self, calls):
        #...data ...seperate incomming
        in_list = []
        for a in calls:
            for b in a:
                if b['type'] == 'incoming':
                    in_list.append(b)
        return in_list
        exit()

            #print in_list


    def separate_out (self, calls =[]):
    #...data ...seperate outgoing
        oout_list = []
        for a in calls:
            for b in a:
                if b['type'] == 'outgoing':
                    oout_list.append(b);
        return oout_list
        exit()
            #print out_list

    def colours (self, a):
        if a == 'c':
            coloursss = (0,147,255,1)
            return coloursss
        elif a == 'm':
            coloursss = (0,255,0,1)
            return coloursss
        elif a == 'e':
            coloursss = (0,255,180,1)
            return coloursss
        elif a == 'ce':
            coloursss = (255,20,147,1)
            return coloursss
        elif a == 'cm':
            coloursss = (0,0,255,1)
            return coloursss
        elif a == 'me':
            coloursss = (255,0,0,1)
            return coloursss
        elif a == 'cme':
            coloursss = (0,180,255,1)
            return coloursss
        elif a == 'ecm':
            coloursss = (128,0,128,1)
            return coloursss
        else :
            coloursss = (0,255,255,1)
            return coloursss


    def durations (self, inn_list=[]):
         for aList1 in inn_list:
                for aList2 in inn_list:
                    if aList1['from']==aList2['from'] and aList1 !=aList2:
                        a= aList1['duration']
                        b= aList2['duration']
                        a = a + b
                        aList1['duration'] = a
                        inn_list.remove(aList2)
         return inn_list


    def merge (self, a=[]):
        L1 = a
        L2 = []
        for l in L1:
            for j in l:
                L2.append(j)
        a = L2
        for aList1 in a:
                for aList2 in a:
                    if aList1['from']==aList2['from'] and aList1 !=aList2:
                        x= aList1['duration']
                        y= aList2['duration']
                        x = x + y
                        aList1['duration'] = x

                        j = aList1['key']
                        i = aList2['key']
                        i = j+i
                        aList1['key'] = i
                        a.remove(aList2)
        return a

    def merge_out (self, p=[]):
        L1 = p
        L2 = []
        for l in L1:
            for j in l:
                L2.append(j)
        p = L2
        for aList1 in p:
                for aList2 in p:
                    if aList1['from']==aList2['from'] and aList1 !=aList2:
                        x= aList1['duration']
                        y= aList2['duration']
                        x = x + y
                        aList1['duration'] = x

                        j = aList1['key']
                        i = aList2['key']
                        i = j+i
                        aList1['key'] = i
                        p.remove(aList2)
        return p



