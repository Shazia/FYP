from methods import *
from filter1 import *
from export import *
from imporT import *
from display import *
import shlex

class CommandManipulation():
    def __init__(self):
        self.input = []
        self.command = ""
        self.argument = ""
        self.filt = Filter(self)
        #self.glw = Glow()
        self.imp = Import()
        self.exp = Export()
        #self.disp = Display()

    def Parse(self, textEntered):
        self.input = shlex.split(textEntered)
        self.command = self.input[0]
        self.argument1 = self.input[1]
        self.argument2 = self.input[2]
        self.CallModule()

    def CallModule(self):
        if self.command == "Filter":
            self.filt.filter(self.argument1)
        #elif self.command == "Glow":
         #   self.glw.glow(self.argument1)
        elif self.command == "Import":
            self.imp.import1(self.argument1, self.argument2)
        elif self.command == "Export":
            self.exp.export1(self.argument1, self.argument2)
        #elif self.command == "Show":
         #   self.disp.show(self.argument1)
        

        
