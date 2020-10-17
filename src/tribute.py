#fighting 
import random


class Tribute:
    def _init_(self, name, survival, fight, hide)
    	self.name = name
    	self.survival = survival
    	self.fight = fight
    	self.hide = fight 
    
    def fight():
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
