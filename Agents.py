import random 
R = random.Random(123456789)

class BaseAgent:
    name = ""
    def __init__(self):
        self.nextAction = None
        
    
    def learnFromPreviousStep(self,action):
        self.nextAction = None
#===============================================

class AllD_Agent(BaseAgent):
    name = "ALLD"
    def __init__(self):
        self.nextAction = 1
    
    def learnFromPreviousStep(self,action):
        return

#===============================================


class Random_Agent(BaseAgent):
    name = "RANDOM"
    def __init__(self):
        self.nextAction = R.randint(0,1)
    
    def learnFromPreviousStep(self,action):
        self.nextAction = R.randint(0,1)

#===============================================


class TFT_Agent(BaseAgent):
    name = "TIT FOR TAT"
    def __init__(self):
        self.nextAction = 0
    
    def learnFromPreviousStep(self,action):
        self.nextAction = action

#===============================================

class Tester_Agent(BaseAgent):
    name = "TESTER"
    def __init__(self):
        self.nextAction = 1
        self.i = 0
        self.actionRotation = [0,0,1]
        self.triggered = False

    def learnFromPreviousStep(self,action):
        if action:
            self.triggered = True

        if self.triggered:
            self.nextAction = action
        else:
            self.i = (self.i+1) % 3
            self.nextAction = self.actionRotation[self.i]
#===================================================

class Joss_Agent(BaseAgent):
    name = "JOSS"
    def __init__(self):
        self.nextAction = 0
    
    def learnFromPreviousStep(self,action):
        act = action
        if not action:
            act = 1 if R.random() > 0.1 else 0
        
        self.nextAction = act

#================================================

class AllC_Agent(BaseAgent):
    name = "ALLC"
    def __init__(self):
        self.nextAction = 0
    
    def learnFromPreviousStep(self,action):
        return

#================================================

class BIPHASE_Agent(BaseAgent):
    name = "BIPHASE"
    def __init__(self):
        self.nextAction = 0
    
    def learnFromPreviousStep(self,action):
        self.nextAction = 0 if self.nextAction else 1 