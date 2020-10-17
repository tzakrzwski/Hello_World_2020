#fighting 
import random


class tribute:
    def __init__(self, name, survival, fight, hide):
    	self.name = name
    	self.survival = survival
    	self.fight = fight
    	self.hide = fight 
    	self.isAlive = True
    	
    def getIsAlive(self): 
        return self.isAlive
    def setIsAlive(self):
        self.isAlive = False
        return self.isAlive
    def getName(self):
        return self.name
        

    def battle(self):
        if int(self.fight) == 1:
            likelyhood = random.randint(0, 60);
        elif int(self.fight) == 2:
            likelyhood = random.randint(20, 80);
        elif int(self.fight) == 3:
            likelyhood = random.randint(40, 100);
        elif int(self.fight) == 4:
            likelyhood = random.randint(60, 100);
        else:
            likelyhood = random.randint(80, 100);
        return likelyhood
    
    def survive(self):
        if int(self.survival) == 1:
            LikelyhoodSurvive = random.randint(25, 100); # 66% chance of living
        elif int(self.survival) == 2:
            LikelyhoodSurvive = random.randint(35, 100); # 77% chance of living
        elif int(self.survival) == 3:
            LikelyhoodSurvive = random.randint(40, 100); #83% chance of living
        elif int(self.survival) == 4:
            LikelyhoodSurvive = random.randint(45, 100); # 90% chance
        else:
            LikelyhoodSurvive = random.randint(50, 100); #100% chance
        if LikelyhoodSurvive > 50:
            LiveAnotherDay = True
        else:
            LiveAnotherDay = False
        return LiveAnotherDay
